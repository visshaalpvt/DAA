# Task 6: Recurrence Formulation for Recursive Search

## 1. Algorithmic Breakdown of Recursive Binary Search

Recursive Binary Search breaks down the search process into three classic Divide-and-Conquer phases:

1. **Divide:**
   The algorithm calculates the midpoint of the current search interval:
   $$\text{mid} = \text{low} + \left\lfloor \frac{\text{high} - \text{low}}{2} \right\rfloor$$
   This involves integer addition, subtraction, and bit shift/division. This takes constant time $c_{\text{div}} = \Theta(1)$.

2. **Inspect & Branch (Basic Operation):**
   Compare the target registration number with $A[\text{mid}]$.
   - If equal, return $\text{mid}$ immediately (Best Case, $\Theta(1)$).
   - If target $< A[\text{mid}]$, branch to left sub-array: range $[ \text{low}, \text{mid} - 1 ]$.
   - If target $> A[\text{mid}]$, branch to right sub-array: range $[ \text{mid} + 1, \text{high} ]$.
   
3. **Conquer:**
   Notice critically: Unlike Merge Sort (which solves **two** subproblems $2T(n/2)$), Binary Search solves **only ONE** subproblem of half the size:
   $$\text{Subproblem size} = \left\lfloor \frac{n}{2} \right\rfloor$$

4. **Combine:**
   The return value of the recursive invocation is passed directly back up the stack. Combining requires zero additional processing: $c_{\text{comb}} = \Theta(1)$.

---

## 2. Mathematical Recurrence Relation

Let $T(n)$ represent the worst-case running time for a sub-array of $n$ elements, where $n = \text{high} - \text{low} + 1$.

### 2.1 Base Cases
- When $n = 0$ (i.e., $\text{low} > \text{high}$), the element is absent:
  $$T(0) = c_0$$
- When $n = 1$ (i.e., $\text{low} == \text{high}$), exactly 1 comparison is performed:
  $$T(1) = c_1$$

### 2.2 Recursive Step ($n > 1$)
For an input size $n > 1$, the worst-case scenario occurs when the search target is not at the midpoint:
$$T(n) = T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + f(n)$$
where $f(n)$ represents the non-recursive overhead:
$$f(n) = c_{\text{div}} + c_{\text{comp}} + c_{\text{comb}} = c \quad (\text{a constant independent of } n)$$

### 2.3 Formal Recurrence Equation
$$T(n) = \begin{cases} 
c_1 & \text{if } n \le 1 \\
T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + c & \text{if } n > 1 
\end{cases}$$

---

## 3. Comparison with Other Recursive Patterns
To appreciate the efficiency of this recurrence, consider how it contrasts with standard algorithms:

| Algorithm | Recurrence Relation | Number of Subproblems ($a$) | Size Reduction Factor ($b$) | Asymptotic Class |
| :--- | :--- | :--- | :--- | :--- |
| **Recursive Binary Search** | $T(n) = T(n/2) + c$ | $1$ | $2$ | $\Theta(\log n)$ |
| **Binary Tree Traversal** | $T(n) = 2T(n/2) + c$ | $2$ | $2$ | $\Theta(n)$ |
| **Merge Sort** | $T(n) = 2T(n/2) + c \cdot n$ | $2$ | $2$ | $\Theta(n \log n)$ |
| **Linear Search (Recursive)**| $T(n) = T(n - 1) + c$ | $1$ | Decrement ($n-1$) | $\Theta(n)$ |

This clearly highlights why Recursive Binary Search scales exponentially better: at each step, exactly half the remaining records are eliminated while solving only **one** subproblem.
