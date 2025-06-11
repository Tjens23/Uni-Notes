
The primary goal of asymptotic analysis is to evaluate algorithms _before_ investing time in their implementation. This involves addressing two main questions:

1. Does the algorithm solve the problem correctly?
2. Is the algorithm efficient in terms of runtime?

These notes will focus on the second question, analyzing the runtime of algorithms.

### Analyzing Runtime

In runtime analysis, an algorithm's runtime is the number of **basic operations** it performs in the **RAM model** for the **worst-case input**. This number of operations is a growing function $f(n)$ of the input size $n$.

The objectives are:

1. Examine how well theoretical analyses in the RAM model align with the observed runtimes of algorithms on real computers.
2. Introduce **asymptotic analysis** as a tool for comparing $f(n)$ for different algorithms.

The goal is to sort algorithms based on the growth rate of their runtimes, avoiding the implementation of those unlikely to be the fastest.

### Analysis vs. Reality


#### Linear Example

```java
public class Linear {
	public static void main(String[] args) {
		long time = System.currentTimeMillis();         
		long n = Long.parseLong(args[0]);         
		long total = 0;         
		for(long i=1; i<=n; i++){
			total = total + 1;
		}         
		System.out.println(total);
        System.out.println(System.currentTimeMillis() - time);
    }
}
```

Analysis suggests a runtime of $Time(n) = c_{1 }\cdot n + c_0$.


#### Quadratic Example

```java
for(long i=1; 1<=n; i++) {
	for(long j=1; j<=n; j++){
		total = total + 1;
	}
}
```

Here, the runtime is $Time(n) = (c2 * n + c1) * n + c0 = c2 * n^2 + c1 * n + c0$.

#### Cubic Example

```java
for(long i=1; i<=n; i++) {
	for(long j=1; j<=n; j++){
        for(long k=1; k<=n; k++){
            total = total + 1;
        }
    }
}
```

In this case, the runtime is $Time(n) = ((c3 * n + c2) * n + c1) * n + c0 = c3 * n^3 + c2 * n^2 + c1 * n + c0$.

The RAM model appears to predict the actual runtime well, at least for the tested examples.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}

\begin{tikzpicture}
\begin{axis}[
    title={Runtime Complexity Visualization},
    xlabel={$n$},
    ylabel={$T(n)$},
    legend pos=north west,
    grid=both,
    xmin=0, xmax=10,
    ymin=0, ymax=1000,
    domain=0:10,
    samples=100
]
    \addplot[blue, thick]       {x};        % Linear
    \addplot[orange, thick]     {x^2};      % Quadratic
    \addplot[red, thick]        {x^3};      % Cubic
    \legend{$T(n)=n$, $T(n)=n^2$, $T(n)=n^3$}
\end{axis}
\end{tikzpicture}

\end{document}
```
This graph gives a **visual** for how each algorithm's runtime increases with input size $n$:

- **Linear** grows slowly.
- **Quadratic** grows faster.
- **Cubic** quickly dominates as $n$ increases



### Multiplicative Constants

Multiplicative constants become irrelevant when growth rates differ. For example:

$f(n) = 3000n$ $h(n) = 3n^2$ $g(n) = 4000n$ $k(n) = 4n^2$

Even with larger constants, $c1 * n$ will always outperform $c2 * n^2$ as $n$ grows.

### Growth Rate

We aim to compare the _essential growth rate_ of functions in a way that ignores multiplicative constants. Such a comparison can be used to make a rough sorting of algorithms before implementation. If algorithm B will always lose to algorithm A for large $n$, regardless of multiplicative constants, there's little point in implementing algorithm B.

### Notation

> Asymptotic notation provides a way to compare functions' essential growth rates by disregarding multiplicative constants.

For a function $f(n)$, we consider all scalings of it ${c * f(n) | all c > 0}$ as equally good. This set of functions is referred to as $f(n)$'s _class_.

Based on this principle, five relations are defined for the growth rate of functions, corresponding to the five classical order relations: ≤, ≥, =, <, >. These are called $O, Ω, Θ, o, ω$, respectively, and are pronounced "O", "Omega", "Theta", "little o", and "little omega".

### Growth Rate Relationships

- **$f ≤ g$ in growth rate:** $f(n)$ grows at most as fast as functions from $g(n)$'s class.
- **$f ≥ g$ in growth rate:** $f(n)$ grows at least as fast as functions from $g(n)$'s class.
- **$f = g$ in growth rate:** $f(n)$ grows exactly as fast as functions from $g(n)$'s class.
- **$f < g$ in growth rate:** $f(n)$ grows slower than all functions from $g(n)$'s class.
- **$f > g$ in growth rate:** $f(n)$ grows faster than all functions from $g(n)$'s class.


### Practical Asymptotic Analysis

These definitions behave as expected of order relations:

- $f(n) = o(g(n)) ⇒ f(n) = O(g(n))$ (like $x < y ⇒ x ≤ y$)
- $f(n) = Θ(g(n)) ⇒ f(n) = O(g(n))$ (like $x = y ⇒ x ≤ y$)
- $f(n) = O(g(n)) ⇔ g(n) = Ω(f(n))$ (like $x ≤ y ⇔ y ≥ x$)
- $f(n) = o(g(n)) ⇔ g(n) = ω(f(n))$ (like $x < y ⇔ y > x$)
- $f(n) = O(g(n))$ and $f(n) = Ω(g(n)) ⇒ f(n) = Θ(g(n))$ (like $x ≤ y$ and $x ≥ y ⇒ x = y$)

The asymptotic relationships between most functions $f$ and $g$ can be clarified by the following theorems:

1. If $\frac{f(n)}{g(n)} → k > 0$ for $n → ∞$, then $f(n) = Θ(g(n))$.
2. If $\frac{f(n)}{g(n)} → 0$ for $n → ∞$, then $f(n) = o(g(n))$.
3. For all $a > 0$ and $b > 1$, $\frac{n^a}{b^n} → 0$ for $n → ∞$. Thus, any polynomial is $o()$ of any exponential function.
4. For all $a, d > 0$ and $c > 1$, $\frac{(log_c n)^a}{n^d} → 0$ for $n → ∞$. Thus, any logarithm (even raised to any power) is $o()$ of any polynomial.

### Examples of Function Growth Rates

With rules (1)–(4), it can be shown that the following functions are in increasing growth rate:

$1, \log{n}, \sqrt{n}, n, n log n, n\sqrt{n}, n^{2}, n^{3},  n^{10}, 2^{n}$

### Dominant Terms

For functions with multiple terms, the term(s) with the highest growth rate determine the overall growth rate.

![Dominant terms graph](https://api-turbo.ai/ed1448db-81f9-4b59-bc60-823f2609de5a.jpeg)

### ✍️ Examples of Asymptotic Analysis of Algorithms

#### Example 1

```
Algorithm1(n)
i = 1
while i ≤ n
    i = i + 2
```

The loop has $\lceil n/2\rceil = Θ(n)$ iterations. Each iteration takes between $c1$ and $c2$ time, so each iteration takes $Θ(1)$ time. Therefore, the runtime is $Θ(n * 1) = Θ(n)$.

#### Example 2

```
Algorithm2(n)
s = 0
for i = 1 to n
    for j = i downto 1
        s = s + 1
```

There are $n$ iterations of the outer loop. For each, there are at most $n$ iterations of the inner loop. Each iteration of the inner loop takes $Θ(1)$ time. So, the runtime is $O(n * n * 1) = O(n^2)$. The inner loop runs $(1 + 2 + 3 + ... + n) = (n + 1)n/2 = Θ(n^2)$ times.

#### Example 3

```
Algorithm3(n)
s = 0
for i = 1 to n
    for j = i to n
        for k = i to j
            s = s + 1
```

There are $n$ iterations of the outer loop. For each, there are at most $n$ iterations of the middle loop. For each of these, there are at most $n$ iterations of the inner loop. Each iteration of the inner loop takes $Θ(1)$ time. So, the runtime is $O(n * n * n * 1) = O(n^3)$.

### Working Principle

Compare growth rates of algorithms via asymptotic analysis, and normally only implement the one with the lowest growth rate. For two algorithms with the same growth rate, implement both and measure their runtimes.