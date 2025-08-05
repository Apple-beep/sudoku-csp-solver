import time
import utils
from csp import CSP

def select_unassigned_variable(csp, assignment):
    # Static Variable Ordering
    for variable in csp.variables:
        if variable not in assignment:
            return variable

def order_domain_values(csp, var, assignment):
    # Domains are assumed to be ordered 1-9
    return csp.domains[var]

def is_consistent(csp, var, value, assignment):
    # Ensure value does not conflict with assigned neighbors
    for neighbor in csp.constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def bruteforce_search(csp):
    # Entry point for recursive brute force search
    return recursive_search(csp, {})

def recursive_search(csp, assignment):
    # Count the search nodes
    csp.nodes_generated += 1

    if len(assignment) == len(csp.variables):
        grid = utils.assignment_to_grid(assignment)
        if utils.test_sudoku(grid):
            return assignment
        else:
            return None

    var = select_unassigned_variable(csp, assignment)

    for value in order_domain_values(csp, var, assignment):
        if is_consistent(csp, var, value, assignment):
            assignment[var] = value
            result = recursive_search(csp, assignment)
            if result:
                return result
            del assignment[var]

    return None

def solve_sudoku_brute_force(grid):
    variables = utils.enumerate_cells()
    domains = utils.get_domains(grid)
    constraints = utils.get_constraints()

    csp = CSP(variables, domains, constraints)
    start_time = time.time()
    solution = bruteforce_search(csp)
    end_time = time.time()
    search_time = end_time - start_time

    if solution:
        is_solved = True
        grid = utils.assignment_to_grid(solution)
    else:
        is_solved = False

    return (
        is_solved,
        grid,
        csp.nodes_generated,
        search_time,
    )
