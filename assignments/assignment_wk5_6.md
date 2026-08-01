# Assignment — Weeks 5 & 6: A* Search and CSP

**Dates covered:** Tue 4 Aug – Thu 13 Aug 2026 (Week 5 & 6 class slots)
**Final submission deadline:** Thursday 13 August 2026, end of class
*(Lecturer: adjust these dates if your actual calendar differs — search
for "Aug 2026" in this file to find both date mentions.)*

This is a self-directed assignment. There is no live lecture support for
these two weeks — everything you need is in this repo. Use your Tue/Thu
class slots as protected working time; a TA may be present for logistics,
but the technical guidance is in `01_Informed_Search_A_Star/` and
`02_CSP/`.

## Learning outcomes

By completing this assignment you should be able to:

1. Explain the difference between informed and uninformed search.
2. Implement A* search correctly, including an admissible heuristic.
3. Model a problem as a CSP (variables, domains, constraints).
4. Implement backtracking search for a CSP.
5. Design test cases that give meaningfully different coverage of your
   code's behaviour, not just repeated happy-path checks.

## Part 1 — A* Grid Pathfinding (Week 5)

**File:** `01_Informed_Search_A_Star/starter_code/astar_grid.py`

1. Read `01_Informed_Search_A_Star/guide.md`.
2. Work through `01_Informed_Search_A_Star/worked_example.md` by hand —
   trace it on paper before you code. Compare against
   `solution/astar_worked_example_solution.py` if you want to check your
   trace.
3. Implement, in `starter_code/astar_grid.py`:
   - `neighbours(grid, node)`
   - `heuristic(node, goal)` (Manhattan distance)
   - `astar(grid, start, goal)`
4. Your solver must run correctly on `ASSIGNMENT_GRID` (already in the
   file) **and** on any other valid grid — don't hard-code anything
   specific to that one grid.
5. In `starter_code/test_astar_grid.py`, write your **3 required test
   cases** (`test_case_1`, `test_case_2`, `test_case_3`), following the
   method in `03_Test_Case_Design/training_guide.md`. Each test needs a
   one-line comment stating which mind-map category it covers.

**Optional bonus (not required for full marks):** add diagonal movement as
a configurable option, with a correctly adjusted (still admissible)
heuristic.

## Part 2 — CSP Map Colouring (Week 6)

**File:** `02_CSP/starter_code/csp_map_coloring.py`

1. Read `02_CSP/guide.md`.
2. Work through `02_CSP/worked_example.md` by hand — trace both the
   2-colour failure and the 3-colour success. Compare against
   `solution/csp_worked_example_solution.py` if you want to check your
   trace.
3. Implement, in `starter_code/csp_map_coloring.py`:
   - `is_consistent(assignment, var, value)`
   - `select_unassigned_variable(assignment)`
   - `backtracking_search(variables, domain)`
4. Your solver must correctly solve the Australia map problem already
   defined in the file (`VARIABLES`, `NEIGHBOURS`, `DOMAIN`).
5. In `starter_code/test_csp_map_coloring.py`, write your **3 required
   test cases**, following the same method as Part 1. Each test needs a
   one-line comment stating which mind-map category it covers.

**Optional bonus (not required for full marks):** implement forward
checking and show (in a comment or short note) how many fewer nodes get
explored compared to plain backtracking on the same problem.

## Deliverables checklist

- [ ] `astar_grid.py` — all TODOs implemented, runs without errors
- [ ] `test_astar_grid.py` — 3 test cases implemented, all passing, each
      labelled with its mind-map category
- [ ] `csp_map_coloring.py` — all TODOs implemented, runs without errors
- [ ] `test_csp_map_coloring.py` — 3 test cases implemented, all passing,
      each labelled with its mind-map category
- [ ] A short `NOTES.md` (create this yourself, in your own copy of
      `Wk5_6/`) with:
      - 2–3 sentences confirming your heuristic is admissible and why
      - 2–3 sentences naming which mind-map branches your 6 test cases
        (3 + 3) cover in total, and why you picked that spread

## How your work will be assessed (rubric)

| Criterion | Weight |
|---|---|
| A* correctness (finds optimal path; correctly reports no-path) | 25% |
| CSP correctness (finds valid colouring; correctly reports failure) | 25% |
| Test case coverage diversity (not 6 variations of one category) | 25% |
| Code clarity (docstrings kept, sensible variable names, no leftover `NotImplementedError`) | 15% |
| `NOTES.md` reasoning (admissibility explanation, coverage explanation) | 10% |

## Submission instructions

1. Make sure all tests pass locally:
   ```bash
   pytest 01_Informed_Search_A_Star/starter_code/ -v
   pytest 02_CSP/starter_code/ -v
   ```
2. Commit your work on your branch `wk5-6-<your-student-id>`.
3. Push your branch to your fork.
4. Open a Pull Request from your fork into the original class repo.
5. Paste your PR link into the class submission form/forum before the
   deadline above. GitHub timestamps your commits automatically — commits
   after the deadline will be marked late per your course's late policy.

## If you get stuck

1. Re-read the relevant `guide.md` and `worked_example.md`.
2. Check `../resources/reading_links.md`.
3. Ask in the class forum/channel — classmates and the TA can help with
   concepts; they should not write your code for you.
