# Design and Analysis of Algorithms (DAA)

Welcome to the **Design and Analysis of Algorithms (DAA)** coursework repository by **Visshaal Natarajan**.

This repository contains implementations, mathematical proofs, asymptotic case analyses, recurrence solutions, empirical benchmarking suites, and production system architectures for academic submissions.

---

## Coursework Components

### [CO1_Assignment: Searching Student Registration Numbers](./CO1_Assignment/)
Comprehensive evaluation of searching algorithms (**Linear Search**, **Iterative Binary Search**, and **Recursive Binary Search**) on datasets up to **1,000,000 student records**, culminating in the **Day-4 Production Design Challenge**.

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

## Key Experimental Highlights

- **Linear Search:** $O(N)$ time, requires $1,000,000$ string comparisons and takes $\approx 63.45\text{ ms}$ in worst-case lookup for $N=1,000,000$.
- **Iterative Binary Search:** $O(\log N)$ time, requires only **$20$ string comparisons** and takes **$3.39\,\mu s$** for $N=1,000,000$ ($> 18,700\times$ faster).
- **Day-4 Design Challenge:** Solved using an in-memory sorted array and atomic Read-Copy-Update (RCU) double buffering to handle 50,000 queries/hour on 1M records with $< 0.03\%$ single-core CPU utilization.

---

## Instructions to Run

```bash
# Clone the repository
git clone https://github.com/visshaalpvt/DAA.git
cd DAA/CO1_Assignment/Task_8_Implementation_Testing/Source_Code

# Run unit tests
python test_suite.py -v

# Run performance benchmarks across N = [100 to 1,000,000]
python benchmark.py
```
