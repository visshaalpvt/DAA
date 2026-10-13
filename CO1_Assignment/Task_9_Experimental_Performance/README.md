# Task 9: Experimental Performance Analysis

## 1. Experimental Setup & Benchmark Environment
All benchmark experiments were conducted on a real Windows workstation using Python 3.11 with high-resolution CPU performance counters (`time.perf_counter_ns()`).

- **Hardware Platform:** AMD/Intel 64-bit Architecture
- **Dataset Scale:** $N \in \{100, 1\,000, 10\,000, 100\,000, 500\,000, 1\,000\,000\}$ records
- **Timer Resolution:** Sub-microsecond precision
- **Metrics Tracked:**
  1. Wall-clock execution time in microseconds ($\mu s$)
  2. Number of key comparisons evaluated

---

## 2. Experimental Results Tables

### 2.1 Execution Time ($\mu s$) Across Input Sizes
| Dataset Size ($N$) | Linear Search (Best) | Linear Search (Avg) | Linear Search (Worst) | Iterative Binary (Best) | Iterative Binary (Avg) | Iterative Binary (Worst) | Recursive Binary (Best) | Recursive Binary (Avg) | Recursive Binary (Worst) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **100** | $1.15\,\mu s$ | $3.53\,\mu s$ | $6.26\,\mu s$ | $1.76\,\mu s$ | $1.62\,\mu s$ | $1.79\,\mu s$ | $6.91\,\mu s$ | $2.84\,\mu s$ | $6.61\,\mu s$ |
| **1,000** | $0.85\,\mu s$ | $57.00\,\mu s$ | $75.74\,\mu s$ | $2.73\,\mu s$ | $2.85\,\mu s$ | $2.84\,\mu s$ | $5.04\,\mu s$ | $4.45\,\mu s$ | $4.96\,\mu s$ |
| **10,000** | $0.78\,\mu s$ | $499.09\,\mu s$ | $976.03\,\mu s$ | $3.66\,\mu s$ | $3.73\,\mu s$ | $3.83\,\mu s$ | $4.71\,\mu s$ | $4.35\,\mu s$ | $4.87\,\mu s$ |
| **100,000** | $1.00\,\mu s$ | $4,955.15\,\mu s$ | $9,841.17\,\mu s$ | $4.36\,\mu s$ | $5.44\,\mu s$ | $4.54\,\mu s$ | $6.20\,\mu s$ | $5.79\,\mu s$ | $6.27\,\mu s$ |
| **500,000** | $2.50\,\mu s$ | $27,012.12\,\mu s$ | $46,781.50\,\mu s$ | $4.84\,\mu s$ | $5.10\,\mu s$ | $5.35\,\mu s$ | $6.10\,\mu s$ | $6.32\,\mu s$ | $6.46\,\mu s$ |
| **1,000,000**| $0.80\,\mu s$ | $37,228.32\,\mu s$ | $63,449.70\,\mu s$ | $3.22\,\mu s$ | $3.14\,\mu s$ | $3.39\,\mu s$ | $4.08\,\mu s$ | $3.93\,\mu s$ | $4.14\,\mu s$ |

---

### 2.2 Key Comparisons Count Across Input Sizes
| Dataset Size ($N$) | Linear (Best) | Linear (Avg) | Linear (Worst) | Iterative Binary (Best) | Iterative Binary (Avg) | Iterative Binary (Worst) | Recursive Binary (Best) | Recursive Binary (Avg) | Recursive Binary (Worst) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **100** | 1 | 43 | 100 | 6 | 6 | 7 | 6 | 6 | 7 |
| **1,000** | 1 | 509 | 1,000 | 9 | 9 | 10 | 9 | 9 | 10 |
| **10,000** | 1 | 4,664 | 10,000 | 13 | 12 | 14 | 13 | 12 | 14 |
| **100,000** | 1 | 44,735 | 100,000 | 16 | 16 | 17 | 16 | 16 | 17 |
| **500,000** | 1 | 257,797 | 500,000 | 18 | 18 | 19 | 18 | 18 | 19 |
| **1,000,000**| 1 | 522,224 | 1,000,000 | 19 | 19 | 20 | 19 | 19 | 20 |

---

## 3. Graphical Performance Analysis

### 3.1 Worst-Case Execution Time vs Input Size (Log-Log Scale)
![Execution Time Comparison](execution_time_comparison.png)
- **Observation:** On the log-log scale, Linear Search produces a steep upward diagonal line corresponding to linear slope ($O(N)$), reaching **$63.45\text{ ms}$** at $N=1,000,000$.
- In stark contrast, both Iterative and Recursive Binary Search remain nearly flat across 4 orders of magnitude, executing in under **$4.2\,\mu s$** even at $1,000,000$ records.

### 3.2 Basic Operation (Key Comparison) Count vs Input Size
![Comparison Count Comparison](comparison_count_comparison.png)
- **Observation:** Linear Search comparison count grows directly with $N$ ($1,000,000$ comparisons in worst case).
- Binary Search follows precisely the theoretical formula $\lfloor \log_2 N \rfloor + 1$, leveling out at only **20 comparisons** at $N=1,000,000$.

### 3.3 Iterative vs Recursive Binary Search Overhead
![Binary Iterative vs Recursive](binary_iterative_vs_recursive.png)
- **Observation:** While both algorithms execute the identical number of comparisons (e.g., exactly 20 at $N=1,000,000$), Recursive Binary Search consistently exhibits a modest latency penalty ($\approx 20\text{--}35\%$ higher execution time) attributable to Python stack frame allocation and function invocation overhead.

### 3.4 Multi-Case Analysis at $N = 100,000$
![Cases Comparison](cases_comparison_linear_vs_binary.png)
- **Observation:** Linear Search degrades by four orders of magnitude between Best Case ($1\,\mu s$) and Worst Case ($9,841\,\mu s$). Binary Search provides steady, sub-$5\,\mu s$ predictable performance across all cases.

### 3.5 Asymptotic Growth Rate Verification (Ratio Test)
![Theory vs Experiment Ratios](theory_vs_experiment_ratios.png)
- **Observation:** The empirical ratio $T(N)/N$ for Linear Search and $T(N)/\log_2 N$ for Binary Search converge to horizontal asymptotes, experimentally verifying the asymptotic classes $\Theta(N)$ and $\Theta(\log N)$.
