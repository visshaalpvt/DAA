# DAA CO1 Assignment: Searching Student Registration Numbers

## Overview
This repository contains the complete implementation, mathematical analysis, empirical evaluation, and production systems design for **Course Outcome 1 (CO1)** of **Design and Analysis of Algorithms (DAA)**.

The assignment centers on designing, implementing, and analyzing search algorithms for **Student Registration Numbers** across datasets ranging from $100$ to $1,000,000$ records.

---

## Repository Structure
```
CO1_Assignment
│
├── Task_1_Algorithm_Design/         # Algorithm design, explanations, pseudocode & flowcharts
├── Task_2_Basic_Operation/          # Identification of basic operations vs overhead
├── Task_3_Mathematical_Complexity/  # Summation formulas & closed-form time/space derivations
├── Task_4_Case_Analysis/            # Best, Average, and Worst-case probabilistic derivations
├── Task_5_Asymptotic_Analysis/      # Formal definitions and proofs for O, Ω, and Θ
├── Task_6_Recurrence_Formulation/   # Recurrence modeling for recursive binary search
├── Task_7_Recurrence_Solution/      # Step-by-step solutions (Substitution, Master Theorem, Tree)
├── Task_8_Implementation_Testing/   # Source code modules and comprehensive unit tests
│   └── Source_Code/                 # Python implementations of all algorithms & benchmarks
├── Task_9_Experimental_Performance/ # Empirical benchmark results (CSV & high-resolution plots)
├── Task_10_Theory_vs_Experiment/    # Ratio tests, empirical vs theoretical alignment, deviations
├── Task_11_Final_Recommendation/    # Multi-criteria decision matrix & technical justification
├── Task_12_Design_Challenge/        # Day-4 Design Challenge: 50,000 req/hr on 1,000,000 records
├── Report/
│   ├── Source_Code_Screenshots/     # Rendered dark-mode source code presentation cards
│   ├── Output_Screenshots/          # Terminal execution logs & test/benchmark cards
│   ├── Analysis/                    # Consolidated analytical synthesis
│   ├── Tables_and_Graphs/           # High-resolution matplotlib charts and CSV datasets
│   └── Documentation/               # Comprehensive academic technical report
└── README.md
```

---

## Quick Start & Execution Instructions

### Prerequisites
- Python 3.8+ (Tested on Python 3.11)
- `matplotlib`, `numpy`, `pillow`

### 1. Run the Unit Test Suite
To verify algorithm correctness and parity across all test cases and edge cases:
```bash
cd CO1_Assignment/Task_8_Implementation_Testing/Source_Code
python test_suite.py -v
```

### 2. Run the Benchmark Suite
To generate fresh empirical performance metrics across $N \in [100, 1000, 10000, 100000, 500000, 1000000]$:
```bash
cd CO1_Assignment/Task_8_Implementation_Testing/Source_Code
python benchmark.py
```
This automatically updates `benchmark_results.csv` and regenerates all high-resolution performance plots.

---

## Key Experimental Results Summary

| Metric | Linear Search | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Asymptotic Complexity** | $\Theta(n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ |
| **Max Comparisons ($N=1\text{M}$)** | $1,000,000$ | **20** | **20** |
| **Average Latency ($N=1\text{M}$)**| $37.2\text{ ms}$ | **$3.14\,\mu s$** | $3.93\,\mu s$ |
| **Worst-Case Latency ($N=1\text{M}$)**| $63.45\text{ ms}$ | **$3.39\,\mu s$** | $4.14\,\mu s$ |
| **Speedup Factor ($N=1\text{M}$)** | $1\times$ | **$18,700\times$ faster** | $15,300\times$ faster |
| **Auxiliary Memory** | $O(1)$ | **$O(1)$** | $O(\log n)$ |

---

## Day-4 Design Challenge Verdict
- **Workload:** 1,000,000 records, 50,000 search queries per hour ($\approx 14$ QPS average, $70$ QPS peak), daily batch updates.
- **Architectural Solution:** In-memory sorted array utilizing **Iterative Binary Search** coupled with **Zero-Downtime Double Buffering (RCU)**.
- **Resource Footprint:** Consumes **$< 0.03\%$ of a single CPU core** at peak traffic and requires only **$32\text{ MB}$ of RAM**, delivering sub-$4\,\mu s$ response latency and 100% zero-downtime during daily batch syncs.
