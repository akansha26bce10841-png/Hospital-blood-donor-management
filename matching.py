"""
matching.py
Demonstrates:
- Classes and Objects (BloodMatchingEngine)
- Dictionary lookup and membership operators
- Operator precedence and associativity in scoring formulas
- Division with mixed data types (float / and integer //)
- Arithmetic operators (+, -, *, /, //)
- Logical operators (and, or, not)
- Selection sort using beginner loops
- FrozentSet checks for universal donors and recipients
"""

from utils import is_donor_ready_for_emergency, aggregate_hospital_units_array
from data import UNIVERSAL_DONORS, UNIVERSAL_RECIPIENTS

class BloodMatchingEngine:
    """
    Engine responsible for rule-based blood matching between
    emergency requests, volunteer donors, and hospital inventories.
    """
    def __init__(self, compatibility_table):
        self.compatibility_table = compatibility_table

    def is_compatible(self, donor_group, recipient_group):
        """
        Determines if donor blood group can safely be transfused to recipient.
        Demonstrates dictionary lookup and membership operator 'in'.
        """
        if recipient_group in self.compatibility_table:
            allowed_donors = self.compatibility_table[recipient_group]
            return donor_group in allowed_donors
        return False

    def calculate_donor_priority(self, donor, request):
        """
        Calculates a priority score for candidate donors.
        Demonstrates:
        - Operator precedence and associativity: addition, subtraction, integer division
        - Relational and ternary evaluation
        """
        # City proximity bonus
        if donor.city.lower() == request.city.lower():
            city_bonus = 100
        else:
            city_bonus = 40

        # Exact group match bonus
        if donor.blood_group == request.blood_group:
            type_bonus = 30
        else:
            type_bonus = 15

        # Age factor: prefer younger adult donors slightly
        # Integer division: donor.age // 10
        age_factor = donor.age // 10

        # Operator Precedence Demonstration:
        # Parentheses ensure grouping, followed by addition and subtraction from left to right
        total_score = (city_bonus + type_bonus) - age_factor
        return total_score

    def find_matching_donors(self, request, donor_list):
        """
        Finds all compatible, active donors for an emergency blood request.
        Sorts matches in descending order of priority using a simple beginner selection sort.
        """
        candidate_donors = []

        for donor in donor_list:
            # Rule 1: Donor must be compatible with recipient
            compatible = self.is_compatible(donor.blood_group, request.blood_group)

            # Rule 2: Donor must be verified ready (age eligible + available status)
            ready = is_donor_ready_for_emergency(donor)

            if compatible and ready:
                candidate_donors.append(donor)

        # Simple beginner selection sort by priority score (descending)
        n = len(candidate_donors)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                score_j = self.calculate_donor_priority(candidate_donors[j], request)
                score_max = self.calculate_donor_priority(candidate_donors[max_idx], request)
                if score_j > score_max:
                    max_idx = j
            # Swap elements
            temp = candidate_donors[i]
            candidate_donors[i] = candidate_donors[max_idx]
            candidate_donors[max_idx] = temp

        return candidate_donors

    def find_matching_hospitals(self, request, hospital_list):
        """
        Finds hospitals holding compatible blood units in stock.
        Prioritizes hospitals in the same city.
        """
        matching_hospitals = []
        for hospital in hospital_list:
            # Check if hospital has at least 1 unit of any compatible blood group
            compatible_groups = self.compatibility_table.get(request.blood_group, ())
            has_stock = False
            for bg in compatible_groups:
                if hospital.get_units(bg) > 0:
                    has_stock = True
                    break

            if has_stock:
                matching_hospitals.append(hospital)

        return matching_hospitals

    def execute_emergency_matching(self, request, donor_list, hospital_list):
        """
        Executes a complete matching operation and displays detailed findings.
        Demonstrates:
        - Frozen set membership checks
        - Mixed type division (float / and int)
        - Array data structure aggregation
        """
        print("\n=======================================================")
        print("          EMERGENCY BLOOD MATCHING REPORT              ")
        print("=======================================================")
        request.display_details()

        # Check Frozen Set categories
        if request.blood_group in UNIVERSAL_RECIPIENTS:
            print("[INFO] Patient Blood Group is AB+ (Universal Recipient: can receive all compatible types).")

        # 1. MATCH HOSPITALS
        print("\n--- [1] MATCHED HOSPITAL BLOOD BANKS ---")
        matched_hospitals = self.find_matching_hospitals(request, hospital_list)

        # Use array aggregation utility to count exact requested blood units in hospitals
        units_array, total_exact_units = aggregate_hospital_units_array(matched_hospitals, request.blood_group)

        if len(matched_hospitals) == 0:
            print("No hospitals currently have stock for compatible blood groups.")
        else:
            print(f"Found {len(matched_hospitals)} hospital(s) with compatible stock:")
            for h in matched_hospitals:
                exact_units = h.get_units(request.blood_group)
                is_local = "[LOCAL]" if h.city.lower() == request.city.lower() else "[OUTSTATION]"
                print(f" -> {is_local} {h.name} ({h.city}) | Tel: {h.phone}")
                print(f"    Available '{request.blood_group}' Units: {exact_units}")

        # 2. MATCH DONORS
        print("\n--- [2] MATCHED VOLUNTEER DONORS ---")
        matched_donors = self.find_matching_donors(request, donor_list)

        if len(matched_donors) == 0:
            print("No available volunteer donors found matching compatibility criteria.")
        else:
            print(f"Found {len(matched_donors)} eligible donor(s) sorted by priority:")
            for rank, donor in enumerate(matched_donors, start=1):
                score = self.calculate_donor_priority(donor, request)
                location_tag = "[LOCAL]" if donor.city.lower() == request.city.lower() else "[OUTSTATION]"
                universal_tag = " (Universal Donor O-)" if donor.blood_group in UNIVERSAL_DONORS else ""
                print(f" {rank}. {location_tag} [{donor.donor_id}] {donor.name} | Group: {donor.blood_group}{universal_tag} | City: {donor.city} | Tel: {donor.phone} | Score: {score}")

        # 3. FULFILLMENT & SHORTAGE SUMMARY
        print("\n--- [3] EMERGENCY FULFILLMENT SUMMARY ---")
        print(f"Total Units Requested      : {request.units_needed}")
        print(f"Exact Units In Hospitals   : {total_exact_units}")
        print(f"Potential Volunteer Donors : {len(matched_donors)}")

        # Mixed data type division demonstration:
        # float division (total_exact_units * 100.0) / request.units_needed
        if request.units_needed > 0:
            fulfillment_ratio = (total_exact_units * 100.0) / request.units_needed
        else:
            fulfillment_ratio = 100.0

        # Calculate shortage
        shortage = request.units_needed - total_exact_units
        if shortage < 0:
            shortage = 0

        print(f"Immediate Hospital Coverage: {fulfillment_ratio:.1f}%")
        print(f"Remaining Blood Deficit    : {shortage} unit(s)")

        if shortage == 0:
            print(">> STATUS: FULLY COVERED by hospital blood bank reserves.")
        elif len(matched_donors) >= shortage:
            print(f">> STATUS: HOSPITAL SHORTAGE CAN BE COVERED by reaching {shortage} of the {len(matched_donors)} matched donors.")
        else:
            print(">> STATUS: CRITICAL SHORTAGE! Both hospital units and volunteer donors are insufficient.")

        print("=======================================================\n")
