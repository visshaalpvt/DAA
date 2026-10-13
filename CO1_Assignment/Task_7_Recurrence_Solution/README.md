# Task 7: Step-by-Step Recurrence Solution

## 1. Problem Statement
We solve the recurrence relation derived in Task 6:
$$T(n) = T\left(\frac{n}{2}\right) + c \quad \text{for } n > 1, \quad \text{with } T(1) = d$$
where $c$ and $d$ are positive constants.

We provide complete, rigorous mathematical solutions using three independent analytical methods:
1. **The Substitution (Iteration / Unrolling) Method**
2. **The Master Theorem**
3. **The Recursion Tree Method**

---

## 2. Method 1: The Substitution / Iteration Method (Unrolling)

### Step 1: Successive Expansions
Assume for simplicity $n = 2^k \implies k = \log_2 n$.
- Expansion 1:
  $$T(n) = T\left(\frac{n}{2}\right) + c$$
- Expansion 2:
  Substitute $T(n/2) = T(n/4) + c$:
  $$T(n) = \left[T\left(\frac{n}{4}\right) + c\right] + c = T\left(\frac{n}{4}\right) + 2c = T\left(\frac{n}{2^2}\right) + 2c$$
- Expansion 3:
  Substitute $T(n/4) = T(n/8) + c$:
  $$T(n) = \left[T\left(\frac{n}{8}\right) + c\right] + 2c = T\left(\frac{n}{8}\right) + 3c = T\left(\frac{n}{2^3}\right) + 3c$$

### Step 2: General $i$-th Expansion Formula
By mathematical induction, after $i$ substitutions:
$$T(n) = T\left(\frac{n}{2^i}\right) + i \cdot c$$

### Step 3: Reaching the Base Case
The recursion stops when the subproblem size reaches the base case $n / 2^i = 1$:
$$\frac{n}{2^i} = 1 \implies 2^i = n \implies i = \log_2 n$$

### Step 4: Substitution of $i$
Substitute $i = \log_2 n$ into the general formula:
$$T(n) = T(1) + (\log_2 n) \cdot c$$
Using the base condition $T(1) = d$:
$$T(n) = d + c \log_2 n$$

### Conclusion:
Since $c > 0$ and $d > 0$:
$$T(n) = \Theta(\log n)$$

---

## 3. Method 2: The Master Theorem

The Master Theorem provides a cookbook solution for recurrences of the form:
$$T(n) = a T\left(\frac{n}{b}\right) + f(n)$$
where $a \ge 1, b > 1$, and $f(n)$ is an asymptotically positive function.

### Step 1: Identify Parameters
For our binary search recurrence $T(n) = T(n/2) + c$:
- $a = 1$ (number of recursive calls)
- $b = 2$ (subproblem reduction factor)
- $f(n) = c = \Theta(1) = \Theta(n^0)$

### Step 2: Compute the Critical Exponent
$$\log_b a = \log_2 1 = 0$$
Hence, the watershed function is:
$$n^{\log_b a} = n^0 = 1$$

### Step 3: Match Master Theorem Case
Compare $f(n)$ with $n^{\log_b a}$:
$$f(n) = c = \Theta(1) = \Theta(n^{\log_b a})$$
This matches **Case 2** of the Master Theorem:
> If $f(n) = \Theta(n^{\log_b a} \log^k n)$ where $k = 0$, then:
> $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$

### Step 4: Evaluate Solution
Substituting $a = 1, b = 2, k = 0$:
$$T(n) = \Theta(n^0 \log^{0+1} n) = \Theta(1 \cdot \log n) = \Theta(\log n)$$

---

## 4. Method 3: The Recursion Tree Method

### Step 1: Structural Tree Analysis
In Recursive Binary Search, because $a = 1$, each node has exactly **one child**. The tree is a single chain (degenerate tree) from the root to the single leaf:

```text
Level 0:        T(n)             Cost = c
                 │
Level 1:        T(n/2)           Cost = c
                 │
Level 2:        T(n/4)           Cost = c
                 │
                ...
                 │
Level k:        T(1)             Cost = d (Base Case)
```

### Step 2: Cost Analysis per Level
- **Level 0:** 1 node of size $n$, work done $= c$.
- **Level 1:** 1 node of size $n/2$, work done $= c$.
- **Level 2:** 1 node of size $n/4$, work done $= c$.
- **Level $j$:** 1 node of size $n/2^j$, work done $= c$.
- **Level $k = \log_2 n$ (Leaf):** 1 node of size 1, work done $= d$.

### Step 3: Summation Across All Levels
$$\text{Total Cost} = \sum_{j=0}^{(\log_2 n) - 1} (\text{Cost at level } j) + (\text{Cost at leaf level})$$
$$\text{Total Cost} = \sum_{j=0}^{(\log_2 n) - 1} c + d$$
$$\text{Total Cost} = c \cdot \log_2 n + d$$

### Conclusion:
$$\text{Total Cost} = c \log_2 n + d = \Theta(\log n)$$

---

## 5. Synthesis of Mathematical Methods
All three independent analytical approaches rigorously converge to the exact identical closed form:
$$T(n) = c \log_2 n + d \in \mathbf{\Theta(\log n)}$$

This mathematically guarantees that the number of operations grows purely logarithmically with database size, explaining why even for 1,000,000 records, the algorithm requires no more than 20 iterations.
