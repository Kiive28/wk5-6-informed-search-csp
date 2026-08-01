# Sample 2 — Worked Example: Backtracking CSP on a Triangle Graph (step by step)

This example is fully solved so you can check your understanding of
backtracking search before you touch the assignment's map (which has more
regions). The full runnable code is in
`solution/csp_worked_example_solution.py`.

## The problem

Three regions, **A**, **B**, **C**, mutually adjacent (a triangle / K3
graph): every pair (A-B, B-C, A-C) must get **different** colours.

```
      A
     / \
    B---C
```

- Variables: `A, B, C`
- Variable order (simple "first unassigned" strategy): `A, B, C`
- Value order tried for each variable: as listed in the domain
- Constraint: for every edge `(X, Y)`, `colour(X) != colour(Y)`

## Part 1 — Try with only 2 colours: `[Red, Green]`

A triangle is **not 2-colourable** (this is a known graph theory fact — any
odd cycle needs at least 3 colours). Let's watch backtracking discover this.

| Step | Action | Assignment so far | Result |
|---|---|---|---|
| 1 | Assign A = Red | A=Red | consistent |
| 2 | Try B = Red | A=Red | conflicts with A (A-B) — skip |
| 3 | Try B = Green | A=Red, B=Green | consistent, assign |
| 4 | Try C = Red | A=Red, B=Green | conflicts with A (A-C) — skip |
| 5 | Try C = Green | A=Red, B=Green | conflicts with B (B-C) — skip |
| 6 | No values left for C | A=Red, B=Green | **fail — backtrack to B** |
| 7 | Undo B=Green. No more values for B | A=Red | **fail — backtrack to A** |
| 8 | Undo A=Red. Try A = Green | A=Green | consistent |
| 9 | Try B = Red | A=Green | consistent, assign |
| 10 | Try C = Red | A=Green, B=Red | conflicts with B (B-C) — skip |
| 11 | Try C = Green | A=Green, B=Red | conflicts with A (A-C) — skip |
| 12 | No values left for C | A=Green, B=Red | **fail — backtrack to B** |
| 13 | Undo B=Red. Try B = Green | A=Green | conflicts with A (A-B) — skip |
| 14 | No more values for B | A=Green | **fail — backtrack to A** |
| 15 | Undo A=Green. No more values for A | {} | **fail — backtrack to root** |
| 16 | No more variables to try | — | **CSP FAILURE: no solution with 2 colours** |

This matches the graph theory prediction — good confirmation your solver is
correct if it returns "no solution" here.

## Part 2 — Try with 3 colours: `[Red, Green, Blue]`

| Step | Action | Assignment so far | Result |
|---|---|---|---|
| 1 | Assign A = Red | A=Red | consistent |
| 2 | Try B = Red | A=Red | conflicts with A — skip |
| 3 | Try B = Green | A=Red, B=Green | consistent, assign |
| 4 | Try C = Red | A=Red, B=Green | conflicts with A — skip |
| 5 | Try C = Green | A=Red, B=Green | conflicts with B — skip |
| 6 | Try C = Blue | A=Red, B=Green, C=Blue | consistent, assign |
| 7 | All variables assigned | A=Red, B=Green, C=Blue | **SOLUTION FOUND** |

No backtracking was even needed this time — the extra colour gave enough
"room" to satisfy every constraint on the first attempt.

## What to check when you trace your own examples

1. Is every candidate value checked against **all** constraints involving
   already-assigned variables, not just the most recent one?
2. When a variable runs out of legal values, does the algorithm correctly
   **undo** the previous variable's assignment before trying its next
   value?
3. Does the algorithm terminate and report failure cleanly when no
   solution exists (rather than looping forever)?
4. Does a complete, constraint-satisfying assignment stop the search
   immediately?

## Run it yourself

```bash
python 02_CSP/solution/csp_worked_example_solution.py
```

This prints both traces (2-colour failure, 3-colour success) so you can
compare your own implementation's behaviour against it.
