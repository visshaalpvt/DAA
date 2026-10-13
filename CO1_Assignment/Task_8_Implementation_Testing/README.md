# Task 8: Implementation and Testing

## 1. Source Code Organization
All source code modules for this assignment are implemented in Python 3.11 and located inside the [`Source_Code`](Source_Code/) directory:

```
Task_8_Implementation_Testing/
├── Source_Code/
│   ├── student_database.py          # StudentRecord schema & synthetic database generator
│   ├── linear_search.py             # Iterative Linear Search with comparison tracking
│   ├── binary_search_iterative.py   # Iterative Binary Search implementation
│   ├── binary_search_recursive.py   # Recursive Binary Search with recurrence validation
│   ├── test_suite.py                # Comprehensive unittest test suite
│   └── benchmark.py                 # Multi-scale performance benchmarking harness
└── README.md
```

---

## 2. Implementation Highlights

### 2.1 Student Record Representation (`student_database.py`)
Each student record is encapsulated as an immutable dataclass:
```python
@dataclass
class StudentRecord:
    reg_no: str           # e.g., "REG2024BCSE000042" (Primary Search Key)
    name: str             # e.g., "Visshaal Natarajan"
    department: str       # e.g., "Computer Science and Engineering"
    cgpa: float           # e.g., 9.45
    year_of_study: int    # e.g., 3
```

### 2.2 Comparison Instrumentation
Every search function returns a tuple `(index, comparisons_count)`:
- If found: returns `(index, count)`
- If not found: returns `(-1, count)`
This enables exact, non-intrusive empirical measurement of basic operations during experimental validation.

---

## 3. Testing Methodology & Coverage

The test suite [`test_suite.py`](Source_Code/test_suite.py) employs Python's standard `unittest` framework to validate all three algorithms against rigorous edge cases:

1. **`test_first_element_search`:**
   - Validates lookup when target is at index 0 (Best case for Linear Search).
   - Confirms Linear Search performs exactly 1 comparison.
2. **`test_last_element_search`:**
   - Validates lookup when target is at index $n - 1$ (Worst case for Linear Search).
   - Confirms Linear Search performs exactly $n$ comparisons.
3. **`test_middle_element_search`:**
   - Validates lookup when target is at index $\lfloor n / 2 \rfloor$ (Best case for Binary Search).
   - Confirms Binary Search performs exactly 1 comparison.
4. **`test_non_existent_element`:**
   - Validates absent key handling (e.g. `REG9999NONEXISTENT`).
   - Ensures algorithms return `-1` gracefully without crashes or boundary exceptions.
5. **`test_single_element_list`:**
   - Boundary test on array of size $n = 1$ for both present and absent targets.
6. **`test_empty_list`:**
   - Boundary test on empty array ($n = 0$).
   - Ensures 0 comparisons and `-1` return.
7. **`test_parity_across_random_queries`:**
   - Runs 50 random queries across a 1,000-record dataset.
   - Asserts that all three algorithms return identical index results for every query.

---

## 4. Test Suite Execution Output

```bash
$ py test_suite.py -v
test_empty_list (test_suite.TestSearchAlgorithms.test_empty_list) ... ok
test_first_element_search (test_suite.TestSearchAlgorithms.test_first_element_search) ... ok
test_last_element_search (test_suite.TestSearchAlgorithms.test_last_element_search) ... ok
test_middle_element_search (test_suite.TestSearchAlgorithms.test_middle_element_search) ... ok
test_non_existent_element (test_suite.TestSearchAlgorithms.test_non_existent_element) ... ok
test_parity_across_random_queries (test_suite.TestSearchAlgorithms.test_parity_across_random_queries) ... ok
test_single_element_list (test_suite.TestSearchAlgorithms.test_single_element_list) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.012s

OK
```

All 7 test cases passed with 100% success rate, verifying algorithmic correctness, boundary safety, and parity.
