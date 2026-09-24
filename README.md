# Command Line Emergency Blood Donor and Hospital Matching Engine

A first-year B.Tech Computer Science academic project built for the **Python Essentials** course. This simulation matches emergency patient blood requests with compatible volunteer donors and hospital blood banks using clean, rule-based logic and core Python fundamentals.

---

## 1. Project Overview
During medical emergencies, finding compatible blood quickly is critical. This project simulates an emergency blood matching coordination engine through a menu-driven command-line interface (CLI). The application allows emergency operators to:
1. Maintain records of volunteer donors.
2. Monitor blood unit stocks across partner hospitals.
3. Submit emergency blood requests.
4. Execute instant rule-based matching that evaluates medical blood group compatibility, donor availability, and hospital inventory reserves.

---

## 2. Problem Being Solved
Emergency blood procurement often encounters bottlenecks due to:
- Delays in verifying ABO and Rh factor compatibility.
- Difficulty in locating nearby donors who meet physical readiness criteria.
- Inability to quickly aggregate blood unit inventory across multiple hospitals to determine whether blood banks or volunteer donors are required.

This project solves these issues with a deterministic, lightweight matching engine that calculates compatibility, ranks potential donors, and computes real-time hospital stock coverage without needing heavy software frameworks or external databases.

---

## 3. Objectives
- Implement a fully functional, interactive CLI system using **only standard Python fundamentals**.
- Strictly adhere to the **Python Essentials** course syllabus without using unauthorized libraries, frameworks, or advanced language constructs.
- Demonstrate foundational programming principles: control flow, modular decomposition, beginner-level object-oriented programming (OOP), data structures (lists, tuples, sets, dictionaries, frozensets, arrays), and operators.
- Validate user inputs reliably using control loops and string checks without relying on exception handling (`try`/`except`).

---

## 4. Key Features
- **Module 1 — Donor Management:**
  - Register new volunteer donors with age, blood group, city, phone number, and availability status.
  - Search donors by exact blood group or active availability.
  - Update donor status (e.g., when a donor is temporarily unavailable).
  - Check donor readiness using bitwise status flags (age eligibility and availability).
- **Module 2 — Hospital Management:**
  - Register partner hospitals and initialize inventory for 8 standard blood groups (`A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`).
  - View real-time blood bank inventory per hospital.
  - Search hospitals situated in a specific city.
  - Update unit counts when units are donated or dispatched.
- **Module 3 — Emergency Blood Matching Engine:**
  - Input patient blood group, city, and required units.
  - Cross-reference medical compatibility lookup tables.
  - Filter and rank eligible donors by locality and compatibility score.
  - Match partner hospitals with available units and aggregate stock using Python's standard `array` data structure.
  - Compute immediate coverage percentage and identify blood deficits.
- **Module 4 — Network Status & Summary:**
  - View total registered donors, hospitals, and unique operational cities using set theory operations.
  - Display network-wide unit counts aggregated across all blood groups.

---

## 5. Technologies Used
- **Language:** Python 3 (3.8+)
- **Standard Library Modules:** `sys`, `os`, `array`
- **Dependencies:** None (Zero third-party packages; no `pip install` required)

---

## 6. Python Concepts Demonstrated

| Concept | Application in Codebase |
| :--- | :--- |
| **Variables & Types** | `int` (age, stock), `float` (percentage), `str` (IDs, names), `bool` (availability) |
| **`input()` & `print()`** | Interactive menu navigation, formatted reports, status messages |
| **Arithmetic Operators** | `+`, `-`, `*`, `/`, `//` used for stock adjustments, scoring, and fulfillment |
| **Assignment Operators** | `=`, `+=`, `-=` updating inventory and unit counters |
| **Relational Operators** | `==`, `!=`, `<`, `>`, `<=`, `>=` for age limits, stock checks, and menu choices |
| **Logical Operators** | `and`, `or`, `not` combining matching filters and validation checks |
| **Membership Operators** | `in`, `not in` checking compatibility tuples and valid blood group choices |
| **Identity Operators** | `is None`, `is not None` verifying search lookup results |
| **Bitwise Operators** | `&`, `|` for multi-flag donor emergency readiness validation |
| **`type()` Function** | Natural data type verification (`type(status) == bool`, `type(arr).__name__`) |
| **Type Conversion** | Explicit conversions: `int()`, `float()`, `str()`, `set()`, `tuple()`, `list()` |
| **Operator Precedence** | Priority score: `score = (city_bonus + type_bonus) - age_factor` |
| **Mixed Type Division** | Float division `(units * 100.0) / needed` vs Integer division `age // 10` |
| **Lists** | Dynamic collections of `Donor` and `Hospital` objects |
| **Tuples** | Immutable reference data: `VALID_BLOOD_GROUPS`, `STANDARD_CITIES` |
| **Sets** | Unique operational cities extraction (`set(d.city for d in donors)`) |
| **Dictionaries** | Blood compatibility table and hospital inventory maps |
| **Frozen Sets** | Immutable medical categories: `UNIVERSAL_DONORS`, `UNIVERSAL_RECIPIENTS` |
| **Control Flow** | `if`, `elif`, `else`, `for`, `while`, `break`, `continue` for menus and validation |
| **Functions & Modules** | Clean modular decomposition across 7 dedicated Python files |
| **Array Data Structure** | `array.array('i')` for aggregating numeric hospital blood units |
| **Object-Oriented Programming** | `Donor`, `Hospital`, `BloodRequest`, `BloodMatchingEngine` classes with constructors (`__init__`) and methods |

---

## 7. Project Structure

```text
blood_donor_matching/
│
├── main.py                     # Main CLI entry point and menu orchestration
├── donor.py                    # Donor class, registration, filtering, and availability
├── hospital.py                 # Hospital class, inventory management, and stock updates
├── blood_request.py            # BloodRequest class and request specifications
├── matching.py                 # BloodMatchingEngine and rule-based matching algorithms
├── data.py                     # Seed dataset, compatibility table, tuples, and frozensets
├── utils.py                    # Validation without try/except, bitwise flags, array utility
│
├── tests/
│   └── test_project.py         # Plain Python assert-based unit test suite (10 test cases)
│
├── docs/
│   ├── system_architecture.md  # Architectural diagrams (Mermaid & ASCII)
│   └── workflow.md             # Emergency request matching process workflow
│
├── statement.md                # Problem statement, scope, target users, and features
├── README.md                   # Complete project documentation and guide
└── REPORT_OUTLINE.md           # 15-section academic project report outline
```

---

## 8. Requirements & Setup
- Any standard Python 3.8+ installation.
- No pip packages or third-party tools are required.

To clone or set up the project:
1. Open your terminal / command prompt.
2. Navigate to the project directory:
   ```bash
   cd "C:\Users\Abhilasha Verma\.gemini\antigravity\scratch\blood_donor_matching"
   ```

---

## 9. How to Run
Execute the main program using standard Python:
```bash
python main.py
```

---

## 10. How to Test
The project includes a dedicated test script that executes 10 test cases using only native Python `assert` statements:
```bash
python tests/test_project.py
```

Expected output:
```text
========================================
 RUNNING ACADEMIC PROJECT TEST SUITE    
========================================
Testing Donor creation and attributes...
  -> Passed.
Testing Donor availability toggle...
  -> Passed.
Testing donor search and filtering...
  -> Passed.
Testing Hospital creation and inventory updates...
  -> Passed.
Testing identity operator (is None / is not None) in lookups...
  -> Passed.
Testing blood compatibility rules...
  -> Passed.
Testing bitwise donor readiness status flags...
  -> Passed.
Testing Python array data structure aggregation...
  -> Passed.
Testing FrozenSet universal classifications...
  -> Passed.
Testing matching engine donor ranking and calculations...
  -> Passed.
========================================
 ALL TESTS PASSED SUCCESSFULLY! (10/10) 
========================================
```

---

## 11. Example Workflow Walkthrough
1. **Launch Program:** Run `python main.py`.
2. **Review Initial Inventory:** Choose option `4` (View System Summary) to inspect pre-seeded donors, hospitals, and units.
3. **Submit Emergency Request:**
   - Choose option `3` (Emergency Blood Request & Matching).
   - Select option `1` (Create Emergency Request & Run Matching Engine).
   - Enter Reference ID: `REQ-101`
   - Patient Name: `Rahul Verma`
   - Required Blood Group: `A+`
   - Location: `Delhi`
   - Units Needed: `3`
4. **Inspect Matching Output:**
   - The engine lists all local and outstation hospitals carrying compatible blood units (`A+`, `A-`, `O+`, `O-`).
   - The engine ranks matching volunteer donors by locality bonus, compatibility bonus, and age factor.
   - The system displays the hospital stock coverage percentage and notes whether any remaining units need to be covered by volunteer donors.
5. **Update Stock / Donor Status:** Navigate to Donor or Hospital menus to update availability or stock after units are allocated.

---

## 12. Non-Functional Requirements
- **Usability:** Clean, human-readable terminal output with intuitive numbered menus and descriptive validation messages.
- **Reliability:** Built with robust loop-based input validation preventing crashes on invalid input without needing exception handling.
- **Maintainability:** Modular architecture separating entity classes, reference datasets, matching algorithms, and UI flows.
- **Performance & Efficiency:** Minimal memory footprint using in-memory data structures and rapid $O(1)$ dictionary lookups for compatibility checks.

---

## 13. Limitations
- **In-Memory Storage:** Data modifications persist only during the active runtime session and reset upon program termination (database and file persistence are outside syllabus bounds).
- **Console Interface:** Operates strictly via standard CLI text input and output.
- **Simplified Distance Metric:** Geographic proximity is evaluated based on matching city strings rather than GPS coordinates.

---

## 14. Future Enhancements
- File-based persistence (CSV or JSON) when file handling topics are introduced in subsequent coursework.
- Real-time GPS/pincode-based distance calculation using routing APIs.
- Automated SMS/Email alerts for matched volunteer donors.
- Web or graphical dashboard integration using beginner-friendly UI libraries.
