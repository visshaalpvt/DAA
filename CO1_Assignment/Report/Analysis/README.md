# Report Analysis: Consolidated Theoretical & Empirical Synthesis

## 1. Executive Summary
This document provides a consolidated technical synthesis of Course Outcome 1 (CO1) for Design and Analysis of Algorithms (DAA), focusing on searching algorithms applied to student registration numbers.

---

## 2. Comparative Matrix: Theory vs Practice

| Metric | Linear Search | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Strategy** | Sequential Brute-Force | Divide and Conquer | Divide and Conquer |
| **Data Structure Requirement** | Any Array | Strictly Sorted Array | Strictly Sorted Array |
| **Basic Operation** | `target == A[i].reg_no` | `target <=> A[mid].reg_no` | `target <=> A[mid].reg_no` |
| **Best-Case Operations** | $1$ ($\Omega(1)$) | $1$ ($\Omega(1)$) | $1$ ($\Omega(1)$) |
| **Average-Case Operations** | $\frac{n+1}{2} \approx 0.5n$ ($\Theta(n)$) | $\approx \log_2 n - 1$ ($\Theta(\log n)$) | $\approx \log_2 n - 1$ ($\Theta(\log n)$) |
| **Worst-Case Operations** | $n$ ($O(n)$) | $\lfloor \log_2 n \rfloor + 1$ ($O(\log n)$) | $\lfloor \log_2 n \rfloor + 1$ ($O(\log n)$) |
| **Observed Comparisons ($N=1\text{M}$)**| $1,000,000$ comparisons | $20$ comparisons | $20$ comparisons |
| **Observed Worst Time ($N=1\text{M}$)** | $63,449.70\,\mu s$ ($63.45\text{ ms}$) | $3.39\,\mu s$ | $4.14\,\mu s$ |
| **Auxiliary Space Complexity** | $O(1)$ | $O(1)$ | $O(\log n)$ ($\approx 20$ stack frames) |
| **Empirical Speedup ($N=1\text{M}$)**| $1\times$ (Baseline) | **$18,716\times$ faster** | **$15,326\times$ faster** |

---

## 3. Key Findings

1. **Logarithmic Dominance:**
   The transition from $O(n)$ to $O(\log n)$ represents a reduction of $99.998\%$ in required CPU operations for databases exceeding 100,000 records.
2. **Predictability Under Worst-Case Loads:**
   While Linear Search exhibits variance proportional to input size (spanning from $1\,\mu s$ up to $63,450\,\mu s$), Binary Search maintains bounded sub-$5\,\mu s$ deterministic latency across all test distributions.
3. **Overhead of Recursion:**
   Iterative Binary Search out-performs Recursive Binary Search by $20\text{--}35\%$ in execution time due to zero call stack maintenance, while avoiding call stack memory overhead.
4. **Day-4 Production Readiness:**
   An in-memory sorted array utilizing Iterative Binary Search combined with Atomic Double Buffering (RCU) easily satisfies the 50,000 requests/hour demand across 1,000,000 student records with $< 0.03\%$ CPU utilization.
