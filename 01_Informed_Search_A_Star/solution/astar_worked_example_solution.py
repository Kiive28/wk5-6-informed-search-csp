"""
Sample 1 -- fully worked A* solution for the 4x4 grid described in
../worked_example.md

This file is a REFERENCE only. It solves the small worked example, not the
assignment's grid. Use it to check your understanding of A* before you
write your own implementation in ../starter_code/astar_grid.py.

Run:
    python astar_worked_example_solution.py
"""
import heapq

# Grid layout matching worked_example.md
# '.' = free cell, '#' = wall, 'S' = start, 'G' = goal
GRID = [
    "S...",
    ".#..",
    ".#..",
    "...G",
]

ROWS = len(GRID)
COLS = len(GRID[0])


def find_cell(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] == symbol:
                return (r, c)
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(r, c):
    if not (0 <= r < ROWS and 0 <= c < COLS):
        return False
    return GRID[r][c] != "#"


def neighbours(node):
    r, c = node
    # 4-directional moves: up, down, left, right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if is_walkable(nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    # Manhattan distance -- admissible for 4-directional grid movement
    (r, c), (gr, gc) = node, goal
    return abs(r - gr) + abs(c - gc)


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(start, goal, verbose=True):
    # Priority queue entries: (f, -g, row, col)
    # -g breaks ties by preferring the LARGER g (closer to goal) when f is
    # equal; (row, col) breaks further ties deterministically.
    counter_step = 0
    open_heap = []
    g_score = {start: 0}
    f_start = heuristic(start, goal)
    heapq.heappush(open_heap, (f_start, -0, start[0], start[1], start))
    came_from = {}
    closed = set()
    in_open = {start}

    while open_heap:
        f, neg_g, _, _, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        in_open.discard(current)
        counter_step += 1
        g = g_score[current]
        h = heuristic(current, goal)
        if verbose:
            print(f"Step {counter_step}: pop {current}  g={g} h={h} f={f}")

        if current == goal:
            if verbose:
                print(f"Goal reached at {current} with cost {g}")
            return reconstruct_path(came_from, current), g

        closed.add(current)

        for nb in neighbours(current):
            if nb in closed:
                continue
            tentative_g = g + 1  # every move costs 1 on this grid
            if nb not in g_score or tentative_g < g_score[nb]:
                came_from[nb] = current
                g_score[nb] = tentative_g
                f_nb = tentative_g + heuristic(nb, goal)
                heapq.heappush(
                    open_heap, (f_nb, -tentative_g, nb[0], nb[1], nb)
                )
                in_open.add(nb)
                if verbose:
                    print(
                        f"    neighbour {nb}: g={tentative_g} "
                        f"h={heuristic(nb, goal)} f={f_nb} (added/updated)"
                    )

    return None, float("inf")  # no path found


if __name__ == "__main__":
    start = find_cell("S")
    goal = find_cell("G")
    print(f"Start: {start}, Goal: {goal}\n")

    path, cost = astar(start, goal, verbose=True)

    print()
    if path:
        print(f"Path found (cost={cost}):")
        print(" -> ".join(str(p) for p in path))
    else:
        print("No path exists.")
