# Guide: Constraint Satisfaction Problems (CSP)

## 1. What is a CSP?

A Constraint Satisfaction Problem is defined by three things:

- **Variables**: `X = {X1, X2, ..., Xn}` — the things you need to assign
  values to (e.g. regions on a map, cells in a Sudoku grid, exam slots).
- **Domains**: `D = {D1, D2, ..., Dn}` — the set of possible values each
  variable can take (e.g. a list of colours, numbers 1–9).
- **Constraints**: `C` — rules restricting which combinations of values are
  allowed (e.g. "adjacent regions must have different colours").

A **solution** is a complete assignment of a value to every variable such
that every constraint is satisfied.

## 2. Backtracking search

The standard exact algorithm for solving CSPs is depth-first search with
backtracking:

```
function BACKTRACKING-SEARCH(csp):
    return BACKTRACK({}, csp)

function BACKTRACK(assignment, csp):
    if assignment is complete:
        return assignment
    var = SELECT-UNASSIGNED-VARIABLE(csp, assignment)
    for value in ORDER-DOMAIN-VALUES(var, assignment, csp):
        if value is CONSISTENT with assignment (given constraints):
            add {var = value} to assignment
            result = BACKTRACK(assignment, csp)
            if result != failure:
                return result
            remove {var = value} from assignment   # <-- the "backtrack"
    return failure
```

Plain English: pick an unassigned variable, try a value that doesn't
conflict with what's already assigned, recurse. If every value for this
variable leads to failure further down, undo (backtrack) and try a
different value for the *previous* variable.

## 3. Making backtracking efficient

Plain backtracking works but can be slow. Two standard improvements:

- **Forward checking**: whenever you assign a value to a variable,
  immediately remove inconsistent values from the domains of its
  *unassigned neighbours*. If any neighbour's domain becomes empty, you
  know immediately (without recursing further) that this branch fails.
- **Variable/value ordering heuristics** (optional bonus, not required for
  the base assignment):
  - **MRV (Minimum Remaining Values)**: choose the variable with the
    fewest legal values left — fail fast.
  - **Degree heuristic**: among ties, choose the variable involved in the
    most constraints with other unassigned variables.
  - **LCV (Least Constraining Value)**: try the value that rules out the
    fewest choices for neighbouring variables first.

For this assignment, a correct **plain backtracking** solver is the
baseline requirement. Forward checking is a bonus extension — see
`assignments/assignment_wk5_6.md`.

## 4. Step-by-step method for solving *any* CSP

1. **Identify the variables.** What are the "slots" that need a value?
2. **Identify the domain of each variable.** What values could each slot
   take, ignoring constraints for now?
3. **Identify the constraints.** Write them as pairs/rules, e.g. an
   adjacency list (`region A conflicts with region B`) or arithmetic rules.
4. **Represent this in code**: variables as a list, domains as a
   dict `{variable: [values]}`, constraints as an adjacency structure or a
   function `conflicts(var1, val1, var2, val2) -> bool`.
5. **Implement `is_consistent`**: given a partial assignment and a
   candidate `(variable, value)`, check it against every constraint
   involving already-assigned variables.
6. **Implement `backtracking_search`** using the pseudocode above.
7. **Trace it by hand on a tiny example first** (see `worked_example.md`).
8. **Test it**: does it find a valid solution when one exists? Does it
   correctly report failure when the problem is over-constrained (no
   solution exists, e.g. too few colours for a densely connected map)?

## 5. Common mistakes

- Checking a new assignment only against *some* constraints instead of all
  relevant ones.
- Forgetting to undo (`remove {var = value}`) when backtracking, causing
  stale assignments to leak into later attempts.
- Not handling the "no solution exists" case — your function should return
  `None`/`failure`, not crash or loop forever.
- Confusing "domain" (candidate values before constraints) with "consistent
  values" (what's still legal given the current partial assignment).

## Further reading

See `../resources/reading_links.md` for external references on CSPs,
backtracking search, and constraint propagation.
