
## Contents:

- Describing existing algorithms
- Developing new algorithms
- Evaluating/analyzing algorithms

When analyzing an algorithm, we should focus on the following qualities:

- Correctness:
	- Stops for all inputs (never an infinite loop).
	- Gives correct output when it stops.
- speed
- space of usage
- implementation complexity
- **Extra Properties** (problem-specific)


# Ingredients of Algorithm Analysis

We need the following to analyze algorithms:

- Model of problem: Individual for each problem (but often straightforward).
- Model of machine: We use the RAM-model.
- Measure for quality: We focus on time consumption.
- Mathematical tools: Asymptotic notation, invariants, induction, recursion equations.


# RAM Model

- A memory: A large array of cells, each with space for a number or a character. (list/array = many neighboring cells)
- A CPU with a number of basic operations:
    - plus, minus, times, compare, ... two cells' contents
    - move contents between two cells
    - jump in program (loop, branch, function/method call).

All basic operations are assumed to take the same time.
- Time for an algorithm: number of basic operations performed.
- Space for an algorithm: maximum number of occupied memory cells.

# Measuring Time Consumption: Input
For a given size $n$ of input, there are often many different concrete inputs.

## Example: 

Sorting = arrange elements in ascending order

For $n=8$, the following lists are four out of many possible inputs:

- 7,2,3,1,8,5,4,6
- 1,8,2,7,3,6,4,5
- 1,2,3,4,5,6,7,8
- 8,7,6,5,4,3,2,1

An algorithm usually has different time consumption on each of these.

Which input should we use to assess time consumption?
- Worst case (max over all inputs of size )
- Average case (average over a distribution of inputs of size )
- Best case (min over all inputs of size )


# Worst Case Time Consumption

- Worst case gives a **guarantee**.
- Is often representative of average case (but can also be more pessimistic).
- Average case: Which distribution of inputs? Why is this distribution realistic/relevant? Analysis is often (mathematically) difficult to carry out.
- Best case: Often does not provide much relevant information.


Almost all analyses in this course are worst case.

Worst-case running time is normally an increasing function of the input size :

# Growth Rate

An analysis must therefore give a function $f(n)$ of the input size $n$.
To compare the running time of algorithms, we, therefore, need to compare functions. More precisely, we want to investigate how two functions $f(n)$ and $g(n)$ grow when $n$ increases.

Specifically, we would like to be able to recognize if, for example, $g(n)$ will always exceed $f(n)$ when $n$ becomes large enough. We then say that g(n)g(n) has a greater growth rate than $f(n)$, and we would normally prefer the algorithm with running time $f(n)$.

For small $n$, (almost) all algorithms are fast, so it is the running time for large $n$ that is interesting.

Examples of functions listed in increasing growth rate:


$$\sqrt{1}, \log{n}, n, n\log{n}, n\sqrt{n}, n^2, n^3, n^{10}, 2^n$$

These have quite different efficiencies in practice:

| Time     | $n$                  | $n\log n$            | $n^2$        | $n^3$    | $n^{10}$ | $2^n$ |
| -------- | -------------------- | -------------------- | ------------ | -------- | -------- | ----- |
| 1 minute | $6.0 \times 10^{10}$ | $1.9 \times 10^9$    | $245,000$    | $3,910$  | $12$     | $36$  |
| 1 month  | $2.6 \times 10^{15}$ | $5.7 \times 10^{13}$ | $50,900,000$ | $13,700$ | $35$     | $51$  |

The table shows which input sizes $n$ you can handle if the algorithm must perform $f(n)$ CPU operations, and it must be completed after one minute and one month, respectively. It is assumed that a CPU can perform $10^{9}$ operations per second.


```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}

% Plot for 1 Minute
\begin{tikzpicture}
\begin{axis}[
    title={1 Minute Time Limit},
    ybar,
    bar width=10pt,
    ymin=1,
    ymode=log,
    ylabel={Max Input Size $n$},
    symbolic x coords={$n$, $n\log n$, $n^2$, $n^3$, $n^{10}$, $2^n$},
    xtick=data,
    x tick label style={rotate=45, anchor=east},
    width=7cm,
    height=8cm,
    grid=both,
    yticklabel style={/pgf/number format/fixed}
]
\addplot coordinates {
    ($n$, 6.0e10)
    ($n\log n$, 1.9e9)
    ($n^2$, 2.45e5)
    ($n^3$, 3910)
    ($n^{10}$, 12)
    ($2^n$, 36)
};
\end{axis}
\end{tikzpicture}

\vspace{1cm}

% Plot for 1 Month
\begin{tikzpicture}
\begin{axis}[
    title={1 Month Time Limit},
    ybar,
    bar width=10pt,
    ymin=1,
    ymode=log,
    ylabel={Max Input Size $n$},
    symbolic x coords={$n$, $n\log n$, $n^2$, $n^3$, $n^{10}$, $2^n$},
    xtick=data,
    x tick label style={rotate=45, anchor=east},
    width=7cm,
    height=8cm,
    grid=both,
    yticklabel style={/pgf/number format/fixed}
]
\addplot coordinates {
    ($n$, 2.6e15)
    ($n\log n$, 5.7e13)
    ($n^2$, 5.09e7)
    ($n^3$, 13700)
    ($n^{10}$, 35)
    ($2^n$, 51)
};
\end{axis}
\end{tikzpicture}

\end{document}
```


