# Task 1: Algorithm Design

## 1. Domain Overview: Student Registration Number Search
Searching through academic records is a fundamental problem in institutional databases. Each student record is uniquely indexed by their **Registration Number** (e.g., `REG2024BCSE000042`). 

In this task, we design three distinct search algorithms to locate student records based on their registration number:
1. **Linear Search (Sequential Search)**
2. **Iterative Binary Search**
3. **Recursive Binary Search**

---

## 2. Approach 1: Linear Search (Sequential Search)

### 2.1 Design Description & Working Principle
Linear Search examines each student record sequentially starting from the first element (index `0`) and proceeds until either:
1. A record matching the query registration number is encountered (search successful).
2. The entire database of $n$ records has been inspected without a match (search unsuccessful).

- **Data Preconditions:** No ordering required. Works on unsorted, dynamically appended arrays.
- **Data Postconditions:** Returns the zero-based index of the matching student record, or `-1` if absent.

### 2.2 Pseudocode
```text
ALGORITHM LinearSearch(A[0..n-1], target_reg_no)
// Input:  Array A of n StudentRecords, and target_reg_no (string)
// Output: Index of record matching target_reg_no, or -1 if not found

FOR i ← 0 TO n - 1 DO
    IF A[i].reg_no == target_reg_no THEN
        RETURN i
    END IF
END FOR

RETURN -1
```

### 2.3 Flowchart
```mermaid
graph TD
    Start([Start]) --> Init[i = 0]
    Init --> CheckBound{i < n ?}
    CheckBound -- Yes --> Comp{A[i].reg_no == target?}
    Comp -- Match Found --> RetSuccess([Return i])
    Comp -- No Match --> Incr[i = i + 1]
    Incr --> CheckBound
    CheckBound -- No --> RetFail([Return -1])
```

---

## 3. Approach 2: Iterative Binary Search

### 3.1 Design Description & Working Principle
Binary Search utilizes the **Divide and Conquer** paradigm on a collection sorted by `reg_no`.
1. The search space is delimited by two pointers: `low` (initially `0`) and `high` (initially `n - 1`).
2. The midpoint is computed as: $\text{mid} = \text{low} + \lfloor (\text{high} - \text{low}) / 2 \rfloor$.
3. The registration number at `A[mid]` is compared against the target:
   - If `A[mid].reg_no == target`, the record is found at `mid`.
   - If `A[mid].reg_no < target`, because the array is sorted, the target must reside in the right sub-array. We prune the left half by setting `low = mid + 1`.
   - If `A[mid].reg_no > target`, the target must reside in the left sub-array. We prune the right half by setting `high = mid - 1`.
4. The process repeats until `low > high`, signaling that the record does not exist.

- **Data Preconditions:** Array must be monotonically sorted in ascending order of `reg_no`.
- **Data Postconditions:** Returns index of matching record, or `-1`.

### 3.2 Pseudocode
```text
ALGORITHM BinarySearchIterative(A[0..n-1], target_reg_no)
// Input:  Sorted array A of n StudentRecords, and target_reg_no (string)
// Output: Index of record matching target_reg_no, or -1 if not found

low ← 0
high ← n - 1

WHILE low <= high DO
    mid ← low + ⌊(high - low) / 2⌋
    
    IF A[mid].reg_no == target_reg_no THEN
        RETURN mid
    ELSE IF A[mid].reg_no < target_reg_no THEN
        low ← mid + 1
    ELSE
        high ← mid - 1
    END IF
END WHILE

RETURN -1
```

### 3.3 Flowchart
```mermaid
graph TD
    Start([Start]) --> Init[low = 0, high = n - 1]
    Init --> LoopCond{low <= high ?}
    LoopCond -- Yes --> CalcMid["mid = low + ⌊(high - low) / 2⌋"]
    CalcMid --> CheckEqual{A[mid].reg_no == target?}
    CheckEqual -- Yes --> RetSuccess([Return mid])
    CheckEqual -- No --> CheckLess{A[mid].reg_no < target?}
    CheckLess -- Yes --> SetRight[low = mid + 1]
    CheckLess -- No --> SetLeft[high = mid - 1]
    SetRight --> LoopCond
    SetLeft --> LoopCond
    LoopCond -- No --> RetFail([Return -1])
```

---

## 4. Approach 3: Recursive Binary Search

### 4.1 Design Description & Working Principle
Recursive Binary Search implements the Divide and Conquer strategy through recursive self-invocations:
1. **Base Case 1 (Empty Range):** If `low > high`, the element does not exist; return `-1`.
2. **Divide & Inspect:** Compute `mid = low + ⌊(high - low) / 2⌋`. If `A[mid].reg_no == target`, return `mid`.
3. **Conquer (Subproblem):**
   - If `target < A[mid].reg_no`: Recurse on left interval `[low, mid - 1]`.
   - Else: Recurse on right interval `[mid + 1, high]`.

- **Call Stack Behavior:** At each recursive step, activation records storing parameters (`arr`, `target`, `low`, `high`) are pushed onto the call stack, achieving stack depth proportional to $\lceil \log_2 n \rceil$.

### 4.2 Pseudocode
```text
ALGORITHM BinarySearchRecursiveHelper(A, target_reg_no, low, high)
// Input:  Sorted array A, target string, boundary indices low and high
// Output: Index of record or -1

IF low > high THEN
    RETURN -1
END IF

mid ← low + ⌊(high - low) / 2⌋

IF A[mid].reg_no == target_reg_no THEN
    RETURN mid
ELSE IF target_reg_no < A[mid].reg_no THEN
    RETURN BinarySearchRecursiveHelper(A, target_reg_no, low, mid - 1)
ELSE
    RETURN BinarySearchRecursiveHelper(A, target_reg_no, mid + 1, high)
END IF


ALGORITHM BinarySearchRecursive(A[0..n-1], target_reg_no)
// Wrapper function
RETURN BinarySearchRecursiveHelper(A, target_reg_no, 0, n - 1)
```

### 4.3 Flowchart
```mermaid
graph TD
    Start([Call Helper low, high]) --> BaseCheck{low > high ?}
    BaseCheck -- Yes --> RetFail([Return -1])
    BaseCheck -- No --> CalcMid["mid = low + ⌊(high - low) / 2⌋"]
    CalcMid --> MatchCheck{A[mid].reg_no == target?}
    MatchCheck -- Match --> RetMid([Return mid])
    MatchCheck -- No Match --> BranchCheck{target < A[mid].reg_no ?}
    BranchCheck -- Yes --> RecurLeft["Recurse(low, mid - 1)"]
    BranchCheck -- No --> RecurRight["Recurse(mid + 1, high)"]
    RecurLeft --> Done([Return Subproblem Result])
    RecurRight --> Done
```

---

## 5. Summary of Design Invariants
| Property | Linear Search | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Data Ordering** | Unordered / Any | Strictly Ascending Sorted | Strictly Ascending Sorted |
| **Strategy** | Brute-force Sequential | Divide and Conquer (Iterative) | Divide and Conquer (Recursive) |
| **Auxiliary Memory** | $O(1)$ | $O(1)$ | $O(\log n)$ (Call stack) |
| **Control Structure**| Simple loop | While loop with boundary adjustments | Tail-recursive function calls |
