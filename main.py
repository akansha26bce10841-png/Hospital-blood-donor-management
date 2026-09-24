"""
main.py
Command Line Emergency Blood Donor and Hospital Matching Engine

Main entry point for the application.
Demonstrates:
- Control flow (while, if, elif, else, break, continue)
- Function calls and modular imports
- input() and print() interactions
- Set and list operations for system overview
- Clean navigation without unexpected program termination
"""

import sys
from donor import (
    Donor,
    find_donor_by_id,
    filter_donors_by_blood_group,
    filter_available_donors,
    get_unique_donor_cities
)
from hospital import (
    Hospital,
    find_hospital_by_id,
    filter_hospitals_by_city,
    filter_hospitals_with_blood_group
)
from blood_request import BloodRequest
from matching import BloodMatchingEngine
from data import (
    VALID_BLOOD_GROUPS,
    STANDARD_CITIES,
    BLOOD_COMPATIBILITY,
    UNIVERSAL_DONORS,
    UNIVERSAL_RECIPIENTS,
    RH_NEGATIVE_GROUPS,
    get_initial_donors,
    get_initial_hospitals
)
from utils import (
    read_non_empty_string,
    read_integer,
    read_blood_group,
    read_phone,
    read_yes_no,
    aggregate_hospital_units_array
)


def handle_donor_management(donors):
    """Sub-menu for managing volunteer donors."""
    while True:
        print("\n----------------------------------------")
        print("         DONOR MANAGEMENT MENU          ")
        print("----------------------------------------")
        print("1. Add a New Donor")
        print("2. View All Donors")
        print("3. Search Donors by Blood Group")
        print("4. Search Currently Available Donors")
        print("5. Update Donor Availability")
        print("6. Return to Main Menu")
        print("----------------------------------------")

        choice = read_integer("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            print("\n--- Add New Donor ---")
            donor_id = read_non_empty_string("Enter Donor ID (e.g., D111): ").upper()

            # Check if ID already exists (using identity check is not None)
            existing_donor = find_donor_by_id(donors, donor_id)
            if existing_donor is not None:
                print(f">> Error: Donor with ID {donor_id} already exists!")
                continue

            name = read_non_empty_string("Enter Full Name: ")
            age = read_integer("Enter Age (18-65): ", 18, 65)
            blood_group = read_blood_group("Enter Blood Group: ", VALID_BLOOD_GROUPS)
            city = read_non_empty_string("Enter City: ")
            phone = read_phone("Enter 10-digit Phone: ")
            is_avail = read_yes_no("Is donor currently available? (yes/no): ")

            new_donor = Donor(donor_id, name, age, blood_group, city, phone, is_avail)
            donors.append(new_donor)
            print(f">> Success: Donor '{name}' ({donor_id}) added successfully.")

        elif choice == 2:
            print(f"\n--- Registered Donors ({len(donors)}) ---")
            if len(donors) == 0:
                print("No donors registered yet.")
            else:
                for d in donors:
                    d.display_details()

        elif choice == 3:
            print("\n--- Search Donors by Blood Group ---")
            bg = read_blood_group("Enter Blood Group to search: ", VALID_BLOOD_GROUPS)
            matches = filter_donors_by_blood_group(donors, bg)
            print(f"Found {len(matches)} donor(s) with Blood Group '{bg}':")
            for d in matches:
                d.display_details()

        elif choice == 4:
            print("\n--- Currently Available Donors ---")
            available = filter_available_donors(donors)
            print(f"Total Available Donors: {len(available)}")
            for d in available:
                d.display_details()

        elif choice == 5:
            print("\n--- Update Donor Availability ---")
            donor_id = read_non_empty_string("Enter Donor ID to update: ").upper()
            donor = find_donor_by_id(donors, donor_id)

            # Demonstrating identity operator 'is None'
            if donor is None:
                print(f">> Error: No donor found with ID '{donor_id}'.")
            else:
                current_status = "Available" if donor.is_available else "Unavailable"
                print(f"Donor Found: {donor.name} (Current: {current_status})")
                new_status = read_yes_no("Set new availability (yes = Available / no = Unavailable): ")
                donor.set_availability(new_status)
                print(f">> Success: Availability for {donor.name} updated to {new_status}.")

        elif choice == 6:
            break


def handle_hospital_management(hospitals):
    """Sub-menu for managing hospitals and blood inventories."""
    while True:
        print("\n----------------------------------------")
        print("        HOSPITAL MANAGEMENT MENU        ")
        print("----------------------------------------")
        print("1. Add a New Hospital")
        print("2. View All Hospitals and Inventories")
        print("3. Search Hospitals by City")
        print("4. Update Hospital Blood Stock")
        print("5. Return to Main Menu")
        print("----------------------------------------")

        choice = read_integer("Enter your choice (1-5): ", 1, 5)

        if choice == 1:
            print("\n--- Add New Hospital ---")
            h_id = read_non_empty_string("Enter Hospital ID (e.g., H206): ").upper()

            # Check if ID already exists (identity check)
            existing_h = find_hospital_by_id(hospitals, h_id)
            if existing_h is not None:
                print(f">> Error: Hospital with ID {h_id} already exists!")
                continue

            name = read_non_empty_string("Enter Hospital Name: ")
            city = read_non_empty_string("Enter City: ")
            phone = read_non_empty_string("Enter Emergency Phone: ")

            # Build initial inventory dictionary
            print("Enter initial blood stock units:")
            inventory = {}
            for bg in VALID_BLOOD_GROUPS:
                units = read_integer(f"Units for {bg} (0 or more): ", 0, 1000)
                inventory[bg] = units

            new_hospital = Hospital(h_id, name, city, inventory, phone)
            hospitals.append(new_hospital)
            print(f">> Success: Hospital '{name}' ({h_id}) added successfully.")

        elif choice == 2:
            print(f"\n--- Registered Hospitals ({len(hospitals)}) ---")
            if len(hospitals) == 0:
                print("No hospitals registered.")
            else:
                for h in hospitals:
                    h.display_details()

        elif choice == 3:
            print("\n--- Search Hospitals by City ---")
            city = read_non_empty_string("Enter City name: ")
            matches = filter_hospitals_by_city(hospitals, city)
            print(f"Found {len(matches)} hospital(s) in '{city}':")
            for h in matches:
                h.display_details()

        elif choice == 4:
            print("\n--- Update Hospital Blood Stock ---")
            h_id = read_non_empty_string("Enter Hospital ID: ").upper()
            hospital = find_hospital_by_id(hospitals, h_id)

            if hospital is None:
                print(f">> Error: No hospital found with ID '{h_id}'.")
            else:
                print(f"Hospital: {hospital.name} ({hospital.city})")
                bg = read_blood_group("Enter Blood Group to update: ", VALID_BLOOD_GROUPS)
                current_units = hospital.get_units(bg)
                print(f"Current units of {bg}: {current_units}")
                delta = read_integer("Enter number of units to add (e.g. 5, or negative if deducted): ", -100, 100)
                new_units = hospital.update_units(bg, delta)
                print(f">> Success: Updated {bg} units in {hospital.name} to {new_units}.")

        elif choice == 5:
            break


def handle_emergency_request(donors, hospitals, engine):
    """Sub-menu for creating emergency requests and running matching."""
    while True:
        print("\n----------------------------------------")
        print("      EMERGENCY BLOOD REQUEST MENU      ")
        print("----------------------------------------")
        print("1. Create Emergency Request & Run Matching Engine")
        print("2. View Blood Compatibility Reference Table")
        print("3. View Universal & Rare Blood Categories (FrozenSets)")
        print("4. Return to Main Menu")
        print("----------------------------------------")

        choice = read_integer("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            print("\n--- Create Emergency Blood Request ---")
            req_id = read_non_empty_string("Enter Request Reference ID (e.g., REQ-101): ").upper()
            patient_name = read_non_empty_string("Enter Patient Name: ")
            blood_group = read_blood_group("Enter Required Blood Group: ", VALID_BLOOD_GROUPS)
            city = read_non_empty_string("Enter Hospital/Patient City: ")
            units = read_integer("Enter Number of Units Needed (1-50): ", 1, 50)

            request = BloodRequest(req_id, patient_name, blood_group, city, units)
            # Execute matching
            engine.execute_emergency_matching(request, donors, hospitals)

        elif choice == 2:
            print("\n--- Blood Transfusion Compatibility Reference Table ---")
            print("Recipient Group | Compatible Donor Blood Groups")
            print("----------------|----------------------------------------------")
            for recipient, compatible_tuple in BLOOD_COMPATIBILITY.items():
                print(f"  {recipient:<14}| {', '.join(compatible_tuple)}")

        elif choice == 3:
            print("\n--- Special Blood Classifications (Using FrozenSets) ---")
            print(f"1. Universal Red Cell Donors    : {', '.join(UNIVERSAL_DONORS)}")
            print(f"   (Can safely donate to any recipient group)")
            print(f"2. Universal Red Cell Recipients: {', '.join(UNIVERSAL_RECIPIENTS)}")
            print(f"   (Can safely receive blood from any donor group)")
            print(f"3. Rh-Negative Blood Groups     : {', '.join(RH_NEGATIVE_GROUPS)}")
            print(f"   (Relatively rare blood groups requiring Rh-negative compatible blood)")

        elif choice == 4:
            break


def view_system_summary(donors, hospitals):
    """
    Displays a comprehensive summary of the system.
    Demonstrates:
    - Set operations to find unique cities
    - Array data structure aggregation across all blood types
    - Relational checks and formatted output
    """
    print("\n=======================================================")
    print("              SYSTEM STATUS & SUMMARY                  ")
    print("=======================================================")

    # Donor statistics
    total_donors = len(donors)
    available_donors = len(filter_available_donors(donors))

    # Set of unique donor cities
    donor_cities = get_unique_donor_cities(donors)

    # Hospital statistics
    total_hospitals = len(hospitals)
    hospital_cities = set()
    for h in hospitals:
        hospital_cities.add(h.city)

    # Combined cities using set union
    all_active_cities = donor_cities | hospital_cities

    print(f"Registered Volunteer Donors : {total_donors}")
    print(f"Currently Available Donors  : {available_donors}")
    print(f"Unique Donor Cities ({len(donor_cities)})     : {', '.join(sorted(list(donor_cities)))}")
    print("-------------------------------------------------------")
    print(f"Registered Partner Hospitals: {total_hospitals}")
    print(f"Hospital Network Cities ({len(hospital_cities)})  : {', '.join(sorted(list(hospital_cities)))}")
    print(f"Total Operational Cities ({len(all_active_cities)}) : {', '.join(sorted(list(all_active_cities)))}")
    print("-------------------------------------------------------")
    print("Total Blood Bank Inventory (Aggregated via Python Array):")

    total_all_units = 0
    for bg in VALID_BLOOD_GROUPS:
        # Use array aggregation utility
        units_arr, total_bg_units = aggregate_hospital_units_array(hospitals, bg)
        total_all_units += total_bg_units
        print(f"  * Blood Group {bg:<3} : {total_bg_units:>3} units in stock")

    print(f"\n>> TOTAL BLOOD UNITS IN NETWORK: {total_all_units} units")
    print("=======================================================\n")


def main():
    """Main program execution loop."""
    print("=======================================================")
    print(" COMMAND LINE EMERGENCY BLOOD DONOR & HOSPITAL SYSTEM  ")
    print("       Python Essentials Academic Project (B.Tech)     ")
    print("=======================================================")

    # Initialize in-memory dataset
    donors = get_initial_donors()
    hospitals = get_initial_hospitals()
    engine = BloodMatchingEngine(BLOOD_COMPATIBILITY)

    while True:
        print("\n========================================")
        print("               MAIN MENU                ")
        print("========================================")
        print("1. Donor Management")
        print("2. Hospital Management")
        print("3. Emergency Blood Request & Matching")
        print("4. View System Summary")
        print("5. Exit")
        print("========================================")

        choice = read_integer("Select an option (1-5): ", 1, 5)

        if choice == 1:
            handle_donor_management(donors)
        elif choice == 2:
            handle_hospital_management(hospitals)
        elif choice == 3:
            handle_emergency_request(donors, hospitals, engine)
        elif choice == 4:
            view_system_summary(donors, hospitals)
        elif choice == 5:
            print("\nThank you for using Emergency Blood Donor & Hospital Matching Engine.")
            print("System shutting down gracefully. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
