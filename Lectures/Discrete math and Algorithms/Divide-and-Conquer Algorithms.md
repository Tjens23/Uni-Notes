Divide-and-Conquer is an algorithm design technique. It's essentially the same as **recursive algorithms**.

The main idea is:

1. **Divide** the problem into smaller subproblems of the same type.
2. **Solve** the subproblems recursively.
3. **Construct** a solution to the original problem from the solutions of the subproblems.


> Base cases, i.e. problems of size $O(1)$, are solved directly without recursion and are usually trivial.



### General Structure of Divide-and-Conquer Code

The general structure of Divide-and-Conquer code is as follows:

- If base case ($n=O(1)$):
    - Do work
- If not base case:
    
    - Do work
    - Recursive call
    - Do work
    - Recursive call
    - Do work

Note that some recursive algorithms may have only one recursive call, while others may have more than two.

### Divide-and-Conquer Examples

- **Mergesort**:
    - Divide input into two parts X and Y (trivial).
    - Sort each part recursively.
    - Merge the two sorted parts into one sorted part (real work).
    - Base case: $n\leq1$ (trivial).
- **Quicksort**:
    - Divide input into two parts X and Y such that $X \leq Y$ (real work).
    - Sort each part recursively.
    - Return X followed by Y (trivial).
    - Base case: $n\leq1$ (trivial).
- **Inorder traversal of a binary search tree**:
    - Two recursive calls on the right and left subtrees.
    - $O(1)$ work in between (printing the key in the current node).


### Flow of Control

When Divide-and-Conquer algorithms are executed, the flow of control can be visualized locally and globally.

###  Recursion Trees

The flow of control can be illustrated using **recursion trees**, where each node represents a call to the code. Base cases are leaves, and non-base cases are internal nodes. The tree's fanout (number of children) equals the number of recursive calls in the code.

At any given time, the total execution (the red path) reaches some node $v$. The call corresponding to $v$ is executing actions. All calls corresponding to nodes on the path from $v$ to the root are paused. Each call's state (variables, command reached, etc.) is stored on a stack by the computer to prevent mixing executions. Calls corresponding to other tree nodes are either complete or have not started.

- Calling a child in the recursion tree = push on stack.
- Finishing a node's execution = pop from stack.

###  Correctness of Divide-and-Conquer Algorithms

Correctness is argued from the bottom up in the recursion tree:

- Argue that base case calls are correct (usually trivial).
- For a non-base case call, argue that if the recursive calls are correct, then this, along with the local work, results in a correct answer for the current call.

In other words, correctness of calls with large inputs follows from correctness of calls with smaller inputs and the actions involved in constructing a solution for the large input from the solutions for the smaller inputs.

> Formally, correctness can be shown via induction on the input size. The base case for the recursion is the base case for the induction proof.

The specific argument is unique to each algorithm and is usually developed along with the algorithm.


### Recursion Equations

To analyze the execution times of recursive algorithms, we use recursion equations. Let $T(n)$
be the worst-case execution time on an input of size $n$.

f a recursive algorithm for problems of size nn makes aa recursive calls, each on subproblems of size $\frac{n}{b}$ and does $\theta(f(n))$ local work, then the following applies for the execution time $T(n)$

$$T(n) = \begin{cases} a \cdot T(n/b) + \Theta(f(n)) & \text{if } n > 1 \\ \Theta(1) & \text{if } n \leq 1 \end{cases}$$

The last line is often omitted, and it is usually understood that we use asymptotic notation (so we write $f(n)$ instead of $\theta(f(n))$ and 1 instead of $\theta(1)$

_Example_: Mergesort has two recursive calls of size $\frac{n}{2}$ and does $\theta(n)$ local work. Its recursion equation is therefore $T(n)=2\cdot T(\frac{n}{2})+n$

### Runtime of Divide-and-Conquer Algorithms

The total work of a recursive algorithm equals the sum of the local work in the algorithm's recursion tree. A recursion equation describes the structure of a recursive algorithm and provides a recursive description of its runtime (i.e., $T(n)$ is described based on $T$ for smaller input sizes)

However, we also want to find a direct expression (a function of $n$) for the algorithm's runtime $T(n)$.

### Recursion Tree Method

For a recursive algorithm (or a recursion equation):

1. Annotate the nodes in the recursion tree with:
    
    - Input size for the call to the node
    - Resulting work done in this node
2. Find the sum of the work in all nodes by:
    
    - First, find the tree's height (number of layers).
    - Sum each layer in the recursion tree separately.
    - Sum the resulting values for all layers.


### Examples of the Recursion Tree Method

#### Example 1

$$T(n)=2\cdot T (\frac{n}{2})+n$$

where

$$a=2,\quad b=2, \quad f(n) = n$$

| Step               | Description                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| 1. Draw the tree   | Tree with fanout $a = 2$.                                                                               |
| 2. Input sizes     | Insert input sizes in nodes (= $\frac{n}{b^{depth}}$).                                                  |
| 3. Find the height | Height: $\frac{n}{b^{height}} = 1 \leftrightarrow  b^{height} = n \leftrightarrow height = \log_{b}{n}$ |
| 4. Convert to work | Apply the function $f$ to convert input size to work.                                                   |
| 5. Sum each layer  | Sum each layer and express as a function of the layer number $i: 2^{i}\cdot \frac{n}{2^{i}}/ = n$.      |
| 6. Sum all layers  | Sum all layers to find total work: $n \log_{b} {n}$.                                                    |

#### Example 2
$$T(n)=3\cdot T(\frac{n}{2})+n$$
where

$$a=3,\quad b=2, \quad f(n) = n$$


|Step|Description|
|---|---|
|1. Draw the tree|Draw a tree with fanout $a = 3$.|
|2. Input sizes|Insert input sizes in nodes (= $n/b^{depth}$).|
|3. Find the height|Find the height based on $n/b^{height} = 1 \Leftrightarrow b^{height} = n \Leftrightarrow height = \log_b n$.|
|4. Convert to work|Apply the function $f$ to convert input size to work.|
|5. Sum each layer|Sum each layer and express as a function of the layer number $i$: $3^i \cdot n/2^i = n(3/2)^i$.|
|6. Sum all layers|The last layer dominates, so the total work is $\Theta(3^{\log_2 n}) = \Theta(n^{\log_2 3}) = \Theta(n^{1.5849...})$.|


#### Example 3

$$T(n)=3\cdot T(\frac{n}{4})+n^{2}$$
where

$$a=3,\quad b=4, \quad f(n) = n^{2}$$


| Step               | Description                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| 1. Draw the tree   | Draw a tree with fanout $a = 3$.                                                                              |
| 2. Input sizes     | Insert input sizes in nodes (= $n/b^{depth}$).                                                                |
| 3. Find the height | Find the height based on $n/b^{height} = 1 \Leftrightarrow b^{height} = n \Leftrightarrow height = \log_b n$. |
| 4. Convert to work | Apply the function $f$ to convert input size to work.                                                         |
| 5. Sum each layer  | Sum each layer and express as a function of the layer number $i$: $3^i \cdot (n/4^i)^2 = n^2(3/16)^i$.        |
| 6. Sum all layers  | The first layer dominates, so the total work is $\Theta(n^2)$.                                                |
### Mathematical Facts

> If the elements in a sum change exponentially, the whole sum is dominated by the largest term.

Exponentially growing/falling: largest term = last/first term.

For $c > 1$:

$$\frac{c^{k+1}-1}{c-1}=\frac{c}{c-1}\cdot c^{k}-\frac{1}{c-1}=\theta(c^{k})$$

where:
- The left side​ $\frac{c^{k+1}-1}{c-1}$ is the exact closed-form sum of the geometric series
- The middle expression shows this can be rewritten as $\frac{c}{c-1}\cdot c^{k}-\frac{1}{c-1}$
- Since $\frac{c}{c-1}$ is a constant when $c>1$, and $\frac{1}{c-1}$ becomes negligible compared to $c^{k}$  for large $k$, the dominant term is $c^{k}$, hence $\theta(c^{k})$



Example:

$$c=2$$

we have:

$$1+2+4+8+\dots+2^{k}$$


where the numbers:

- Level 0: 1 node doing work = $2^{0}=1$ unit of work
- Level 1: 2 nodes doing work = $2^{1}=2$ units of work
- Level 2: 4 nodes doing work  $2^{2}=4$ units of work
- Level 3: 8 nodes doing work $2^{3}=8$ units of work

apply formular:

$$\frac{c^{k}-1}{c-1}$$

so $1+2+4+8+\dots+2^{k}=\frac{2^{k-1}-1}{2-1}$



rewrite expression:

$$2^{k-1}-1=2\cdot2^{k}-1$$

Since $2\cdot 2^{k}$ grows exponentially the constant $-1$ becomes negligible compared to $2\cdot 2^{k}$, hence $\theta(2^{k})$


other facts:

- $(a^{b})^{c}=a^{bc}=(a^{c})^{b}$
- $a^{\log_{b}{n}}=n^{\log_{b}{a}}$
- $\log_{b}{a}=\frac{\log_{c}{a}}{\log_{c}{b}}$

The last fact can be used to calculate $\log_{b}{a}$ via a calculator (where the natural logarithm $\ln$ is available). It can also be written as $\log_{b}{x}=\frac{1}{\log_{c}{b}}\cdot\log_{c}{x}$ which shows that logarithms with different bases (here bb and cc) are a constant factor from each other:
$$\log_{b}{x}=\theta(\log_{c}{x})$$

### Divide-and-Conquer Examples

These three examples are representative, meaning one of the following often applies:

- All layers have approximately the same sum, so the total sum is the number of layers (tree height) times this sum.
- The layers' sum grows exponentially downward through the layers, so the bottom layer dominates. To find this layer's sum, you need to know the tree's height.
- The layers' sum decreases exponentially downward through the layers (= grows exponentially upward through the layers), so the top layer dominates.

###  Master Theorem

A generic solution for these three cases is in the book's theorem on pages 102–3 [3rd edition: page 94], called the Master Theorem. Most recursive algorithms are described by a recursion equation that fits into the Master Theorem. If it doesn't fit, one can try the recursion tree method directly.

The recursion equation $T(n)=a\cdot T(\frac{n}{b})+f(n)$ has the following solution where $\alpha = \log_{b}{a}$:

1. If $f(n) = O(n^{\alpha-\in})$ for some $\in > 0$, then $T(n) = \Theta(n^\alpha)$.
    
2. If $f(n) = \Theta(n^\alpha (\log n)^k)$ for some $k \geq 0$, then $T(n) = \Theta(n^\alpha (\log n)^{k+1})$.
    
3. If $f(n) = \Omega(n^{\alpha+\in})$ for some $\in > 0$, then $T(n) = \Theta(f(n))$.
    
    • **Extra condition:** In case 3, there must also exist a $c < 1$ and an $n_0$ such that $a \cdot f(n/b) \leq c \cdot f(n)$ when $n \geq n_0$.


In short: the case is determined by the relationship between the growth rates for $f(n)$ and for $n^a(\log n)^k$ (where $k \geq 0$). If they are equal, we have case 2. If $f(n)$ is smaller (by at least a factor of $n^c$), we have case 1. If $f(n)$ is larger (by at least a factor of $n^c$), we have case 3 (if the extra condition is met).


### Master Theorem Examples
#### Example 1

$$T(n)=2\cdot T(\frac{n}{2})+n$$
$$a=2, \quad b=2, \quad f(n)= n, \quad \alpha=\log_{2}{2}=1$$
$$f(n)=n=\theta(n^{1})= \theta(n^{\alpha}(\log_{2}{n})^{0})$$ 
So, we are in case 2, and $T(n)=\theta(n^{\alpha}(\log_{2}{n})^{0+1})=\theta(n\log{n})$

## Example 2

$$T(n) = 3T(n/2) + n$$

- $a = 3$
- $b = 2$
- $f(n) = n$
- $\alpha = \log_2 3 = \frac{\ln(3)}{\ln(2)} = 1.5849...$
- $f(n) = n = O(n^{1.5849...-\epsilon}) = O(n^{\alpha-\epsilon})$ for example $\epsilon = 0.1$

So, we are in case 1, and $T(n) = \Theta(n^\alpha) = \Theta(n^{1.5849...})$.

## Example 3

$$T(n) = 3T(n/4) + n^2$$

- $a = 3$
- $b = 4$
- $f(n) = n^2$
- $\alpha = \log_4 3 = \frac{\ln(3)}{\ln(4)} = 0.7924...$
- $f(n) = n^2 = \Omega(n^{0.7924...+\epsilon}) = \Omega(n^{\alpha+\epsilon})$ for example $\epsilon = 0.1$

So, we are in case 3, and $T(n) = \Theta(f(n)) = \Theta(n^2)$.

In case 3, we also need to check the extra condition: with $c = 3/16 < 1$ and $n_0 = 1$, we satisfy $a \cdot f(n/b) = 3(n/4)^2 = \frac{3}{16} \cdot n^2 \leq c \cdot f(n) = c \cdot n^2$ for all $n \geq n_0$.

## Example 4

$T(n) = 2T(n/2) + n \log n, a = 2, b = 2, f(x) = x \log x$

We have seen that the $ith layer in the recursion tree does $n \log(n/2^i)$ work, which can be written as $n(\log(n) - \log(2^i)) = n(\log(n) - i)$. This expression falls as $i$ rises, so all layers do at most the same work as the first layer ($i = 0$). The first layer does $n \log n$ work and there are $\log n$ layers in all, so the total work is $O(n \log^2 n)$.

We now look at the upper half of the layers, i.e. at layer $i$ for $i = 1, 2, ..., k = \frac{1}{2} \log n$.

The work for layer $i$ falls as $i$ rises, so each of these layers does at least the same work as the last of them (layer $k$). The work for layer $k$ is $n(\log(n) - k) = n(\log(n) - \frac{1}{2} \log n) = \frac{1}{2} n \log n$.

There are therefore $k = \frac{1}{2} \log n$ layers, which each do at least $\frac{1}{2} n \log n$ work. The total work is therefore $\Omega(n \log^2 n)$.

In total, we have shown that the total work is $\Theta(n \log^2 n)$.

$T(n) = 2T(n/2) + n \log n$

- $a = 2$
- $b = 2$
- $f(n) = n \log n$
- $\alpha = \log_2 2 = 1$
- $f(n) = n \log n = \Theta(n^1(\log n)^1) = \Theta(n^\alpha(\log n)^1)$ [i.e., $k = 1$]

So, we are in case 2, and $T(n) = \Theta(n^\alpha(\log n)^{1+1}) = \Theta(n(\log n)^2)$. [Note: $(\log n)^2$ is often written as $\log^2 n$.]

## Example 5

$T(n) = T(n/3) + T(2n/3) + n$

This recursion equation indicates the runtime for a recursive algorithm that does $O(n)$ local work and makes two recursive calls, one with size $n/3$ and one with size $2n/3$.

Unfortunately, this recursion equation is not of the type that the Master Theorem deals with. For those, all recursive calls must have the same size $(n/b)$:

$T(n) = aT(n/b) + f(n)$

We can therefore not use the Master Theorem.

We now show how we can still solve the recursion equation with the recursion tree method.

1. Draw a tree with fanout 2 (since there are two recursive calls).
    
2. Insert input sizes in nodes: multiply by 1/3 (one child) or 2/3 (the other child) when going downwards.
    
3. Find the longest and shortest path to a leaf:
    
    - $n(\frac{1}{3})^k = 1 \Leftrightarrow n = 3^k \Leftrightarrow \log_3 n = k$
    - $n(\frac{2}{3})^k = 1 \Leftrightarrow n = (\frac{3}{2})^k \Leftrightarrow \log_{3/2} n = k$
4. A node with input of size $x$ does $f(x) = x$ work. It has two children with inputs of size $x/3$ and $2x/3$, which therefore do $f(x/3) = x/3$ and $f(2x/3) = 2x/3$ work. Since $x/3 + 2x/3 = x$, we see that the node's work is equal to the sum of its children's work. It follows that the sum of work in layer $k$ is equal to the sum of the work in layer $k + 1$, if layer $k + 1$ is a full layer (all nodes in layer $k$ have two children). So all full layers have the same sum.
    
5. $1 \leq n \leq n \leq \cdots \leq n \leq n$
    

$\Theta(n \log n)$

Sum each layer and then sum all layers to find the total work. The answer is $\Theta(n \log n)$.

## Ceilings and Floors

Now, consider the recursion equation $T(n) = T(\lceil n/2 \rceil) + T(\lfloor n/2 \rfloor) + n$. Since $x - 1 < \lfloor x \rfloor \leq x \leq \lceil x \rceil < x + 1$, it follows that:

$n_0 = n n_1 \leq \lfloor n_0/2 \rfloor < n_0/2 + 1 = n/2 + 1 n_2 \leq \lfloor n_1/2 \rfloor < (n/2 + 1)/2 + 1 = n/2^2 + 1/2 + 1 n_3 \leq \lfloor n_2/2 \rfloor < (n/2^2 + 1/2 + 1)/2 + 1 = n/2^3 + 1/2^2 + 1/2 + 1 ... n_i < n/2^i + 1/2^{i-1} + ... + 1/2 + 1$

Similarly, it follows that: $n_0 = n n_1 \geq \lceil n_0/2 \rceil > n_0/2 - 1 = n/2 - 1 n_2 \geq \lceil n_1/2 \rceil > (n/2 - 1)/2 - 1 = n/2^2 - 1/2 - 1 n_3 \geq \lceil n_2/2 \rceil > (n/2^2 - 1/2 - 1)/2 - 1 = n/2^3 - 1/2^2 - 1/2 - 1 ... n_i > n/2^i - (1/2^{i-1} + ... + 1/2 + 1)$

## Impact on Recursion Trees

So, for the recursion equation $T(n) = T(\lceil n/2 \rceil) + T(\lfloor n/2 \rfloor) + n$, we've shown:

$n/2^i - (1/2^{i-1} + ... + 1/2 + 1) < n_i < n/2^i + (1/2^{i-1} + ... + 1/2 + 1)$

The expression in the parenthesis is equal to $1 + c + c^2 + ... + c^{i-1}$ for $c = 1/2$, and is therefore equal to:

$\frac{(1/2)^i - 1}{1/2 - 1} = \frac{1 - (1/2)^i}{1/2} = 2 - (1/2)^{i-1} < 2$

For the recursion equation $T(n) = 2T(n/2) + n$, we showed $n_i = n/2^i$.

In the two recursion trees for:

$T(n) = T(\lceil n/2 \rceil) + T(\lfloor n/2 \rfloor) + n T(n) = 2T(n/2) + n$

The input sizes $n_i$ in the nodes on an arbitrary layer $i$ only differ by plus/minus 2.

For all the functions $f$ we encounter, $f(n + 2) = O(f(n))$. For such functions, we obtain the same asymptotic running time whether we analyze recursive equations with or without floors/ceilings.

- For $f(n) = n$, $f(n + 2) = n + 2 = O(n) = O(f(n))$.
- For $f(n) = n^2$, $f(n + 2) = (n + 2)^2 = n^2 + 4n + 4 = O(n^2) = O(f(n))$.
- For $f(n) = \log(n)$, $f(n + 2) = \log(n + 2) <= \log(2n) = 1 + \log(n) = O(\log(n)) = O(f(n))$.
- For $f(n) = 2^n$, $f(n + 2) = 2^{n+2} = 4 \cdot 2^n = O(2^n) = O(f(n))$.



# 🎲 Analyzing the Work in Root Layers

For the root layer, the sum of the work is clearly $n$. Therefore, for all full layers, the sum of the work in the layer equals $n$. With $\log(n)$ full layers, the total work is $\Theta(n\log(n))$.

For non-full layers, the sum can only be smaller (leaves have no children, so their input size isn't passed to the next layer), meaning at most $n$. There are at most $\log(n)$ layers in total (full and non-full), so the total work is $O(n\log(n))$.

All in all, the total work is $\Theta(n\log(n))$. Note that logarithms with different bases only differ by a constant factor.

## 🧮 Floors and Ceilings in Recursive Equations

A detail that often gets overlooked involves floors and ceilings in recursive equations. Mergesort serves as a good example. The recursion equation for Mergesort is typically written as:

$$T(n) = 2T(n/2) + n$$

However, when $n$ is odd, the two recursive calls can't be exactly the same size. Thus, the recursion equation should actually be:

$$T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + n$$

Does this difference significantly impact the runtime calculation? No, it does not.

## 🌳 Floors and Ceilings in Recursive Equations

Consider a path down through the recursion tree, where $n_i$ denotes the size of the input at layer $i$ (with the root layer set to number 0).

For the recursion equation $T(n) = 2T(n/2) + n$:

$$n_0 = n \quad n_1 = n_0/2 = n/2 \quad n_2 = n_1/2 = (n/2)/2 = n/2^2 \quad n_3 = n_2/2 = (n/2^2)/2 = n/2^3 \quad \ldots \quad n_i = n/2^i$$

