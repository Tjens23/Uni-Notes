---
tags:
  - Notes
links: "[[AI Lecture 9]]"
creation date: 2025-05-21 14:10
modification date: Wednesday 21st May 2025 14:10:56
semester: 4
year: 2025
---


---
# [[AI Lecture 8 Notes]]

---



## 🎯 Uncertainty

**Uncertainty** arises due to:

- **Partial observability:** Difficulty in fully assessing the current state (e.g., road conditions, other drivers' intentions).
- **Uncertainty in action outcomes:** Unpredictable events that may occur (e.g., flat tire).
- **Complexity of modeling and predicting traffic:** The sheer difficulty in accurately forecasting traffic conditions.

A purely logical approach:

- Risks falsehood or
- Leads to conclusions too weak for decision-making.

**Probabilistic assertions** summarize effects of:

- **Laziness:** Failure to enumerate exceptions, qualifications, etc.
- **Ignorance:** Lack of explicit theories, relevant facts, initial conditions, etc.
- **Intrinsically random behavior**

## 🤔 Making Decisions Under Uncertainty

To make decisions under uncertainty, an agent should consider:

- **Probabilities** of different outcomes.
- **Preferences** for different outcomes, which can be encapsulated by a **utility function**.

The agent should choose the action that maximizes the **expected utility**:

$$P(A_{t}\quad\text{succeeds}) \times U(A_t\quad\text{succeeds})+P(A_{t}\quad \text{fails})\times U(A_{t} \quad \text{fails})$$

Here, $A_t$ represents an action taken at time $t$, $U$ is the utility function, and $P$ denotes probability.

- **Utility theory** represents and infers preferences.
- **Decision theory** combines probability theory and utility theory.

## 🚪 Monty Hall Problem

Here's a summary of the Monty Hall problem:

- There are three closed doors, and a prize is behind one of them.
- You pick a door.
- The host opens one of the other doors to reveal no prize.
- The host offers you the chance to switch to the remaining door.

Should you switch? Yes!

Here's why:

- Initially, there's a $\frac{1}{3}$ probability you picked the correct door and a $\frac{2}{3}$ probability you picked the wrong door.
- Switching doors means if you initially picked the wrong door (which is more likely), you now win the prize.

The expected payoff of switching is $\left(\frac{1}{3}\right) \times 0 + \left(\frac{2}{3}\right) \times \text{Prize}$, while not switching yields $\left(\frac{1}{3}\right) \times \text{Prize} + \left(\frac{2}{3}\right) \times 0$.

## 🎲 Where Do Probabilities Come From?

Probabilities can be interpreted in different ways:

- **Frequentism**: Probabilities are relative frequencies.
    
    - Example: If we toss a coin many times, $P(\text{heads})$ is the proportion of times the coin will come up heads.
    - John Edmund Kerrich demonstrated this with coin tosses during his internment in Nazi-occupied Denmark.
- **Subjectivism (Bayesianism)**: Probabilities are degrees of belief.
    
    - But then, how do we assign belief values to statements?
    - The term "Bayesian" comes from Thomas Bayes, who proved a special case of Bayes' theorem.

## 🔀 Random Variables

- We describe the uncertain state of the world using **random variables**.
- Denoted by capital letters
	- $R$: It will rain tomorrow
	- $W$: Weather condition
	- $D$: Outcome of rolling two dice
	- $S$: Speed of my car (in KPH)
- Just like variables in CSP’s, random variables take on values in a domain
    - Domain values must be mutually exclusive and exhaustive
	    - $R \in {\text{True}, \text{False}}$
	    - $W \in {\text{Sunny}, \text{Cloudy}, \text{Rainy}, \text{Snow}}$
	    - $D \in {(1,1), (1,2), \ldots (6,6)}$
	    - $S \in [0, 260]$

## 🗓️ Events

**Probabilistic statements** are defined over **events**, or sets of world states. Examples:

- "It will rain tomorrow."
- "The weather is either cloudy or snowy."
- "The sum of the two dice rolls is 11."
- "My car is going between 50 and 90 kilometers per hour."

Events are described using propositions:

- $R = \text{True}$
- $W = \text{"Cloudy"} \vee W = \text{"Snowy"}$
- $D \in {(5,6), (6,5)}$
- $50 \leq S \leq 90$

$P(A)$ is the probability of the set of world states in which proposition $A$ holds. $P(X = x)$, or $P(x)$ for short, is the probability that random variable $X$ has taken on the value $x$.

## ⚖️ Kolmogorov’s Axioms of Probability

For any propositions (events) A, B:

- $0 \leq P(A) \leq 1$
- $P(\Omega) = 1$ and $P(\emptyset) = 0$, where $\Omega$ is the sample space and $\emptyset$ is the null/empty set.
    - Example: tossing a die:
        - $P(\Omega) = P({1, 2, \ldots, 6}) = 1$
        - $P(11) = 0, P({}) = 0$

Here's a **Venn diagram** that illustrates the Kolmogorov's axioms and their application to probability, especially the relationship between events A and B.

![Venn diagram illustrating probabilities of events](https://api-turbo.ai/ae2dc5c7-2333-418b-adbc-a0e8ad553a09/9f693f5b-e791-4728-b2a9-22d12907da52.jpeg)

$P(A\vee B)=P(A)+P(B)-P(A\land B)$ The subtraction accounts for double-counting.

Based on these axioms, $P(\neg A) = 1 - P(A)$.

These axioms are sufficient to completely specify probability theory for discrete random variables. For continuous variables, density functions are needed.

## ⚛️ Atomic Events

- **Atomic event**: a complete specification of the state of the world, or a complete assignment of domain values to all random variables
- Atomic events are mutually exclusive and exhaustive

Example: If the world consists of only two Boolean variables Cavity and Toothache, then there are 4 distinct atomic events:

- $\text{Cavity} = \text{false} \wedge \text{Toothache} = \text{false}$
- $\text{Cavity} = \text{false} \wedge \text{Toothache} = \text{true}$
- $\text{Cavity} = \text{true} \wedge \text{Toothache} = \text{false}$
- $\text{Cavity} = \text{true} \wedge \text{Toothache} = \text{true}$

## 📊 Joint Probability Distributions

A **joint distribution** assigns probabilities to every possible atomic event. From the axioms of probability it follows that the probabilities of all possible atomic events must sum to 1.

|Atomic event|P|
|---|---|
|Cavity = false ∧ Toothache = false|0.8|
|Cavity = false ∧ Toothache = true|0.1|
|Cavity = true ∧ Toothache = false|0.05|
|Cavity = true ∧ Toothache = true|0.05|

Suppose we have a joint distribution $P(X_1, X_2, \ldots, X_n)$ of $n$ random variables with domain sizes $d$. The size of the probability table is $d^n$. It becomes impossible to write out completely for all but the smallest distributions.

- $P(X = x)$ is the probability that random variable $X$ takes on value $x$
- $P(X)$ is the distribution of probabilities for all possible values of $X$

## 📉 Marginal Probability Distributions

To find the marginal distribution $P(Y)$ given the joint distribution $P(X, Y)$, sum over the values of $X$:

$$P(Y=y)=\sum\limits_{i=1}^{n}P(X=x_{i}, Y=y)$$

Similarly, to find $P(X = x)$, sum the probabilities of all atomic events where $X = x$.

Here's a table showing a joint distribution $P(\text{Cavity}, \text{Toothache})$ and how to compute marginal probabilities $P(\text{Cavity})$ and $P(\text{Toothache})$:

| Cavity | Toothache | P(Cavity ∧ Toothache) |
| ------ | --------- | --------------------- |
| false  | false     | 0.80                  |
| false  | true      | 0.10                  |
| true   | false     | 0.05                  |
| true   | true      | 0.05                  |

| P(Cavity)     | Value |
|---------------|-------|
| Cavity = false| 0.90  |
| Cavity = true | 0.10  |

|   P(Toothache)    | Value |
|:-----------------:| ----- |
| Toothache = false | 0.85  |
| Toothache = true  | 0.15  |

##  Conditional Probability

For any two events A and B,

$P(A\mid B) = \frac{P(A\land B)}{P(B)}$

Here's a **Venn diagram** that helps illustrate conditional probability, showcasing the relationship between two events, $A$ and $B$. The area where $A$ and $B$ overlap represents the probability of both events occurring together, while the individual circles represent the probabilities of each event separately.

![Venn diagram illustrating probabilities of events](https://api-turbo.ai/ae2dc5c7-2333-418b-adbc-a0e8ad553a09/76f4964b-6f3f-4346-87ab-780266a289ff.jpeg)

For example, using the joint distribution of $P(\text{Cavity}, \text{Toothache})$:

- $P(\text{Cavity} = \text{true} \mid \text{Toothache} = \text{false}) = \frac{P(\text{Cavity} = \text{true} \wedge \text{Toothache} = \text{false})}{P(\text{Toothache} = \text{false})} = \frac{0.05}{0.85} \approx 0.059$
- $P(\text{Cavity} = \text{false} \mid \text{Toothache} = \text{true}) = \frac{P(\text{Cavity} = \text{false} \wedge \text{Toothache} = \text{true})}{P(\text{Toothache} = \text{true})} = \frac{0.1}{0.15} \approx 0.667$

## 📄 Conditional Distributions

A **conditional distribution** is a distribution over the values of one variable given fixed values of other variables.

| Event                                      | Probability |
|-------------------------------------------|-------------|
| Cavity = false ∧ Toothache = false        | 0.8         |
| Cavity = false ∧ Toothache = true         | 0.1         |
| Cavity = true ∧ Toothache = false         | 0.05        |
| Cavity = true ∧ Toothache = true          | 0.05        |


| P(Cavity \| Toothache = true) |       | P(Cavity)      |       |
| ----------------------------- | ----- | -------------- | ----- |
| Cavity = false                | 0.667 | Cavity = false | 0.941 |
| Cavity = true                 | 0.333 | Cavity = true  | 0.059 |


| P(Toothache \| Cavity = true) |     | P(Toothache)      |       |
| ----------------------------- | --- | ----------------- | ----- |
| Toothache = false             | 0.5 | Toothache = false | 0.889 |
| Toothache = true              | 0.5 | Toothache = true  | 0.111 |
## 🪄 Normalization Trick

To get the whole conditional distribution $P(X \mid y)$ at once, select all entries in the joint distribution matching $Y = y$ and renormalize them to sum to one.

## 📜 Bayes Rule

- Definition of conditional probability: $P(A \mid B) = \frac{P(A \wedge B)}{P(B)}$
- Sometimes we have the conditional probability and want to obtain the joint: $P(A, B) = P(A \mid B)P(B) = P(B \mid A)P(A)$
- The chain rule: $P(A_{1:n}) = \prod_{i=1}^n P(A_i \mid A_{1:i-1})$

### Factoring a Joint Distribution

The product rule gives us two ways to factor a joint distribution:

$$P(A,B)=P(A\mid B)\times P(B\mid A)\times P(A)$$

Therefore,

$P(A\mid B) =\frac{P(B\mid A)\times P(A)}{P(B)}$

### Usefulness of Bayes Rule

- Can get diagnostic probability $P(\text{cavity} \mid \text{toothache})$ from causal probability $P(\text{toothache} \mid \text{cavity})$.
- Can update our beliefs based on evidence.
- Important tool for probabilistic inference.

### Bayes Rule Example: Marie's Wedding

Marie is getting married tomorrow, at an outdoor ceremony in the desert. In recent years, it has rained only 5 days each year ($\frac{5}{365} \approx 0.014$). Unfortunately, the weatherman has predicted rain for tomorrow. When it actually rains, the weatherman correctly forecasts rain 90% of the time. When it doesn't rain, he incorrectly forecasts rain 10% of the time. What is the probability that it will rain on Marie's wedding?

- $P(\text{Rain}) = 0.014$
- $P(\text{Predict} \mid \text{Rain}) = 0.9$
- $P(\text{Predict} \mid \neg \text{Rain}) = 0.1$
- $P(\text{Rain} \mid \text{Predict}) = ?$

Solution:

$$P(\text{Rain} \mid \text{Predict}) = \frac{P(\text{Predict} \mid \text{Rain}) \times P(\text{Rain})}{P(\text{Predict})}$$

$$P(\text{Rain} \mid \text{Predict}) = \frac{P(\text{Predict} \mid \text{Rain}) \times P(\text{Rain})}{P(\text{Predict} \mid \text{Rain}) \times P(\text{Rain}) + P(\text{Predict} \mid \neg \text{Rain}) \times P(\neg \text{Rain})}$$

$$P(\text{Rain} \mid \text{Predict}) = \frac{0.9 \times 0.014}{0.9 \times 0.014 + 0.1 \times 0.986} \approx 0.111$$

### Bayes Rule Example: Breast Cancer Screening

1% of women at age forty who participate in routine screening have breast cancer. 80% of women with breast cancer will get positive mammographies. 9.6% of women without breast cancer will also get positive mammographies. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer?

- $P(\text{Cancer}) = 0.01$
- $P(\text{Positive} \mid \text{Cancer}) = 0.8$
- $P(\text{Positive} \mid \neg \text{Cancer}) = 0.096$
- $P(\text{Cancer} \mid \text{Positive}) = ?$

## 🤝 Independence

Two events $A$ and $B$ are **independent** if and only if $P(A \wedge B) = P(A) \times P(B)$.

- In other words, $P(A \mid B) = P(A)$ and $P(B \mid A) = P(B)$
- This is an important simplifying assumption for modeling, e.g., Toothache and Weather can be assumed to be independent
- Are two mutually exclusive events independent?
    - No, but for mutually exclusive events we have $P(A \wedge B) = 0$, $P(A \vee B) = P(A) + P(B)$

### Conditional Independence

$A$ and $B$ are **conditionally independent** given $C$ iff $P(A \wedge B \mid C) = P(A \mid C) \times P(B \mid C)$.

#### Example: Toothache, Cavity, and Catch

- Toothache: boolean variable indicating whether the patient has a toothache
- Cavity: boolean variable indicating whether the patient has a cavity
- Catch: boolean variable indicating whether the dentist's probe catches in the cavity

If the patient has a cavity, the probability that the probe catches in it doesn't depend on whether he/she has a toothache $P(\text{Catch} \mid \text{Toothache}, \text{Cavity}) = P(\text{Catch} \mid \text{Cavity})$.

Therefore, Catch is conditionally independent of Toothache given Cavity. Likewise, Toothache is conditionally independent of Catch given Cavity $P(\text{Toothache} \mid \text{Catch}, \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})$.

Equivalent statement: $P(\text{Toothache}, \text{Catch} \mid \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity}) \times P(\text{Catch} \mid \text{Cavity})$

## ✍️ Exercise

Given the concepts discussed:

- $P(\text{Cavity} \vee \text{Toothache}) = ?$
- $P(\text{Cavity}) = ?$
- $P(\text{Toothache} \mid \text{Cavity}) = ?$
- $P(\text{Toothache} \mid \text{Catch}, \text{Cavity}) = P(\text{Toothache} \mid \text{Cavity})$
## 👨‍💻 Probabilistic Inference

In general, the agent observes the values of some random variables $X_1, X_2, \ldots, X_n$ and needs to reason about the values of some other unobserved random variables $Y_1, Y_2, \ldots, Y_m$.

- Figuring out a diagnosis based on symptoms and test results
- Classifying the content type of an image or a document based on some features