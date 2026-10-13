# Design and Analysis of Algorithms (DAA) — Course Outcome 1 (CO1)
## Comprehensive Technical Report: Searching Student Registration Numbers

**Course:** Design and Analysis of Algorithms (DAA)  
**Component:** Course Outcome 1 (CO1) Assignment  
**Problem Domain:** Algorithmic Design, Mathematical Complexity Analysis, and Empirical Benchmarking of Search Algorithms for Student Registration Numbers  
**Author:** Visshaal Natarajan  
**Repository:** [github.com/visshaalpvt/DAA](https://github.com/visshaalpvt/DAA)  

---

## Abstract
This report presents an exhaustive theoretical and empirical evaluation of searching algorithms applied to institutional student databases. Three core algorithms—**Linear Search**, **Iterative Binary Search**, and **Recursive Binary Search**—are formulated, implemented, and mathematically analyzed. Mathematical derivations are established for operation counts, best/average/worst-case behaviors, and asymptotic classifications ($O$, $\Omega$, $\Theta$). For the recursive formulation, a recurrence relation $T(n) = T(n/2) + c$ is formulated and solved via three distinct methodologies: the Substitution (Iteration) method, the Master Theorem, and the Recursion Tree method. Rigorous benchmarking is executed across dataset scales ranging from $N = 100$ to $N = 1,000,000$ student records using high-resolution performance counters. The empirical results match theoretical predictions with 100% precision in operation counts and confirm ratio convergence. Finally, the **Day-4 Design Challenge** is solved, presenting an evidence-based production architecture capable of servicing 50,000 search queries per hour over a 1,000,000-record database with nightly batch updates, utilizing Iterative Binary Search and an atomic Read-Copy-Update (RCU) double-buffering scheme with negligible CPU utilization ($< 0.03\%$).

---

## 1. Introduction & Problem Domain
Educational institutions maintain large-scale databases storing hundreds of thousands of student records. The primary access key is the **Student Registration Number** (e.g., `REG2024BCSE000042`), formatted as:
```text
REG<YEAR><DEPARTMENT_CODE><SEQUENCE_NUMBER>
```
Every institutional query (grade lookups, course registrations, fee status verifications, portal logins) initiates a search query on this primary registration key. The algorithmic efficiency of the underlying search strategy dictates database latency, server throughput, and overall system scalability.

---

## 2. Algorithm Design & Specifications

### 2.1 Approach 1: Linear Search (Sequential Search)
Linear Search performs a sequential traversal across all records from index $0$ to $n-1$.
- **Preconditions:** None. Operates directly on unsorted arrays.
- **Invariant:** For loop iteration $i$, no element in $A[0..i-1]$ matches the query key.
- **Pseudocode:**
```text
ALGORITHM LinearSearch(A[0..n-1], target_reg_no)
FOR i ← 0 TO n - 1 DO
    IF A[i].reg_no == target_reg_no THEN
        RETURN i
    END IF
END FOR
RETURN -1
```

### 2.2 Approach 2: Iterative Binary Search
Iterative Binary Search applies the Divide and Conquer strategy on a sorted array of student records.
- **Preconditions:** Array must be monotonically sorted in ascending order of `reg_no`.
- **Invariant:** If `target_reg_no` exists in $A$, it must reside in $A[\text{low}..\text{high}]$.
- **Pseudocode:**
```text
ALGORITHM BinarySearchIterative(A[0..n-1], target_reg_no)
low ← 0, high ← n - 1
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

### 2.3 Approach 3: Recursive Binary Search
Recursive Binary Search divides the search interval and recursively invokes itself on one sub-interval.
- **Preconditions:** Sorted array by `reg_no`.
- **Pseudocode:**
```text
ALGORITHM BinarySearchRecursiveHelper(A, target, low, high)
IF low > high THEN
    RETURN -1
END IF
mid ← low + ⌊(high - low) / 2⌋
IF A[mid].reg_no == target THEN
    RETURN mid
ELSE IF target < A[mid].reg_no THEN
    RETURN BinarySearchRecursiveHelper(A, target, low, mid - 1)
ELSE
    RETURN BinarySearchRecursiveHelper(A, target, mid + 1, high)
END IF
```

---

## 3. Basic Operations & Mathematical Derivations

### 3.1 Identification of Basic Operation
The **Basic Operation** is the operation executed most frequently in the innermost loop:
- **Linear Search:** Key equality comparison: `target_reg_no == A[i].reg_no`.
- **Binary Search (Iterative & Recursive):** Three-way key comparison: `target_reg_no <=> A[mid].reg_no`.

### 3.2 Closed-Form Operation Counts
- **Linear Search (Worst-Case):**
  $$C(n) = \sum_{i=0}^{n-1} 1 = n$$
- **Binary Search (Worst-Case):**
  The array size is halved at each step until size $\le 1$:
  $$\frac{n}{2^k} \le 1 \implies k = \lfloor \log_2 n \rfloor + 1$$
- **Auxiliary Space Complexity:**
  - Linear Search: $O(1)$
  - Iterative Binary Search: $O(1)$
  - Recursive Binary Search: $O(\log_2 n)$ stack frames ($\approx 20$ frames at $N=1,000,000$).

---

## 4. Best-, Average-, and Worst-Case Analysis

### 4.1 Linear Search Case Analysis
- **Best Case:** Target at index 0 $\implies C_{\text{best}}(n) = 1 \implies \Omega(1)$.
- **Worst Case:** Target at index $n-1$ or absent $\implies C_{\text{worst}}(n) = n \implies O(n)$.
- **Average Case:** Assuming uniform distribution across $n$ positions:
  $$E[C(n)] = \sum_{i=1}^n i \cdot \frac{1}{n} = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2} \implies \Theta(n)$$

### 4.2 Binary Search Case Analysis
- **Best Case:** Target at initial midpoint $\implies C_{\text{best}}(n) = 1 \implies \Omega(1)$.
- **Worst Case:** Target at leaf of decision tree or absent $\implies C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1 \implies O(\log n)$.
- **Average Case:** From internal path length of binary tree:
  $$E[C(n)] \approx \log_2 n - 1 \implies \Theta(\log n)$$

---

## 5. Asymptotic Analysis & Formal Proofs

### 5.1 Formal Definitions
- $f(n) \in O(g(n)) \iff \exists c > 0, n_0 \ge 1 \text{ s.t. } 0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0$.
- $f(n) \in \Omega(g(n)) \iff \exists c > 0, n_0 \ge 1 \text{ s.t. } 0 \le c \cdot g(n) \le f(n) \quad \forall n \ge n_0$.
- $f(n) \in \Theta(g(n)) \iff f(n) \in O(g(n)) \land f(n) \in \Omega(g(n))$.

### 5.2 Mathematical Bounds Summary
| Algorithm | Best-Case Bound | Average-Case Bound | Worst-Case Bound |
| :--- | :--- | :--- | :--- |
| **Linear Search** | $\Omega(1)$ | $\Theta(n)$ | $\Theta(n) \text{ / } O(n)$ |
| **Iterative Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $\Theta(\log n) \text{ / } O(\log n)$ |
| **Recursive Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $\Theta(\log n) \text{ / } O(\log n)$ |

---

## 6. Recurrence Formulation & Multi-Method Solutions

### 6.1 Recurrence Formulation
For Recursive Binary Search:
$$T(n) = \begin{cases} 
c_1 & \text{if } n \le 1 \\
T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + c & \text{if } n > 1 
\end{cases}$$

### 6.2 Solution 1: Substitution (Unrolling) Method
$$T(n) = T(n/2) + c = T(n/4) + 2c = \dots = T(n / 2^i) + i \cdot c$$
Setting $n / 2^i = 1 \implies i = \log_2 n$:
$$T(n) = T(1) + c \log_2 n = c_1 + c \log_2 n \implies \Theta(\log n)$$

### 6.3 Solution 2: Master Theorem
Form: $T(n) = a T(n/b) + f(n)$ where $a = 1, b = 2, f(n) = c = \Theta(1)$.
$$\log_b a = \log_2 1 = 0 \implies n^{\log_b a} = n^0 = 1$$
Since $f(n) = \Theta(n^{\log_b a})$, **Case 2** applies with $k = 0$:
$$T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(\log n)$$

### 6.4 Solution 3: Recursion Tree Method
Single branch tree of depth $\log_2 n$. Each level costs constant work $c$:
$$\text{Total Cost} = \sum_{j=0}^{(\log_2 n) - 1} c + d = c \log_2 n + d \implies \Theta(\log n)$$

---

## 7. Experimental Performance & Empirical Results

Benchmarking was executed across input sizes $N \in \{100, 1\,000, 10\,000, 100\,000, 500\,000, 1\,000\,000\}$:

### 7.1 Measured Execution Times ($\mu s$)
| $N$ | Linear (Best) | Linear (Avg) | Linear (Worst) | Iterative Binary (Avg) | Iterative Binary (Worst) | Recursive Binary (Worst) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **100** | $1.15\,\mu s$ | $3.53\,\mu s$ | $6.26\,\mu s$ | $1.62\,\mu s$ | $1.79\,\mu s$ | $6.61\,\mu s$ |
| **1,000** | $0.85\,\mu s$ | $57.00\,\mu s$ | $75.74\,\mu s$ | $2.85\,\mu s$ | $2.84\,\mu s$ | $4.96\,\mu s$ |
| **10,000** | $0.78\,\mu s$ | $499.09\,\mu s$ | $976.03\,\mu s$ | $3.73\,\mu s$ | $3.83\,\mu s$ | $4.87\,\mu s$ |
| **100,000** | $1.00\,\mu s$ | $4,955.15\,\mu s$ | $9,841.17\,\mu s$ | $5.44\,\mu s$ | $4.54\,\mu s$ | $6.27\,\mu s$ |
| **500,000** | $2.50\,\mu s$ | $27,012.12\,\mu s$ | $46,781.50\,\mu s$ | $5.10\,\mu s$ | $5.35\,\mu s$ | $6.46\,\mu s$ |
| **1,000,000**| $0.80\,\mu s$ | $37,228.32\,\mu s$ | $63,449.70\,\mu s$ | $3.14\,\mu s$ | $3.39\,\mu s$ | $4.14\,\mu s$ |

### 7.2 Measured Key Comparisons
| $N$ | Linear Worst Observed | Linear Theory ($N$) | Binary Worst Observed | Binary Theory ($\lfloor \log_2 N \rfloor + 1$) | Match |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **100** | 100 | 100 | 7 | 7 | **100% Exact** |
| **1,000** | 1,000 | 1,000 | 10 | 10 | **100% Exact** |
| **10,000** | 10,000 | 10,000 | 14 | 14 | **100% Exact** |
| **100,000** | 100,000 | 100,000 | 17 | 17 | **100% Exact** |
| **500,000** | 500,000 | 500,000 | 19 | 19 | **100% Exact** |
| **1,000,000**| 1,000,000 | 1,000,000 | 20 | 20 | **100% Exact** |

---

## 8. Theoretical vs Experimental Validation & Deviation Analysis
- **Ratio Convergence:** The ratio $T_{\text{lin}}(N)/N \to 0.06\text{--}0.09\,\mu s/\text{item}$ and $T_{\text{bin}}(N)/\log_2 N \to 0.17\text{--}0.28\,\mu s/\text{step}$ converge to flat asymptotes, confirming mathematical proportionality.
- **Physical Hardware Realities:** Observed timings reflect L1/L2/L3 cache misses at $N = 1,000,000$ (where the array spans $8\text{ MB}$), branch prediction overhead, and Python function call frame overhead.

---

## 9. Final Algorithm Recommendation
**Iterative Binary Search** is recommended:
1. **$18,700\times$ Latency Advantage:** Runs in $3.14\,\mu s$ compared to $63,450\,\mu s$ for Linear Search at 1M records.
2. **Memory Efficiency:** Strictly $O(1)$ space with zero stack frame allocations.
3. **Sorting Amortization:** The $O(N \log N)$ sorting cost is fully amortized after only 5 search queries.

---

## 10. Day-4 Design Challenge Architecture & Defence
- **Workload:** 1,000,000 records, 50,000 queries/hour ($\approx 13.89$ QPS avg, $70$ QPS peak), daily batch updates.
- **Feasibility:** 
  - Linear Search fails under peak load (would require $> 2.6$ dedicated 100% saturated CPU cores).
  - Iterative Binary Search single-core utilization:
    $$\text{Peak CPU Utilization} = 70 \text{ QPS} \times 3.14\,\mu s = \mathbf{0.022\%}$$
- **Zero-Downtime Double Buffering (RCU):**
  Nightly batch updates append new $k$ records to a secondary standby buffer, sort/merge in $< 150\text{ ms}$, and perform an atomic pointer swap. Readers never block, experiencing $100\%$ zero-downtime and sub-$4\,\mu s$ latency.

---

## 11. Conclusion
Course Outcome 1 (CO1) has been thoroughly fulfilled. Theoretical complexity derivations, asymptotic proofs, multi-method recurrence solutions, comprehensive unit testing, multi-scale empirical benchmarking, and production systems architecture collectively demonstrate the algorithmic superiority and operational viability of Iterative Binary Search.
