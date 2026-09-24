"""
utils.py
Demonstrates:
- Input handling and validation without try/except
- While loops, if/elif/else, break, continue
- String checks (isdigit(), strip(), upper())
- Relational and logical operators
- Membership operators (in, not in)
- Bitwise operators (&, |) for emergency readiness status flags
- Array data structure (standard library array.array) for numerical stock aggregation
- Type conversion (int(), float(), str())
- type() function checks
"""

import array

# ====================================================================
# BITWISE CONSTANTS FOR DONOR EMERGENCY READINESS
# ====================================================================
# In emergency matching, donors can have multiple operational status flags.
# We represent these status flags using standard binary powers of 2.
FLAG_AGE_VALID = 1      # Bit 0 (0001 in binary): Age is between 18 and 65
FLAG_AVAILABLE = 2      # Bit 1 (0010 in binary): Donor marked as currently available
FLAG_PHONE_VALID = 4    # Bit 2 (0100 in binary): Contact phone number is 10 digits

def compute_donor_status_flags(donor):
    """
    Computes a bitmask representing the readiness status of a donor.
    Demonstrates bitwise OR (|) to combine flags.
    """
    flags = 0
    # Check age requirement (18 to 65 years)
    if donor.age >= 18 and donor.age <= 65:
        flags = flags | FLAG_AGE_VALID

    # Check availability status
    if donor.is_available:
        flags = flags | FLAG_AVAILABLE

    # Check phone number validity
    if len(donor.phone) == 10 and donor.phone.isdigit():
        flags = flags | FLAG_PHONE_VALID

    return flags


def is_donor_ready_for_emergency(donor):
    """
    Checks if a donor is ready for emergency matching.
    Both age validity (1) and availability (2) are strictly required.
    Demonstrates bitwise AND (&) and comparison (==).
    """
    flags = compute_donor_status_flags(donor)
    required_flags = FLAG_AGE_VALID | FLAG_AVAILABLE
    # Bitwise test: does flags contain all required bits?
    return (flags & required_flags) == required_flags


# ====================================================================
# ARRAY DATA STRUCTURE UTILITY
# ====================================================================
def aggregate_hospital_units_array(hospital_list, blood_group):
    """
    Aggregates unit counts across a list of hospitals using Python's standard array.
    Demonstrates:
    - Standard array data structure (typecode 'i' for signed integer)
    - Array creation, append, and iteration
    - Arithmetic accumulation
    """
    # Create an integer array for unit counts
    units_array = array.array('i')

    for hospital in hospital_list:
        units = hospital.get_units(blood_group)
        # Using type() function to verify integer unit count
        if type(units) == int:
            units_array.append(units)
        else:
            units_array.append(int(units))

    # Calculate total units using a simple for loop
    total_units = 0
    for count in units_array:
        total_units += count

    return units_array, total_units


# ====================================================================
# INPUT VALIDATION FUNCTIONS (STRICTLY NO TRY/EXCEPT)
# ====================================================================
def read_non_empty_string(prompt):
    """
    Reads a non-blank string from the terminal.
    Uses while loop and string strip.
    """
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print(">> Error: Field cannot be empty. Please enter a value.")


def read_integer(prompt, min_val=None, max_val=None):
    """
    Reads an integer from user input without using try/except.
    Validates digits using str.isdigit() and applies range checks.
    """
    while True:
        raw_input = input(prompt).strip()
        if raw_input.isdigit():
            val = int(raw_input)
            if min_val is not None and val < min_val:
                print(f">> Error: Value cannot be less than {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f">> Error: Value cannot be greater than {max_val}.")
                continue
            return val
        else:
            print(">> Error: Invalid entry. Please enter numbers (digits) only.")


def read_blood_group(prompt, valid_groups):
    """
    Reads and validates a blood group string.
    Demonstrates membership operator 'in'.
    """
    while True:
        bg = input(prompt).strip().upper()
        if bg in valid_groups:
            return bg
        print(f">> Error: Invalid blood group '{bg}'. Allowed groups are: {', '.join(valid_groups)}")


def read_phone(prompt):
    """
    Reads a valid 10-digit phone number using string checks.
    """
    while True:
        phone = input(prompt).strip()
        if len(phone) == 10 and phone.isdigit():
            return phone
        print(">> Error: Please enter a valid 10-digit numeric phone number.")


def read_yes_no(prompt):
    """
    Reads a boolean choice (Yes/No) from the user.
    """
    while True:
        ans = input(prompt).strip().lower()
        if ans in ('yes', 'y', 'true', '1'):
            return True
        elif ans in ('no', 'n', 'false', '0'):
            return False
        print(">> Error: Please enter 'yes' (or 'y') or 'no' (or 'n').")
