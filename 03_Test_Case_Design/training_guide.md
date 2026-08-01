# Training: Deriving 3 Test Cases, Step by Step

This walks through the *process* of choosing test cases using the mind-map
in `mindmap.md`, on a function that has nothing to do with A* or CSP
(`binary_search`), so you can copy the *method* without copying an answer.

## The function under test

```python
def binary_search(arr, target):
    """Return the index of `target` in sorted list `arr`, or -1 if absent."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Step 1: Understand the spec

- Input: a **sorted** list `arr`, and a `target` value.
- Output: the index of `target` if present, else `-1`.
- Implicit assumptions to interrogate: what if `arr` is empty? What if
  `target` isn't present? What if `arr` is large?

## Step 2: List candidate branches from the mind-map

Looking at `mindmap.md`, the branches that are plausible for this function:

- **Size**: trivial (empty list), small typical, large/stress.
- **Solvability**: solvable (target present), unsolvable (target absent).
- **Boundary**: target is the first or last element.

## Step 3: Choose 3 *different* branches (don't cluster)

| # | Chosen branch | Concrete case | Why this branch |
|---|---|---|---|
| 1 | Size → trivial | `arr = []`, `target = 5` | Tests the boundary where the loop never executes at all — a very common off-by-one source. |
| 2 | Solvability → solvable, Boundary → last element | `arr = [1,3,5,7,9]`, `target = 9` | Tests a normal case AND a boundary index (last element) together — checks `hi` handling. |
| 3 | Solvability → unsolvable | `arr = [1,3,5,7,9]`, `target = 4` | Tests that a value which *would* fit between two elements is correctly reported absent, not mistaken for a neighbour. |

Notice: I did **not** pick "target present in the middle" plus "target
present near the start" plus "target present near the end" — that would be
3 tests from the *same* branch (Solvability → solvable) and would miss
whether the function handles emptiness or absence at all.

## Step 4: Write the test cases with expected output stated *before* you run the code

```python
def test_case_1_empty_list():
    # Category: Size -> trivial input
    assert binary_search([], 5) == -1

def test_case_2_present_at_boundary():
    # Category: Solvability -> solvable, Boundary -> last element
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_case_3_absent_value():
    # Category: Solvability -> unsolvable
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
```

## Step 5: Run them and treat a failure as information, not noise

If `test_case_1` fails, that tells you something concrete: your `while`
condition or index math doesn't handle empty input. Fix the code, don't
weaken the test.

## Apply this exact process to your assignment

For **A*** (`01_Informed_Search_A_Star`) and **CSP**
(`02_CSP`), repeat steps 1–5:

1. Re-read what the function is supposed to guarantee (optimal path? valid
   colouring?).
2. Pick 3 branches from the mind-map that are *different* from each other.
3. State, in a comment, which branch each test covers and why.
4. Write the assertion(s) with the expected result decided in advance.
5. Run `pytest` and fix code (not tests) when something fails unexpectedly.

Your 3 test cases are graded partly on *coverage diversity* (see the rubric
in `../assignments/assignment_wk5_6.md`), so the branch-selection step is
not optional — it's the main skill being assessed here.
