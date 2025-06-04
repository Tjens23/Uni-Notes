---
tags:
  - Notes
links: "[[AI Lecture 10]]"
creation date: 2025-05-29 17:05
modification date: Thursday 29th May 2025 17:05:55
semester: 4
year: 2025
---


---
# [[AI Lecture 10 Notes]]

---



## 🗣️ The Noisy Channel Model

The goal is to search through the space of all possible sentences and pick the one that is most probable given the waveform. The problem can be defined as finding the most likely sentence `W` out of all sentences in the language `L` given some acoustic input `O`.

- Treat acoustic input `O` as a sequence of individual observations: `O = o1, o2, o3, ..., ot`
- Define a sentence as a sequence of words: `W = w1, w2, w3, ..., wn`

Probabilistic implication involves picking the highest probable `W`:

$\hat{W} = \arg\max_{W \in L} P(W|O)$

Using Bayes' rule, this can be rewritten as:

$\hat{W} = \arg\max_{W \in L} \frac{P(O|W)P(W)}{P(O)}$

Since the denominator is the same for each candidate sentence `W`, it can be ignored for the `argmax`:

$\hat{W} = \arg\max_{W \in L} P(O|W)P(W)$

## 🤖 Toward Hidden Markov Models (HMMs)

### Weighted Finite-State Automaton (WFSA)

> An FSA with probabilities on the arcs. The sum of the probabilities leaving any arc must sum to one.

Every Markov chain (or observable Markov Model) is a WFSA.

### Markov Chain

> A model comprised of a set of states, transition probabilities, a start state, and an end state. The current state only depends on the previous state.

A Markov chain is also referred to as a "First-order observable Markov Model". Andrey Markov was a Russian mathematician known for his work on stochastic processes.

#### Key Components

- A set of states: $Q = q_1, q_2, ... q_N$; the state at time `t` is $q_t$
- Transition probabilities: $A = a_{01}, a_{02} ... a_{ij} ... a_{NN}$
    - Each $a_{ij}$ represents the probability of transitioning from state `i` to state `j`
    - The set of these is the **transition probability matrix** `A`
    - $a_{ij} = P(q_t = j | q_{t-1} = i) \quad 1 \leq i,j \leq N$
    - $\sum_{j=1}^N a_{ij} = 1; \quad 1 \leq i \leq N$
- Distinguished start and end states

#### Markov Assumption

$P(q_i | q_1...q_{i-1}) = P(q_i | q_{i-1})$

The current state only depends on the previous state.

#### Initial Probability Vector

Instead of start state π, there is a special initial probability vector:

$\pi = P(q_1 = i) \quad 1 \leq i \leq N$

Constraint:

$\sum_{j=1}^N \pi_j = 1$

#### Example: Markov Chain for Weather

Consider the probability of 4 consecutive warm days. The sequence is warm-warm-warm-warm, i.e., the state sequence is 3-3-3-3. $P(3,3,3,3) = \pi_3 \cdot a_{33} \cdot a_{33} \cdot a_{33} = 0.2 \cdot (0.6)^3 = 0.0432$ The difference in probabilities between sequences like "hot hot hot hot" and "cold hot cold hot" tells you about the real-world weather information encoded in the figure.

## 🍦 HMM for Ice Cream

Imagine being a climatologist in the year 2799 studying global warming and discovering Jason Eisner’s diary, which lists how many ice creams Jason ate every day in the summer of 2008 in Baltimore, MD. The goal is to figure out how hot it was each day that summer.

## 💡 Hidden Markov Model

For Markov chains, output symbols = states. In many Natural Language Processing tasks, the interesting states are hidden.

> A Hidden Markov Model (HMM) is an extension of a Markov chain in which the input symbols are not the same as the states.

### Assumptions

- **Markov Assumption**: $P(q_i | q_1...q_{i-1}) = P(q_i | q_{i-1})$
- **Output-Independence Assumption**

### Eisner Task Example

- Given: Ice Cream Observation Sequence: 1, 2, 3, 2, 2, 2, 3…
- Produce: Weather Sequence: H, C, H, H, H, C…

## 🤔 The Three Basic Problems for HMMs

Jack Ferguson at IDA in the 1960s defined the three basic problems for HMMs:

| Problem    | Description                                                                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluation | Given the observation sequence $O=(o_1 o_2...o_T)$, and an HMM model $\Phi=(A,B)$, how do we efficiently compute $P(O\|\Phi)$                                           |
| Decoding   | Given the observation sequence $O=(o_1 o_2...o_T)$, and an HMM model $\Phi=(A,B)$, how do we choose a corresponding state sequence $Q=(q_1 q_2...q_T)$ that is optimal? |
| Learning   | How do we adjust the model parameters $\Phi=(A,B)$ to maximize $P(O\|\Phi)$                                                                                             |

### Problem 1: Computing the Observation Likelihood

Given an HMM, how likely is the sequence 3 1 3?

For a Markov chain, we just follow the states 3 1 3 and multiply the probabilities. But for an HMM, we don’t know what the states are! Start with a simpler situation by computing the observation likelihood for a given hidden state sequence.

Suppose we knew the weather and wanted to predict how much ice cream Jason would eat, i.e., $P(3\ 1\ 3 | H\ H\ C)$.

#### Computing Likelihood of 3 1 3 Given Hidden State Sequence

This involves computing the joint probability of observation and state sequence.

#### Computing Total Likelihood of 3 1 3

We would need to sum over all possible hidden state sequences (e.g., Hot hot cold, Hot hot hot, Hot cold hot, ...). How many possible hidden state sequences are there for this sequence?

In general, for an HMM with N hidden states and a sequence of T observations, there are NTNT possible hidden state sequences. Therefore, we can’t just do separate computation for each hidden state sequence.

### The Forward Algorithm

> A kind of dynamic programming algorithm that uses a table to store intermediate values. It computes the likelihood of the observation sequence by summing over all possible hidden state sequences efficiently by folding all the sequences into a single trellis.

The goal is to compute $P(o_1, o_2, ..., o_T, q_T = q_i | \lambda)$ by recursion.

Each cell of the forward algorithm trellis $\alpha_t(j)$ represents the probability of being in state `j` after seeing the first `t` observations, given the automaton. Each cell thus expresses the following probability.
#### The Forward Recursion

We update each cell by computing the forward probability.

### Problem 2: Decoding

Given an observation sequence (e.g., 3 1 3) and an HMM, the task of the decoder is to find the best hidden state sequence.

Given the observation sequence $O=(o_1 o_2...o_T)$, and an HMM model $\Phi=(A,B)$, how do we choose a corresponding state sequence $Q=(q_1 q_2...q_T)$ that is optimal?

One possibility is to compute $P(O|Q)$ for each hidden state sequence $Q$ (e.g., HHH, HHC, HCH,…) and pick the highest one. But this is not efficient because it requires $N^T$ computations.

#### The Viterbi Algorithm

> A dynamic programming algorithm that uses a similar trellis to the Forward algorithm.

It computes the joint probability of the observation sequence together with the best state sequence:

$\max_{q_0, q_1, ..., q_T} P(q_0, q_1, ..., q_T, o_1, o_2, ..., o_T, q_T = q_i | \lambda)$

#### Viterbi Intuition

The algorithm processes the observation sequence from left to right, filling out the trellis. Each cell contains the probability of the most likely path that ends in that cell.

#### Viterbi Recursion

[Viterbi Recursion](https://www.geeksforgeeks.org/viterbi-algorithm-for-hidden-markov-models-hmms/)

#### Viterbi Backtrace

By tracing back through the trellis from the end, the algorithm can determine the most likely sequence of hidden states.