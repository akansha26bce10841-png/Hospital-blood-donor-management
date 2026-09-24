"""
blood_request.py
Demonstrates:
- Classes and Objects
- Constructor (__init__)
- Attributes and Methods
- String formatting for display
"""

class BloodRequest:
    """
    Represents an emergency blood request submitted by a hospital or patient family.
    Uses simple attributes and straightforward methods without magic methods.
    """
    def __init__(self, request_id, patient_name, blood_group, city, units_needed):
        self.request_id = request_id
        self.patient_name = patient_name
        self.blood_group = blood_group
        self.city = city
        self.units_needed = units_needed

    def display_details(self):
        """Displays formatted details of the emergency request."""
        print("--------------------------------------------------")
        print(f" EMERGENCY REQUEST [{self.request_id}]")
        print(f" Patient Name : {self.patient_name}")
        print(f" Blood Group  : {self.blood_group}")
        print(f" City/Location: {self.city}")
        print(f" Units Needed : {self.units_needed}")
        print("--------------------------------------------------")
