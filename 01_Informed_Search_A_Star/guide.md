# Guide: Heuristic (Informed) Search and A*

## 1. Why "informed" search?

Uninformed methods (BFS, DFS, Uniform-Cost Search) explore the search space
blindly — they don't know which direction is more promising. **Informed
search** uses problem-specific knowledge, a **heuristic function h(n)**, to
estimate how close a state `n` is to the goal, and uses that estimate to
guide exploration toward the goal faster.

| | Uninformed (e.g. BFS/UCS) | Informed (e.g. A*) |
|---|---|---|
| Knowledge used | Only the graph structure | Graph + a heuristic estimate |
| Exploration | Expands in all directions equally | Prioritizes nodes closer to the goal |
| Efficiency | Can explore many irrelevant states | Usually explores far fewer states |

## 2. The heuristic function h(n)

`h(n)` = an estimate of the cost from state `n` to the nearest goal.
It must be:

- **Cheap to compute** — otherwise you gain nothing over blind search.
- **Admissible** — never *overestimates* the true remaining cost
  (`h(n) ≤ true cost(n → goal)` for every n). Admissibility is what
  guarantees A* finds the *optimal* (lowest-cost) solution.
- **Consistent (monotonic)** — for every neighbour `n'` of `n`:
  `h(n) ≤ cost(n, n') + h(n')`. Consistency implies admissibility and lets
  A* avoid re-expanding nodes.

Common heuristics for grid pathfinding (4-directional movement):
- **Manhattan distance**: `|x1-x2| + |y1-y2|` — admissible when you can only
  move up/down/left/right.
- **Euclidean distance**: straight-line distance — admissible, but a weaker
  (less informative) estimate than Manhattan for grid movement.

If a heuristic overestimates, A* can still terminate, but it is no longer
guaranteed to return the optimal path.

## 3. Greedy Best-First Search vs A*

- **Greedy Best-First Search** expands the node with the smallest `h(n)`
  only. Fast, but can be led down a bad path because it ignores the cost
  already paid to get there.
- **A\*** expands the node with the smallest `f(n) = g(n) + h(n)`, where
  `g(n)` is the actual cost from the start to `n`. This balances "cost so
  far" against "estimated cost to go", giving both efficiency and (with an
  admissible heuristic) optimality.

## 4. The A* algorithm

```
OPEN  = priority queue ordered by f(n), initially containing the start node
CLOSED = empty set (nodes already fully expanded)
g(start) = 0
f(start) = h(start)

while OPEN is not empty:
    n = node in OPEN with smallest f(n)
    if n is the goal:
        return reconstruct_path(n)
    remove n from OPEN, add n to CLOSED

    for each neighbour n' of n:
        if n' in CLOSED: skip
        tentative_g = g(n) + cost(n, n')
        if n' not in OPEN OR tentative_g < g(n'):
            came_from[n'] = n
            g(n') = tentative_g
            f(n') = g(n') + h(n')
            add/update n' in OPEN

return failure   # no path exists
```

Key implementation details:
- Use a **min-heap / priority queue** (Python: `heapq`) keyed on `f(n)`, so
  the cheapest-looking node is always expanded next.
- Keep a `came_from` dictionary so you can reconstruct the path by walking
  backwards from the goal once it's found.
- Tie-breaking (same `f` value): a common approach is to prefer the node
  with the larger `g(n)` (closer to the goal), which tends to reduce the
  number of nodes expanded. Any consistent tie-break rule is acceptable as
  long as it's documented.

## 5. Step-by-step method for solving *any* A* problem

1. **Define the state representation.** What does one node in the search
   space look like? (e.g. `(row, col)` on a grid; a full board configuration
   for a puzzle.)
2. **Define the successor function.** Given a state, what are the valid
   next states, and what does each transition cost?
3. **Define the goal test.** How do you know you've reached the goal?
4. **Choose and justify a heuristic h(n).** Confirm it is admissible for
   your problem (explain briefly why, in your submission).
5. **Implement the A* loop** using the pseudocode above with a priority
   queue.
6. **Trace it by hand on a tiny example first** (see `worked_example.md`)
   before trusting your code on a bigger input.
7. **Test it**: does it find a path when one exists, correctly report
   "no path" when one doesn't, and return the lowest-cost path (not just
   *a* path)?

## 6. Common mistakes

- Using a heuristic that overestimates (breaks optimality guarantee).
- Forgetting to update `g(n)` when a *cheaper* path to an already-seen node
  is found later.
- Not reconstructing the path (only returning the cost).
- Off-by-one errors in grid boundaries, or not checking for walls/obstacles.
- Infinite loops from not tracking visited/closed nodes correctly.

## Further reading

See `../resources/reading_links.md` for external references on informed
search, heuristics, and A*.
