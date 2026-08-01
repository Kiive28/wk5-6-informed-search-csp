"""
Sample 2 -- fully worked backtracking CSP solution for the triangle graph
described in ../worked_example.md

This file is a REFERENCE only. It solves the small worked example (3 mutually
adjacent regions), not the assignment's map. Use it to check your
understanding before you write your own implementation in
../starter_code/csp_map_coloring.py.

Run:
    python csp_worked_example_solution.py
"""

VARIABLES = ["A", "B", "C"]

# Triangle graph: every pair is adjacent (mutually constrained)
NEIGHBOURS = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
}


def is_consistent(assignment, var, value):
    """A value is consistent if no already-assigned neighbour shares it."""
    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False
    return True


def select_unassigned_variable(assignment):
    # Simple strategy: first variable (in VARIABLES order) not yet assigned.
    for var in VARIABLES:
        if var not in assignment:
            return var
    return None


def backtrack(assignment, domain, verbose, depth=0):
    if len(assignment) == len(VARIABLES):
        return dict(assignment)  # complete assignment found

    var = select_unassigned_variable(assignment)
    for value in domain:
        if verbose:
            print(f"{'  ' * depth}Try {var} = {value} ... ", end="")
        if is_consistent(assignment, var, value):
            if verbose:
                print("consistent, assign")
            assignment[var] = value
            result = backtrack(assignment, domain, verbose, depth + 1)
            if result is not None:
                return result
            if verbose:
                print(f"{'  ' * depth}Backtrack: undo {var} = {value}")
            del assignment[var]
        else:
            if verbose:
                print("conflict, skip")
    return None  # no value worked -> failure, backtrack further


def solve(domain, verbose=True):
    if verbose:
        print(f"--- Solving with domain {domain} ---")
    result = backtrack({}, domain, verbose)
    if verbose:
        if result:
            print(f"SOLUTION: {result}\n")
        else:
            print("FAILURE: no valid colouring exists with this domain.\n")
    return result


if __name__ == "__main__":
    print("Part 1: 2 colours (expected: failure -- a triangle needs 3)\n")
    solve(["Red", "Green"])

    print("Part 2: 3 colours (expected: success)\n")
    solve(["Red", "Green", "Blue"])
