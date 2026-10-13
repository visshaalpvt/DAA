# Task 5: Asymptotic Complexity Analysis

## 1. Formal Mathematical Definitions

### 1.1 Big-O Notation (Asymptotic Upper Bound)
Let $f(n)$ and $g(n)$ be functions mapping non-negative integers to real numbers. We say:
$$f(n) \in O(g(n))$$
if and only if there exist positive constants $c > 0$ and $n_0 \ge 1$ such that:
$$0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0$$

### 1.2 Big-Omega Notation (Asymptotic Lower Bound)
$$f(n) \in \Omega(g(n))$$
if and only if there exist positive constants $c > 0$ and $n_0 \ge 1$ such that:
$$0 \le c \cdot g(n) \le f(n) \quad \forall n \ge n_0$$

### 1.3 Big-Theta Notation (Asymptotic Tight Bound)
$$f(n) \in \Theta(g(n))$$
if and only if $f(n) \in O(g(n))$ and $f(n) \in \Omega(g(n))$, meaning there exist positive constants $c_1, c_2 > 0$ and $n_0 \ge 1$ such that:
$$0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \forall n \ge n_0$$

---

## 2. Formal Asymptotic Proofs

### 2.1 Linear Search (Worst Case)
- **Claim:** $T(n) \in \Theta(n)$
- **Proof:**
  In the worst case, Linear Search performs $n$ comparisons plus constant initialization and return costs:
  $$T(n) = a \cdot n + b \quad \text{where } a > 0, b \ge 0$$
  
  **Upper Bound ($O(n)$):**
  For $n \ge 1$:
  $$T(n) = a \cdot n + b \le a \cdot n + b \cdot n = (a + b) \cdot n$$
  Choose $c_2 = a + b$ and $n_0 = 1$. Then $T(n) \le c_2 \cdot n$ for all $n \ge 1$. Hence, $T(n) \in O(n)$.
  
  **Lower Bound ($\Omega(n)$):**
  For $n \ge 1$:
  $$T(n) = a \cdot n + b \ge a \cdot n$$
  Choose $c_1 = a$ and $n_0 = 1$. Then $c_1 \cdot n \le T(n)$ for all $n \ge 1$. Hence, $T(n) \in \Omega(n)$.
  
  Since $c_1 \cdot n \le T(n) \le c_2 \cdot n$ for all $n \ge 1$, we conclude:
  $$T_{\text{worst}}(n) \in \Theta(n) \quad \blacksquare$$

---

### 2.2 Binary Search (Worst Case)
- **Claim:** $T(n) \in \Theta(\log n)$
- **Proof:**
  In the worst case, the total number of comparisons is $C(n) = \lfloor \log_2 n \rfloor + 1$.
  The running time function can be bounded by:
  $$T(n) = a \cdot \lfloor \log_2 n \rfloor + b \quad \text{with } a > 0, b > 0$$

  **Upper Bound ($O(\log n)$):**
  Since $\lfloor \log_2 n \rfloor \le \log_2 n$:
  $$T(n) \le a \log_2 n + b$$
  For $n \ge 2$, $\log_2 n \ge 1 \implies b \le b \log_2 n$:
  $$T(n) \le a \log_2 n + b \log_2 n = (a + b) \log_2 n$$
  Choose $c_2 = a + b$ and $n_0 = 2$. Then $T(n) \le c_2 \log_2 n$ for all $n \ge n_0$. Hence, $T(n) \in O(\log n)$.

  **Lower Bound ($\Omega(\log n)$):**
  Since $\lfloor \log_2 n \rfloor \ge \log_2 n - 1$:
  $$T(n) \ge a (\log_2 n - 1) + b = a \log_2 n + (b - a)$$
  For sufficiently large $n$ (specifically $n \ge 4$ such that $\log_2 n \ge 2$):
  $$a \log_2 n - a \ge \frac{a}{2} \log_2 n$$
  Choose $c_1 = \frac{a}{2}$ and $n_0 = 4$. Then $c_1 \log_2 n \le T(n)$ for all $n \ge n_0$. Hence, $T(n) \in \Omega(\log n)$.

  Therefore:
  $$c_1 \log_2 n \le T(n) \le c_2 \log_2 n \quad \forall n \ge 4 \implies T(n) \in \Theta(\log n) \quad \blacksquare$$

---

## 3. Limit Test for Asymptotic Orders of Growth

To rigorously compare the growth rates of Linear Search vs Binary Search:
$$\lim_{n \to \infty} \frac{T_{\text{Binary}}(n)}{T_{\text{Linear}}(n)} = \lim_{n \to \infty} \frac{k_1 \log_2 n + c_1}{k_2 n + c_2}$$
Applying L'Hôpital's Rule:
$$= \lim_{n \to \infty} \frac{\frac{k_1}{n \ln 2}}{k_2} = \lim_{n \to \infty} \frac{k_1}{k_2 \ln 2 \cdot n} = 0$$

**Mathematical Consequence:**
Because the limit equals $0$, $T_{\text{Binary}}(n) \in o(T_{\text{Linear}}(n))$ (little-o). The growth of Binary Search is strictly and asymptotically dominated by Linear Search. As $n \to \infty$, Binary Search is infinitely faster than Linear Search.

---

## 4. Master Asymptotic Notation Summary Table

| Algorithm | Best-Case Time | Average-Case Time | Worst-Case Time | Worst-Case Space |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $\Omega(1)$ | $\Theta(n)$ | $O(n) \text{ / } \Theta(n)$ | $\Theta(1)$ |
| **Iterative Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n) \text{ / } \Theta(\log n)$ | $\Theta(1)$ |
| **Recursive Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n) \text{ / } \Theta(\log n)$ | $\Theta(\log n)$ |
