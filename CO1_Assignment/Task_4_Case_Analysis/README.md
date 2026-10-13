# Task 4: Best-, Average-, and Worst-Case Analysis

## 1. Overview of Case Analysis
Algorithms often display differing execution times depending on the distribution of input data and the position of the search target. We analyze the three classical cases:
- **Best Case:** The scenario where the minimal number of basic operations is executed.
- **Worst Case:** The scenario where the maximum possible number of basic operations is executed.
- **Average Case:** The expected value of operations performed, assuming a probabilistic distribution over all possible inputs.

---

## 2. Case Analysis: Linear Search

### 2.1 Best-Case Analysis
- **Condition:** The target registration number resides at index `0` of the database (the very first element).
- **Basic Operations:** Exactly $1$ string comparison.
- **Complexity:** 
  $$C_{\text{best}}(n) = 1 \implies \Omega(1)$$

### 2.2 Worst-Case Analysis
- **Condition:** The target registration number is located at the last index $n - 1$, or does not exist anywhere in the database.
- **Basic Operations:** The loop must iterate through every element from index $0$ to $n - 1$.
- **Complexity:** 
  $$C_{\text{worst}}(n) = n \implies O(n)$$

### 2.3 Average-Case Analysis (Rigorous Mathematical Derivation)
Assume the target is present in the database with probability $p \in [0, 1]$, and if present, is uniformly distributed across all $n$ positions with probability $\frac{1}{n}$.

#### Case A: Successful Search ($p = 1$)
The target is equally likely to be at any index $i \in \{1, 2, \dots, n\}$.
The number of comparisons required to find an element at position $i$ is $i$.
The expected number of comparisons $E[C(n)]$ is:
$$E[C(n)] = \sum_{i=1}^{n} i \cdot P(\text{target at position } i)$$
$$E[C(n)] = \sum_{i=1}^{n} i \cdot \frac{1}{n} = \frac{1}{n} \sum_{i=1}^{n} i$$
Using the arithmetic progression summation identity $\sum_{i=1}^n i = \frac{n(n+1)}{2}$:
$$E[C(n)] = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n + 1}{2}$$

#### Case B: General Search with Success Probability $p$
If the probability of presence is $p$, and absence is $1 - p$ (which always requires $n$ comparisons):
$$E[C(n)] = p \left(\frac{n+1}{2}\right) + (1-p) n = n \left(1 - \frac{p}{2}\right) + \frac{p}{2}$$
For $p = 1$: $E[C(n)] = \frac{n+1}{2} \approx 0.5 n$.
For $p = 0.5$: $E[C(n)] = 0.75 n + 0.25$.
In all non-zero cases:
$$C_{\text{avg}}(n) = \Theta(n)$$

---

## 3. Case Analysis: Binary Search (Iterative & Recursive)

### 3.1 Best-Case Analysis
- **Condition:** The target registration number is positioned precisely at the root of the binary decision tree (i.e., at index $\text{mid} = \lfloor (n - 1)/2 \rfloor$ in the first iteration).
- **Basic Operations:** Exactly $1$ comparison.
- **Complexity:**
  $$C_{\text{best}}(n) = 1 \implies \Omega(1)$$

### 3.2 Worst-Case Analysis
- **Condition:** The target registration number corresponds to a leaf node in the binary decision tree, or is completely absent from the database.
- **Basic Operations:** The search space must be repeatedly halved until $\text{low} > \text{high}$.
- **Formula:**
  $$C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1 \implies O(\log n)$$

For $n = 1,000,000$:
$$C_{\text{worst}}(1,000,000) = \lfloor \log_2(1,000,000) \rfloor + 1 = 19 + 1 = 20 \text{ comparisons}$$

### 3.3 Average-Case Analysis (Binary Decision Tree Derivation)
In a binary decision tree of $n$ keys:
- Level $j$ (where $j \in \{1, 2, \dots, h+1\}$) contains at most $2^{j-1}$ keys.
- Searching for a key at level $j$ requires exactly $j$ comparisons.
- Total internal path length $I(n)$ for a complete binary tree of size $n$:
  $$I(n) = \sum_{j=1}^{h+1} j \cdot 2^{j-1} \approx (h-1)2^{h+1} + 2$$
Dividing by $n \approx 2^{h+1} - 1$:
$$E[C_{\text{bin}}(n)] = \frac{I(n)}{n} \approx \frac{(h-1) 2^{h+1}}{2^{h+1}} = h - 1 \approx \log_2 n - 1$$

For $n = 1,000,000$:
$$E[C_{\text{bin}}(1,000,000)] \approx 20 - 1 = 19 \text{ comparisons}$$

---

## 4. Comprehensive Comparison Table

| Case Scenario | Linear Search | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Best-Case Operations** | $1$ | $1$ | $1$ |
| **Best-Case Notation** | $\Omega(1)$ | $\Omega(1)$ | $\Omega(1)$ |
| **Average-Case Operations** | $\frac{n+1}{2} \approx 0.5n$ | $\approx \log_2 n - 1$ | $\approx \log_2 n - 1$ |
| **Average-Case Notation** | $\Theta(n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ |
| **Worst-Case Operations** | $n$ | $\lfloor \log_2 n \rfloor + 1$ | $\lfloor \log_2 n \rfloor + 1$ |
| **Worst-Case Notation** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Absent Target Operations**| $n$ | $\lfloor \log_2 n \rfloor + 1$ | $\lfloor \log_2 n \rfloor + 1$ |

### Numerical Comparison at $N = 1,000,000$:
- **Linear Search Average:** $500,000$ comparisons.
- **Binary Search Average:** $19$ comparisons.
- **Speedup Factor in Comparisons:** $\frac{500,000}{19} \approx \mathbf{26,315\times}$ reduction in basic operations!
