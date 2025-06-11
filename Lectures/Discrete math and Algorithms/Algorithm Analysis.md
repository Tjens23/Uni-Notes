# Algorithm Analysis

In this course, we will focus on:

```
Describing existing algorithms
Developing new algorithms
Evaluating/analyzing algorithms
```
When analyzing an algorithm, we should focus on the following qualities:

```
Correctness:
```
```
Stops for all inputs (never an infinite loop).
Gives correct output when it stops.
```
```
Speed
```
```
Space Usage
```
```
Implementation Complexity
```
```
Extra Properties (problem-specific)
```
# Ingredients of Algorithm Analysis

We need the following to analyze algorithms:

```
Model of problem: Individual for each problem (but often straightforward).
Model of machine: We use the RAM-model.
Measure for quality: We focus on time consumption.
Mathematical tools: Asymptotic notation, invariants, induction, recursion
equations.
```
# RAM Model

```
A memory: A large array of cells, each with space for a number or a character.
(list/array = many neighboring cells)
A CPU with a number of basic operations:
plus, minus, times, compare, ... two cells' contents
move contents between two cells
jump in program (loop, branch, function/method call).
```

All basic operations are assumed to take the same time.

```
Time for an algorithm: number of basic operations performed.
Space for an algorithm: maximum number of occupied memory cells.
```
# Measuring Time Consumption: Input

# Considerations

For a given size of input, there are often many different concrete inputs.

Example:

Sorting = arrange elements in ascending order

For , the following lists are four out of many possible inputs:

```
7 , 2 , 3 , 1 , 8 , 5 , 4 , 6
1 , 8 , 2 , 7 , 3 , 6 , 4 , 5
1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
8 , 7 , 6 , 5 , 4 , 3 , 2 , 1
```
An algorithm usually has different time consumption on each of these.

Which input should we use to assess time consumption?

```
Worst case (max over all inputs of size )
Average case (average over a distribution of inputs of size )
Best case (min over all inputs of size )
```
# Worst Case Time Consumption

```
Worst case gives a guarantee.
Is often representative of average case (but can also be more pessimistic).
Average case: Which distribution of inputs? Why is this distribution
realistic/relevant? Analysis is often (mathematically) difficult to carry out.
Best case: Often does not provide much relevant information.
```
Almost all analyses in this course are worst case.

Worst-case running time is normally an increasing function of the input size :

# Growth Rate

```
n
```
```
n
```
```
n = 8
```
```
n
n
n
```
```
n
```

An analysis must therefore give a function of the input size.

To compare the running time of algorithms, we, therefore, need to compare functions.
More precisely, we want to investigate how two functions and grow when
increases.

Specifically, we would like to be able to recognize if, for example, will always
exceed when becomes large enough. We then say that has a greater
growth rate than , and we would normally prefer the algorithm with running
time.

For small , (almost) all algorithms are fast, so it is the running time for large that
is interesting.

Examples of functions listed in increasing growth rate:

```
, , , , , , , ,
```
These have quite different efficiencies in practice:

```
1 minute
1 month
```
The table shows which input sizes you can handle if the algorithm must perform
CPU operations, and it must be completed after one minute and one month,
respectively. It is assumed that a CPU can perform operations per second.

# Asymptotic Growth Rate

Later, we will make a formal definition of the concept of asymptotic growth rate for
functions. This will be our tool for comparing the running times of algorithms.

```
f ( n ) n
```
_f_ ( _n_ ) _g_ ( _n_ )
_n_

```
g ( n )
f ( n ) n g ( n )
f ( n )
f ( n )
```
```
n n
```
√ 1 _logn n nlogn n_ √ _n n_^2 _n_^3 _n_^102 _n_

```
n nlogn n^2 n^3 n^102 n
6. 0 ∗ 1010 1. 9 ∗ 109 245 , 000 3 , 910 12 36
7. 6 ∗ 1015 5. 7 ∗ 103 50 , 900000 13700 35 51
```
_n
f_ ( _n_ )
109


