---
tags:
  - Notes
links: "[[AI Lecture 9]]"
creation date: 2025-05-24 14:03
modification date: Saturday 24th May 2025 14:07:04
semester: 4
year: 2025
---


---
# [[AI Lecture 9 Notes]]

---



## 🧠 Bayesian Networks

### Introduction

Imagine you're a doctor trying to figure out if a patient has inhalational anthrax. You see they have a cough, fever, and difficulty breathing. It's not a sure thing, so you're dealing with **uncertainty**. Now, you order an X-ray and see a wide mediastinum. Suddenly, you're much more convinced it's anthrax.

That's the basic idea behind Bayesian Networks: using observations to update beliefs in uncertain situations.

In the opinion of many AI researchers, Bayesian networks are one of the most significant contribution in AI in the last 20-40 years.

They are used in many applications, e.g., spamfiltering, speech recognition, robotics, diagnostic systems and even syndromic surveillance.

## 🎲 Probability Review: Random Variables

> A **random variable** is the basic element of probability. Refers to an event, and there is some degree of uncertainty as to the outcome of the event

For example, the random variable A could be the event of getting heads on a coin flip.

### Boolean Random Variables

The simplest type of random variables are **Boolean random variables.**

- Take the values true or false
- Think of the event as occurring or not occurring
- Examples:
    - A = Getting heads on a coin flip
    - A = It will rain today
    - A = Denmark wins the World Cup in 2026

### The Problem with the Joint Distribution

Joint distributions quickly become unwieldy. For $k$ Boolean random variables, you need a table of size $2^k$. We need ways to use fewer numbers.

## 🕸️ What is a Bayesian Network?

A Bayesian network consists of two key components:

1. A **Directed Acyclic Graph (DAG)**
2. A set of **tables** for each node in the graph

### Directed Acyclic Graph (DAG)

Each node in the graph is a **random variable**.

> A node X is a parent of another node Y if there is an arrow from node X to node Y.

Informally, an arrow from node X to node Y means X has a direct influence on Y.

### Tables for Each Node

Each node $X$ has a **conditional probability distribution** $P(X | \text{Parents}(X))$ that quantifies the effect of the parents on the node.

The parameters are the probabilities in these conditional probability tables (CPTs).

For a given combination of values of the parents (B in this example), the entries for $P(C=\text{true} | B)$ and $P(C=\text{false} | B)$ must add up to 1.

If you have a Boolean variable with _k_ Boolean parents, this table has $2^{k+1}$ probabilities.

Hence, it is enough to know about one of them:

$P(C=\text{false} | B=\text{false}) = 0.4$

Then we can calculate the other one:

$P(C=\text{true} | B=\text{false}) = 1 - 0.4 = 0.6$

## ✨ Properties of Bayesian Networks

1. **Encodes conditional independence relationships**: Shows how variables relate to each other.
2. **Compact representation**: Efficient way to represent joint probability distributions.

### Conditional Independence

**Markov Condition:** Given its parents $(P_1, P_2)$, a node $(X)$ is conditionally independent of its non-descendants $(ND_1, ND_2)$. 

$P(X | P_1, P_2, ND_1, ND_2) = P(X | P_1, P_2)$

### Examples of Conditional Independence

#### Example 1

A is the height of a child and B is the number of words that the child knows. 
- When A is high, B is high too.  
A single piece of information will make A and B completely independent. 
- The child's age.  
The height and the # of words known by the kid are NOT independent, but they are conditionally independent if the kid's age is provided: 

$P(A, B) \neq P(A)P(B)$ but $P(A, B | \text{Age}) = P(A | \text{Age})P(B | \text{Age})$

#### Example 2

- Weather is independent of the other variables
- Toothache and Catch are conditionally independent given Cavity

### The Joint Probability Distribution

Due to the Markov condition, we can compute the joint probability distribution over all the variables $X_1, \ldots, X_n$​ in the Bayesian net using the formula:

$$P(X_1 = x_1, \ldots, X_n = x_n) = \prod_{i=1}^n P(X_i = x_i | \text{Parents}(X_i))$$

Where $\text{Parents}(X_i)$ means the values of the Parents of the node $X_i$​ with respect to the graph.

### Example Calculation

Suppose you want to calculate:

$$\begin{align} P(A=\text{true}, B=\text{true}, C=\text{true}, D=\text{true}) &= P(A=\text{true}) \cdot P(B=\text{true} | A=\text{true}) \\ &\quad \cdot P(C=\text{true} | B=\text{true}) \cdot P(D=\text{true} | B=\text{true}) \\ &= (0.4) \cdot (0.3) \cdot (0.1) \cdot (0.95) \end{align}$$

## 🔎 Inference

> Using a Bayesian network to compute probabilities is called **inference**

In general, inference involves queries of the form: $P(X | E)$

- $E$ = The evidence variable(s)
- $X$ = The query variable(s)

An example of a query would be:

$P(\text{HasAnthrax}=\text{true} | \text{HasFever}=\text{true}, \text{HasCough}=\text{true})$

> Note: Even though HasDifficultyBreathing and HasWideMediastinum are in the Bayesian network, they are not given values in the query (i.e. they do not appear either as query variables or evidence variables)

They are treated as unobserved variables

## 🛠️ Making a Bayes Net

1. **Add variables**: Choose the variables you'd like to be included in the net. 
2. **Add links**: The link structure must be acyclic (no cycles are allowed). 
	- If node X is given parents $Q_1, Q_2, \ldots, Q_n$ you are promising that any variable that's a non-descendent of X is conditionally independent of X given $\{Q_1, Q_2, \ldots, Q_n\}$ 
3. **Add a probability table for each node**: The table for node X must list $P(X | \text{Parent Values})$ for each possible combination of parent values`

Two unconnected variables may still be correlated

Each node is conditionally independent of all non-descendants in the tree, given its parents.

You can deduce many other conditional independence relations from a Bayes net.

## 📝 Bayes Nets Formalized

A Bayes net (also called a belief network) is an augmented directed acyclic graph, represented by the pair (V,E)(V,E) where:

- $V$ is a set of vertices.
- $E$ is a set of directed edges joining vertices. No loops of any length are allowed.

Each vertex in V contains the following information:

- The name of a random variable
- A probability distribution table indicating how the probability of this variable’s values depends on all possible combinations of parental values.

## 🏗️ Building a Bayes Net

1. Choose a set of relevant variables and an ordering for them. 
2. Assume they're called $X_1, \ldots, X_m$ (where $X_1$ is the first in the ordering, $X_2$ is the second, etc.) 
3. For $i = 1$ to $m$: 
	1. Add the $X_i$ node to the network 
	2. Set $\text{Parents}(X_i)$ to be a minimal subset of $\{X_1 \ldots X_{i-1}\}$ such that we have conditional independence of $X_i$ and all other members of $\{X_1 \ldots X_{i-1}\}$ given $\text{Parents}(X_i)$ 
	3. Define the probability table of $P(X_i = k | \text{Assignments of Parents}(X_i))$.

## ☢️ Example Bayes Net Building

Suppose we’re building a nuclear power station.

There are the following random variables:

- GRL: Gauge reads low
- CTL: Core temperature is low
- FG: Gauge is faulty
- FA: Alarm is faulty
- AS: Alarm sound

If the alarm is working properly, the alarm is meant to sound if the gauge stops reading a low temp.

If the gauge is working properly, the gauge is meant to read the temp of the core.

## 🧮 Computing a Joint Entry

$$
\text{How to compute an entry in a joint distribution?}
$$

$$
\text{E.g.: What is } P(S \land \sim M \land L \land \sim R \land T)?
$$

$$
P(S \land \sim M \land L \land \sim R \land T) = P(T \land \sim R \land L \land \sim M \land S)
$$

$$
\begin{aligned}
= &\; P(T \mid \sim R \land L \land \sim M \land S) \cdot P(\sim R \land L \land \sim M \land S) \\
= &\; P(T \mid L) \cdot P(\sim R \land L \land \sim M \land S) \\
= &\; P(T \mid L) \cdot P(\sim R \mid L \land \sim M \land S) \cdot P(L \land \sim M \land S) \\
= &\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \land \sim M \land S) \\
= &\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M \land S) \\
= &\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M \mid S) \cdot P(S) \\
= &\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M) \cdot P(S)
\end{aligned}
$$


### Computing with Bayes Net

We can get this directly from the structure

$$
\begin{aligned}
P(T \land \sim R \land L \land \sim M \land S)
=&\; P(T \mid \sim R \land L \land \sim M \land S) \cdot P(\sim R \land L \land \sim M \land S) \\
=&\; P(T \mid L) \cdot P(\sim R \land L \land \sim M \land S) \\
=&\; P(T \mid L) \cdot P(\sim R \mid L \land \sim M \land S) \cdot P(L \land \sim M \land S) \\
=&\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \land \sim M \land S) \\
=&\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M \land S) \\
=&\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M \mid S) \cdot P(S) \\
=&\; P(T \mid L) \cdot P(\sim R \mid \sim M) \cdot P(L \mid \sim M \land S) \cdot P(\sim M) \cdot P(S)
\end{aligned}
$$


### The General Case

$\begin{align} P(X_1 = x_1 \land X_2 = x_2 \land \ldots \land X_n = x_n) &= \\ P(X_n = x_n \mid X_{n-1} = x_{n-1}, \ldots, X_1 = x_1) &\cdot \\ P(X_{n-1} = x_{n-1} \mid X_{n-2} = x_{n-2}, \ldots, X_1 = x_1) &\cdot \\ &\vdots \\ P(X_2 = x_2 \mid X_1 = x_1) \cdot P(X_1 = x_1) \\ &= \prod_{i=1}^{n} P(X_i = x_i \mid X_1 = x_1, \ldots, X_{i-1} = x_{i-1}) \\ &= \prod_{i=1}^{n} P(X_i = x_i \mid \text{Parents}(X_i)) \end{align}$`
 
 So any entry in the joint pdf table can be computed. And so any conditional probability can be computed.`

## ✅ What We've Achieved

- We have a methodology for building Bayes nets.
- No exponential storage to hold our probability table. Only exponential in the maximum number of parents of any node.
- We can compute probabilities in time linear with the number of nodes.
- So we can also compute answers to any question.

E.G. What could we do to compute $P(R | T, \sim S)$?

1. Compute $P(R \land T \land \sim S)$ 
2. Compute $P(\sim R \land T \land \sim S)$
3. Return $\frac{P(R \land T \land \sim S)}{P(R \land T \land \sim S) + P(\sim R \land T \land \sim S)}$`

### Step 1: Compute $P(R \land T \land \sim S)$`

Sum of all the rows in the Joint that match $R \land T \land \sim S$

### Step 2: Compute $P(\sim R \land T \land \sim S)$

Sum of all the rows in the Joint that match $\sim R \land T \land \sim S$

### Step 3: Return

$$\frac{P(R \land T \land \sim S)}{P(R \land T \land \sim S) + P(\sim R \land T \land \sim S)}$$

4 joint computes

## 🎉 The Good News

We can do inference. We can compute any conditional probability: $P(\text{Some variable} | \text{Some other variable values})$ $$P(E_1 | E_2) = \frac{P(E_1 \land E_2)}{\sum_{\text{joint entries matching } E_2} P(\text{joint entry})} = \frac{\sum_{\text{joint entries matching } E_1 \text{ and } E_2} P(\text{joint entry})}{\sum_{\text{joint entries matching } E_2} P(\text{joint entry})}$$ Suppose you have $m$ binary-valued variables in your Bayes Net and expression E mentions k variables. How much work is the above computation?

## 😞 The Sad, Bad News

Conditional probabilities by enumerating all matching entries in the joint are expensive:

Exponential in the number of variables.

But perhaps there are faster ways of querying Bayes nets?

- If ever asked to manually do a Bayes Net inference -> many tricks to save you time -> not topic of this class though 

### Even Worse News

General querying of Bayes nets is NP-complete.

## 📉 Summary of the Bad News

- Exact inference is feasible in small to medium-sized networks
- Exact inference in large networks takes a very long time
- We resort to approximate inference techniques which are much faster and give pretty good results

## 🤔 One Last Unresolved Issue

Where do we get the Bayesian network from?

Two options:

- Get an expert to design it
- Learn it from data
- More examples and tutorials: 
	- https://www.bayesserver.com/examples/
	- https://www.bnlearn.com/
	- https://dsaldana.github.io/sallybn/doc/tutorial/tutorial.html


## Example: Alarm Network
