# Task 2: Identification of Basic Operations

## 1. Concept of Basic Operation in Algorithm Analysis
In algorithm analysis, the **Basic Operation** is defined as the fundamental instruction that is executed the highest number of times in the innermost loop (or recursive step) and contributes the most significantly to the overall running time $T(n)$.

Let $c_{op}$ be the execution time of one basic operation, and $C(n)$ be the total count of basic operations executed for an input of size $n$. The total running time is modeled as:
$$T(n) \approx c_{op} \cdot C(n)$$

---

## 2. Basic Operation Analysis Across the Algorithms

### 2.1 Linear Search (Sequential)
- **Identified Basic Operation:** Key comparison between the query registration number and the element's registration number:
  $$\text{target\_reg\_no} == \text{A}[i].\text{reg\_no}$$
- **Contribution to Execution:** In each iteration of the loop, this string equality comparison is evaluated once.
- **Accompanying Overhead Operations:**
  - Loop index incrementation: $i \leftarrow i + 1$.
  - Loop boundary check: $i < n$.
  - Array indexing / memory dereferencing: $\&A[i]$.

### 2.2 Iterative Binary Search
- **Identified Basic Operation:** Three-way key comparison between the target registration number and the midpoint element:
  $$\text{target\_reg\_no} \lesseqgtr \text{A}[\text{mid}].\text{reg\_no}$$
- **Contribution to Execution:** In every pass of the `while (low <= high)` loop, the target string is compared against the string at `mid`. Depending on hardware architecture and compiler optimizations, this is either implemented as a single three-way comparator (e.g., `strcmp` / `<=>` returning negative, zero, or positive) or two binary boolean evaluations (`==` followed by `<`). In theoretical analysis, this counts as **1 primary key comparison per interval bisection**.
- **Accompanying Overhead Operations:**
  - Midpoint arithmetic calculation: $\text{mid} = \text{low} + \lfloor (\text{high} - \text{low}) / 2 \rfloor$.
  - Pointer/boundary updates: $\text{low} = \text{mid} + 1$ or $\text{high} = \text{mid} - 1$.
  - Loop continuation condition check: $\text{low} \le \text{high}$.

### 2.3 Recursive Binary Search
- **Identified Basic Operation:** Three-way key comparison at midpoint:
  $$\text{target\_reg\_no} \lesseqgtr \text{A}[\text{mid}].\text{reg\_no}$$
- **Contribution to Execution:** Identical comparison count to iterative binary search.
- **Accompanying Overhead Operations (Stack Cost):**
  - Activation record push: Parameter passing (`arr`, `target`, `low`, `high`) onto the runtime call stack.
  - Return address storage and instruction pointer jumps.
  - Stack frame destruction and unwinding upon termination.
  - Base case evaluation check: `low > high`.

---

## 3. Comparison Matrix: Basic Operations vs Overhead

| Algorithm | Basic Operation | Type | Cost per Operation | Frequency Range $C(n)$ | Secondary Overhead Factors |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | `target == A[i].reg_no` | String Equality Comparison | $O(L)$ where $L$ is string length | $1 \le C(n) \le n$ | Loop counter, bounds checking |
| **Iterative Binary Search** | `target <=> A[mid].reg_no` | Three-way String Comparison | $O(L)$ | $1 \le C(n) \le \lfloor \log_2 n \rfloor + 1$ | Midpoint division, pointer assignments |
| **Recursive Binary Search** | `target <=> A[mid].reg_no` | Three-way String Comparison | $O(L)$ | $1 \le C(n) \le \lfloor \log_2 n \rfloor + 1$ | Call stack frame pushes/pops, recursion depth |

---

## 4. Key Takeaways
1. In all three algorithms, string comparison between 18-character registration strings represents the dominant CPU cycle consumer.
2. Binary search reduces the frequency of this basic operation exponentially from $O(n)$ down to $O(\log_2 n)$.
3. While Iterative and Recursive Binary Search execute the exact same count of basic operations, Recursive Binary Search suffers from additional constant overhead per operation due to stack frame maintenance.
