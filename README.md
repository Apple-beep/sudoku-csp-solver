🧩 Project Overview

This project implements an AI-based Sudoku Solver using three distinct techniques from Constraint Satisfaction Problem (CSP) theory:

* Brute Force Search – Tries every possible combination until it finds a solution. Simple but inefficient.

* CSP Backtracking – Uses recursive backtracking to fill cells while checking constraints, reducing invalid states early.

* CSP with Forward Checking + MRV – Enhances backtracking with:

* Forward Checking: Eliminates invalid future options after each assignment.

* MRV (Minimum Remaining Values): Selects the most constrained variable first, reducing the search space dramatically.

 
 # 🧩 Sudoku CSP Solver


This project implements a Sudoku solver in Python using three different strategies:
1. **Brute Force Search**
2. **CSP Backtracking**
3. **CSP with Forward-Checking and MRV Heuristics**

Developed for **CS480 - Artificial Intelligence** at Illinois Institute of Technology.

---

## 📁 Files Included

| File Name                      | Description |
|-------------------------------|-------------|
| `cs480_P02_A20501777.py`      | Main program file; accepts mode and filename as input |
| `brute_force.py`              | Brute force search solver |
| `csp_backtrack.py`            | Backtracking CSP solver |
| `csp_fc_mrv.py`               | CSP solver with forward checking and MRV |
| `utils.py`                    | Helper functions for grid parsing and display |
| `testcase1.csv` to `testcase8.csv` | Unsolved Sudoku puzzles |
| `*_solution.csv`              | Expected or generated solution files |

---

## ⚙️ How to Run

Run the solver from command line with:

```bash
python cs480_P02_A20501777.py MODE FILENAME
