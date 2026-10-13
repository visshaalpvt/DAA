# Task 3: Mathematical Complexity Analysis

## 1. Mathematical Framework
The time complexity of an algorithm is mathematically determined by formulating the exact summation or recurrence representing the total count of basic operations $C(n)$ executed on an input of size $n$.

---

## 2. Mathematical Derivation: Linear Search

### 2.1 Operation Count Summation
In an array $A[0..n-1]$, let $k \in \{0, 1, \dots, n-1\}$ be the zero-based index where the target student registration number is located.
The total number of comparisons performed is given by the summation:
$$C_{\text{found}}(k) = \sum_{i=0}^{k} 1 = k + 1$$

If the element is not found in the array, the loop iterates through all $n$ elements:
$$C_{\text{unsuccessful}}(n) = \sum_{i=0}^{n-1} 1 = n$$

### 2.2 Time Complexity Formula
$$C_{\text{Linear}}(n) = \begin{cases} 
1 & \text{if target is at index } 0 \\
k + 1 & \text{if target is at index } k \\
n & \text{if target is at index } n-1 \text{ or absent}
\end{cases}$$

### 2.3 Space Complexity
Linear search maintains only a single loop counter variable $i$.
$$S_{\text{Linear}}(n) = c_1 = O(1)$$

---

## 3. Mathematical Derivation: Binary Search (Iterative)

### 3.1 Interval Halving Model
Let the initial search space contain $n$ elements. In each iteration of the search loop:
- Iteration 1: Search interval size is $\approx \frac{n}{2}$
- Iteration 2: Search interval size is $\approx \frac{n}{2^2} = \frac{n}{4}$
- Iteration 3: Search interval size is $\approx \frac{n}{2^3} = \frac{n}{8}$
- Iteration $k$: Search interval size is $\approx \frac{n}{2^k}$

The algorithm terminates in the worst case when the search interval is reduced to size 1 (or 0):
$$\frac{n}{2^k} \le 1 \implies n \le 2^k$$
Taking the base-2 logarithm on both sides:
$$\log_2 n \le k \implies k = \lceil \log_2 n \rceil$$

### 3.2 Exact Decision Tree Bound
A binary search on an array of size $n$ can be modeled as a binary decision tree.
- A binary tree of height $h$ can have at most $2^{h+1} - 1$ total nodes.
- To accommodate $n$ distinct keys, the height $h$ must satisfy:
  $$2^h \le n < 2^{h+1} \implies h = \lfloor \log_2 n \rfloor$$
- Since the root node is at level 0 (1 comparison), the maximum number of comparisons in the worst case is:
  $$C_{\text{worst}}(n) = h + 1 = \lfloor \log_2 n \rfloor + 1$$

### 3.3 Space Complexity
Iterative binary search uses two boundary indices `low`, `high`, and midpoint `mid`:
$$S_{\text{Iterative}}(n) = O(1)$$

---

## 4. Mathematical Derivation: Binary Search (Recursive)

### 4.1 Time Complexity
Recursive binary search performs 1 comparison at the current midpoint and then invokes itself on a subproblem of half the size.
$$C(n) = C\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + 1$$
Solving this recurrence via repeated expansion:
$$C(n) = C(n / 2) + 1 = C(n / 4) + 1 + 1 = \dots = C(1) + \underbrace{1 + 1 + \dots + 1}_{k \text{ times}}$$
Since $n / 2^k = 1 \implies k = \log_2 n$:
$$C_{\text{Recursive}}(n) = 1 + \log_2 n = O(\log n)$$

### 4.2 Space Complexity (Call Stack Analysis)
Each recursive call allocates a stack frame containing:
- Return address (8 bytes on 64-bit architecture)
- Pointer to array $A$ (8 bytes)
- Pointer to target string (8 bytes)
- Integer values: `low`, `high`, `mid` (12 bytes)
- Total frame size: $\approx 36\text{--}48$ bytes.

The maximum depth of the call stack is equal to the number of recursive calls made until `low > high`:
$$\text{Stack Depth} = \lfloor \log_2 n \rfloor + 1$$
$$\text{Memory Overhead } S_{\text{Recursive}}(n) = (\text{Frame Size}) \times (\lfloor \log_2 n \rfloor + 1) = O(\log n)$$

For $n = 1,000,000$ records:
- Stack depth $\le 20$ frames.
- Memory used by call stack $\approx 20 \times 48\text{ B} \approx 960\text{ bytes} \approx 1\text{ KB}$.

---

## 5. Mathematical Summary Table

| Metric | Linear Search | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Summation / Recurrence** | $\sum_{i=1}^n 1$ | Halving relation $n/2^k \le 1$ | $T(n) = T(n/2) + 1$ |
| **Closed-Form Operations $C(n)$** | $n$ (worst) | $\lfloor \log_2 n \rfloor + 1$ (worst) | $\lfloor \log_2 n \rfloor + 1$ (worst) |
| **Auxiliary Variables** | $1$ (`i`) | $3$ (`low`, `high`, `mid`) | $3$ parameters per frame |
| **Auxiliary Space Complexity** | $O(1)$ | $O(1)$ | $O(\log n)$ |
