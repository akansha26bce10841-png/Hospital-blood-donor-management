"""
data.py
Demonstrates:
- Tuples for fixed collections (blood groups, cities)
- Dictionaries for blood compatibility mapping
- Frozen sets for immutable blood categories (universal donors/recipients)
- Seed data initialization (lists of Donor and Hospital objects)
"""

from donor import Donor
from hospital import Hospital

# ====================================================================
# TUPLES (FIXED REFERENCE DATA)
# ====================================================================
VALID_BLOOD_GROUPS = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
STANDARD_CITIES = ('Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune')

# ====================================================================
# FROZEN SETS (IMMUTABLE MEDICAL CATEGORIES)
# ====================================================================
# O- negative can donate red blood cells to any recipient
UNIVERSAL_DONORS = frozenset({'O-'})

# AB+ positive can receive red blood cells from any donor
UNIVERSAL_RECIPIENTS = frozenset({'AB+'})

# Rare Rh-negative blood groups
RH_NEGATIVE_GROUPS = frozenset({'O-', 'A-', 'B-', 'AB-'})

# ====================================================================
# DICTIONARY (BLOOD COMPATIBILITY LOOKUP TABLE)
# Recipient Blood Group -> Tuple of Compatible Donor Blood Groups
# ====================================================================
BLOOD_COMPATIBILITY = {
    'A+': ('A+', 'A-', 'O+', 'O-'),
    'A-': ('A-', 'O-'),
    'B+': ('B+', 'B-', 'O+', 'O-'),
    'B-': ('B-', 'O-'),
    'AB+': ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'),
    'AB-': ('AB-', 'A-', 'B-', 'O-'),
    'O+': ('O+', 'O-'),
    'O-': ('O-',)
}

# ====================================================================
# SEED DATA FUNCTIONS
# ====================================================================
def get_initial_donors():
    """
    Returns a sample list of realistic fictional volunteer donors.
    Demonstrates creating objects and populating a list.
    """
    donors = [
        Donor("D101", "Aarav Sharma", 24, "O+", "Delhi", "9876543210", True),
        Donor("D102", "Priya Patel", 29, "A+", "Delhi", "9876543211", True),
        Donor("D103", "Rohan Mehta", 35, "B+", "Mumbai", "9876543212", True),
        Donor("D104", "Sneha Rao", 22, "O-", "Delhi", "9876543213", True),
        Donor("D105", "Karan Gupta", 31, "AB+", "Bangalore", "9876543214", False),
        Donor("D106", "Ananya Singh", 27, "A-", "Delhi", "9876543215", True),
        Donor("D107", "Vikram Verma", 42, "B-", "Chennai", "9876543216", True),
        Donor("D108", "Neha Deshmukh", 26, "O+", "Mumbai", "9876543217", True),
        Donor("D109", "Aditya Nair", 33, "AB-", "Bangalore", "9876543218", True),
        Donor("D110", "Pooja Joshi", 25, "O-", "Pune", "9876543219", True)
    ]
    return donors


def get_initial_hospitals():
    """
    Returns a sample list of realistic fictional hospitals with blood inventory.
    Demonstrates dictionaries nested inside class objects within a list.
    """
    hospitals = [
        Hospital("H201", "AIIMS Emergency Center", "Delhi",
                 {"A+": 6, "A-": 2, "B+": 5, "B-": 1, "AB+": 4, "AB-": 1, "O+": 8, "O-": 3},
                 "01126588500"),
        Hospital("H202", "Safdarjung Trauma Care", "Delhi",
                 {"A+": 3, "A-": 0, "B+": 4, "B-": 0, "AB+": 2, "AB-": 0, "O+": 5, "O-": 1},
                 "01126165060"),
        Hospital("H203", "Lilavati Hospital & Research", "Mumbai",
                 {"A+": 5, "A-": 1, "B+": 6, "B-": 2, "AB+": 3, "AB-": 1, "O+": 7, "O-": 2},
                 "02226751000"),
        Hospital("H204", "Fortis Memorial Blood Bank", "Bangalore",
                 {"A+": 4, "A-": 1, "B+": 3, "B-": 1, "AB+": 2, "AB-": 1, "O+": 4, "O-": 2},
                 "08066214444"),
        Hospital("H205", "Apollo Specialty Center", "Chennai",
                 {"A+": 7, "A-": 2, "B+": 5, "B-": 2, "AB+": 4, "AB-": 1, "O+": 9, "O-": 4},
                 "04428290200")
    ]
    return hospitals
