"""
hospital.py
Demonstrates:
- Classes and Objects
- Constructor (__init__)
- Attributes and Methods
- Dictionary operations for blood inventory
- Set operations to find available blood groups
- Identity operator (is / is not None)
"""

class Hospital:
    """
    Represents a hospital with a blood inventory.
    Inventory is maintained using a standard Python dictionary mapping
    blood groups (str) to available unit counts (int).
    """
    def __init__(self, hospital_id, name, city, inventory, phone):
        self.hospital_id = hospital_id
        self.name = name
        self.city = city
        self.inventory = inventory  # e.g., {'A+': 5, 'B+': 3, 'O+': 8, ...}
        self.phone = phone

    def display_details(self):
        """Displays hospital basic information and stock counts."""
        print(f"[{self.hospital_id}] {self.name} | City: {self.city} | Emergency Phone: {self.phone}")
        # Format inventory items
        stock_items = []
        for bg, units in self.inventory.items():
            stock_items.append(f"{bg}: {units} units")
        stock_summary = ", ".join(stock_items) if stock_items else "No units in stock"
        print(f"   Inventory: {stock_summary}")

    def get_units(self, blood_group):
        """Returns the number of units available for a given blood group."""
        if blood_group in self.inventory:
            return self.inventory[blood_group]
        return 0

    def update_units(self, blood_group, count):
        """
        Updates unit count by adding count (can be positive or negative).
        Demonstrates assignment operators and comparison.
        """
        current_count = self.get_units(blood_group)
        new_count = current_count + count
        if new_count < 0:
            new_count = 0
        self.inventory[blood_group] = new_count
        return new_count

    def get_available_blood_groups(self):
        """
        Returns a set of blood groups that currently have at least 1 unit in stock.
        Demonstrates set data structure.
        """
        available_groups = set()
        for bg, count in self.inventory.items():
            if count > 0:
                available_groups.add(bg)
        return available_groups


def find_hospital_by_id(hospital_list, hospital_id):
    """
    Searches for a hospital by hospital_id.
    Returns the Hospital object if found, or None if not found.
    Demonstrates returning None for subsequent identity checks (is None / is not None).
    """
    for hospital in hospital_list:
        if hospital.hospital_id.upper() == hospital_id.upper():
            return hospital
    return None


def filter_hospitals_by_city(hospital_list, city):
    """
    Filters hospitals situated in a specified city.
    Demonstrates string comparison and list filtering.
    """
    matches = []
    for hospital in hospital_list:
        if hospital.city.lower() == city.lower():
            matches.append(hospital)
    return matches


def filter_hospitals_with_blood_group(hospital_list, blood_group):
    """
    Filters hospitals that have at least 1 unit of the requested blood group.
    Demonstrates dictionary lookup and relational operator (>).
    """
    matches = []
    for hospital in hospital_list:
        if hospital.get_units(blood_group) > 0:
            matches.append(hospital)
    return matches
