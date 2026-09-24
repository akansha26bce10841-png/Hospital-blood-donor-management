"""
donor.py
Demonstrates:
- Classes and Objects
- Constructor (__init__)
- Attributes and Methods
- List processing and filtering
- Identity operator (is / is not None)
- type() function checking
"""

class Donor:
    """
    Represents an individual volunteer blood donor.
    Uses beginner-friendly attributes and straightforward methods.
    """
    def __init__(self, donor_id, name, age, blood_group, city, phone, is_available=True):
        self.donor_id = donor_id
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.city = city
        self.phone = phone
        self.is_available = is_available

    def display_details(self):
        """Prints donor details in a clean, human-readable format."""
        status_str = "Available" if self.is_available else "Unavailable"
        print(f"[{self.donor_id}] {self.name} | Age: {self.age} | Blood: {self.blood_group} | City: {self.city} | Phone: {self.phone} | Status: {status_str}")

    def set_availability(self, status):
        """Updates the availability status of the donor."""
        # Using type() function to verify boolean parameter
        if type(status) == bool:
            self.is_available = status
        else:
            self.is_available = bool(status)


def find_donor_by_id(donor_list, donor_id):
    """
    Searches for a donor by donor_id.
    Returns the Donor object if found, or None if not found.
    Demonstrates returning None for subsequent identity checks (is None / is not None).
    """
    for donor in donor_list:
        if donor.donor_id.upper() == donor_id.upper():
            return donor
    return None


def filter_donors_by_blood_group(donor_list, blood_group):
    """
    Filters donors by exact blood group match.
    Demonstrates list accumulation and comparison operator.
    """
    matches = []
    for donor in donor_list:
        if donor.blood_group.upper() == blood_group.upper():
            matches.append(donor)
    return matches


def filter_available_donors(donor_list):
    """
    Filters donors whose is_available attribute is True.
    Demonstrates boolean conditions and list filtering.
    """
    available = []
    for donor in donor_list:
        if donor.is_available:
            available.append(donor)
    return available


def get_unique_donor_cities(donor_list):
    """
    Extracts all unique cities where donors reside.
    Demonstrates the set data structure and set.add().
    """
    cities = set()
    for donor in donor_list:
        cities.add(donor.city)
    return cities
