# Problem Statement and Scope

## Project Title
**Command Line Emergency Blood Donor and Hospital Matching Engine**

---

## 1. Problem Statement
In medical emergencies, securing compatible blood quickly is critical for patient survival. Traditional manual phone calls to potential donors and neighboring blood banks are slow, error-prone, and stressful during life-threatening crises. Patients and healthcare providers frequently face delays in identifying compatible donor groups and locating blood units in nearby hospitals.

There is a vital need for a lightweight, transparent, and rule-based emergency blood matching system that can instantly:
1. Identify biological blood compatibility between patients, volunteer donors, and hospital blood banks.
2. Filter available donors based on verified readiness (age eligibility, active availability, valid contact).
3. Evaluate local and regional hospital blood stocks to determine immediate unit coverage and identify deficits.
4. Prioritize candidate donors using proximity and biological compatibility rules.

---

## 2. Project Scope
The scope of this project is an academic command-line simulation developed for a first-year **Python Essentials** course. The project focuses strictly on demonstrating foundational programming concepts rather than enterprise software complexity.

### In Scope
- Management of volunteer donor profiles (registration, searching, availability updates).
- Management of hospital blood inventories across standard ABO/Rh blood groups.
- Rule-based blood matching engine based on standard medical transfusion compatibility.
- Bitwise donor readiness assessment using binary status flags.
- Aggregation of hospital stock counts using Python's native `array` data structure.
- Emergency fulfillment calculation (coverage percentage and shortage computation).
- Interactive, menu-driven command-line interface with loop-based input validation (no `try`/`except`).
- In-memory data persistence throughout runtime execution.
- Plain Python `assert`-based automated test suite.

### Out of Scope
- Graphical user interfaces (GUI) or web applications.
- External databases (SQL, NoSQL), ORM libraries, or flat-file parsers.
- Third-party packages or external pip dependencies.
- Machine learning or statistical matching algorithms.
- Telephony or SMS gateway integrations.

---

## 3. Target Users
1. **Hospital Emergency Room Coordinators:** Medical staff requiring rapid identification of compatible blood units from affiliated hospital blood banks or volunteer donors.
2. **Blood Bank Operators:** Technicians monitoring inventory levels and updating real-time unit availability.
3. **Emergency Helplines & Volunteer Coordinators:** Community organizers facilitating blood donation by identifying eligible, active donors in emergency zones.
4. **Academic Evaluators & First-Year Engineering Students:** Students and professors studying the direct application of core Python fundamentals to real-world problem domains.

---

## 4. High-Level Features
- **Donor Management Module:** Add donors, view active donor registries, filter by blood group, and update donor availability status.
- **Hospital Management Module:** Register hospitals, view multi-blood-group stock inventories, search by geographic location, and update stock counts.
- **Emergency Matching Engine:** Match patient requests with compatible blood groups, rank donors by locality and compatibility score, check hospital reserves, and compute deficit/coverage metrics.
- **System Overview & Summary:** High-level dashboard computing active operational cities using `set` unions and calculating network-wide blood units using standard integer `array`s.
