# Assignment Notes: A* and CSP

## 1. A* Heuristic Admissibility
For my A* implementation, I used the Manhattan distance heuristic. This heuristic is strictly admissible for this specific grid problem because movement is locked to 4 directions (up, down, left, right) with no diagonal movement allowed. Therefore, the calculated Manhattan distance will always be exactly equal to or less than the true path cost (if obstacles exist), meaning it never overestimates the cost to reach the goal. 

## 2. Test Case Coverage Diversity
For both the A* and CSP algorithms, I intentionally selected three distinct branches from the mind-map to ensure robust coverage: one typical/solvable case, one boundary/trivial case, and one strictly unsolvable case. I chose this specific spread because testing only "happy paths" (solvable cases) fails to verify if the algorithm handles edge cases (like `start == goal` or single-variable maps) and fails to prove that the loop terminates correctly when no solution exists. This spread guarantees the code is structurally sound across all extremes.