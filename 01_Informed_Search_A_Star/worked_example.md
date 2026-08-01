# Sample 1 — Worked Example: A* on a 4×4 Grid (step by step)

This example is fully solved so you can check your own understanding of the
algorithm before you touch the assignment's grid (which is different and
larger). The full runnable code is in `solution/astar_worked_example_solution.py`.

## The problem

```
S  .  .  .
.  #  .  .
.  #  .  .
.  .  .  G
```

- Grid is 4×4, rows/cols indexed 0–3, `(row, col)`.
- Start `S = (0,0)`, Goal `G = (3,3)`.
- `#` = wall (impassable) at `(1,1)` and `(2,1)`.
- Movement: 4-directional (up/down/left/right), each step costs 1.
- Heuristic: **Manhattan distance** `h(r,c) = |r-3| + |c-3|`.
- Tie-break rule when two nodes have equal `f`: prefer the one with the
  **larger `g`** (closer to the goal); if still tied, prefer the smaller
  row then smaller column. (Any consistent rule is fine — document yours.)

Precomputed `h` for cells we'll visit:

| Cell | (0,0) | (0,1) | (0,2) | (0,3) | (1,0) | (1,2) | (1,3) | (2,2) | (2,3) | (3,3) |
|---|---|---|---|---|---|---|---|---|---|---|
| h  | 6 | 5 | 4 | 3 | 5 | 3 | 2 | 2 | 1 | 0 |

## Step-by-step trace

| # | Node popped (g, h, f) | Neighbours generated (g, h, f) | OPEN after this step | CLOSED |
|---|---|---|---|---|
| 1 | (0,0) → g0,h6,**f6** | (0,1)→1,5,6 · (1,0)→1,5,6 | (0,1)f6, (1,0)f6 | {(0,0)} |
| 2 | (0,1) → g1,h5,**f6** | (0,2)→2,4,6 · [(1,1) is a wall, skipped] | (1,0)f6, (0,2)f6 | +(0,1) |
| 3 | (0,2) → g2,h4,**f6** (tie-break: g2 > g1) | (0,3)→3,3,6 · (1,2)→3,3,6 | (1,0)f6, (0,3)f6, (1,2)f6 | +(0,2) |
| 4 | (0,3) → g3,h3,**f6** | (1,3)→4,2,6 | (1,0)f6, (1,2)f6, (1,3)f6 | +(0,3) |
| 5 | (1,3) → g4,h2,**f6** | (2,3)→5,1,6 · [(1,2) revisited: 4+1=5, not better than existing g3, skip] | (1,0)f6, (1,2)f6, (2,3)f6 | +(1,3) |
| 6 | (2,3) → g5,h1,**f6** | **(3,3)→6,0,6 [GOAL]** · (2,2)→6,2,8 | (1,0)f6, (1,2)f6, (3,3)f6, (2,2)f8 | +(2,3) |
| 7 | (3,3) → g6,h0,**f6** → **this is the goal, stop** | — | — | +(3,3) |

Note: `(1,0)` (f6, g1) and `(1,2)` (f6, g3) never get expanded — they stay
in OPEN and are simply discarded once the goal is found. This is expected;
A* doesn't need to explore the whole graph.

## Path reconstruction

Walking backwards from the goal via `came_from`:

```
(3,3) ← (2,3) ← (1,3) ← (0,3) ← (0,2) ← (0,1) ← (0,0)
```

Reversed, the path is:

```
(0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3) → (3,3)
```

**Total cost = 6**, which exactly matches the Manhattan-distance lower bound
`h(0,0) = 6` — confirming this path is optimal (no shorter path exists,
even with the walls in the way).

## What to check when you trace your own examples

1. Does every popped node have the smallest `f` in OPEN at that moment?
2. Is a node ever re-expanded after being placed in CLOSED? (It shouldn't
   be, with a consistent heuristic.)
3. When a cheaper `g` is found for a node already in OPEN, is it updated?
4. Does the algorithm stop **as soon as the goal is popped from OPEN**
   (not merely when it's first generated as a neighbour)?

## Run it yourself

```bash
python 01_Informed_Search_A_Star/solution/astar_worked_example_solution.py
```

This prints the same open/closed progression and final path shown above,
so you can compare your own implementation's behaviour against it.
