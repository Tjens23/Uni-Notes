---
tags:
  - Notes
links: "[[AI Lecture 12]]"
creation date: 2025-05-30 11:57
modification date: Friday 30th May 2025 11:57:51
semester: 4
year: 2025
---


---
# [[AI Lecture 12 Notes]]

---



## Intro to Machine Learning

### Definition

> **Machine learning** is getting a computer to perform a task well without explicit programming, achieved by improving performance on a task based on experience.

**Example:** Image classification involves inputting an image and receiving a desired output label, such as apple, pear, tomato, cow, dog, or horse.

### 🍎 Learning for Episodic Tasks

In episodic tasks:

- An agent receives a series of unrelated problem instances.
- The agent makes some decision or inference about each instance.
- "Experience" comes in the form of **training data**.

**Example:** Providing labeled images like apple, pear, tomato, cow, dog, and horse as training data.

### 🔑 Key Challenge

The key challenge of learning is **generalization** to unseen examples.

**Examples:**

1. **Seismic data classification**: Categorizing seismic data related to earthquakes, nuclear explosions, etc.
2. **Spam filter**: Identifying spam emails based on learned patterns.

### ⚙️ The Basic Machine Learning Framework

The machine learning framework can be represented as:

$y=f(x)$
Where:
- $x$ = input
- $y$ = output/classification
- $f$ = function

**Learning**: Given a training set of labeled examples $(x_{1},y_{1}),\dots,(x_n,y_n)$, the goal is to estimate the parameters of the prediction function $f$.

**Inference**: Apply $f$ to a never-before-seen test example $x$ and output the predicted value $y=f(x)$

### 📊 Learning and Inference Pipeline

1. **Learning**: Use training data to estimate parameters of the function ff.
2. **Inference**: Apply the learned function ff to new, unseen data to predict the output.

### 🧪 Naïve Bayes Classifier

The Naïve Bayes classifier is defined as:

$$f(x) = \arg\max P(y|x)$$ $$\propto \arg\max P(y)P(x|y)$$ $$= \arg\max P(y) \prod_{d} P(x_d|y)$$

Where $x_{d}$​ represents a single dimension or attribute of $x$.

### 🌳 Decision Tree Classifier

**Example Problem:** Deciding whether to wait for a table at a restaurant based on attributes.

**Attributes:**

1. Alternate: Is there an alternative restaurant nearby?
2. Bar: Is there a comfortable bar area to wait in?
3. Fri/Sat: Is today Friday or Saturday?
4. Hungry: Are we hungry?
5. Patrons: Number of people in the restaurant (None, Some, Full)
6. Price: Price range 
7. Raining: Is it raining outside?
8. Reservation: Have we made a reservation?
9. Type: Kind of restaurant (French, Italian, Thai, Burger)
10. WaitEstimate: Estimated waiting time (0-10, 10-30, 30-60, >60)

### 🏘️ Nearest Neighbor Classifier

$f(x)$= label of the training example nearest to $x$

- All that is needed is a distance function for the inputs.
- No training is required.

### 👯 K-Nearest Neighbors Classifier

- For a new point, find the kk closest points from the training data.
- Vote for the class label with labels of the kk points.

### 📏 Linear Classifier

Find a linear function to separate the classes:

$f(x) = \text{sgn}(w_1x_1 + w_2x_2 + \ldots + w_Dx_D) = \text{sgn}(w \cdot x)$`

## 📝 Exam Information

### 📅 Exam Details

- **Date**: June 6th
- **Format**: Multiple choice
- **Weighting**: 10-20% homework/exercise related
- **Allowed aids**:
    - Visual Studio Code
    - Pycharm
    - Homework folder (digital)
    - Calculator
    - Offline dictionary
- **Duration**: 2 hours

### ✍️ Exam Code Clarification

- Any additional comments in the code, beyond what is typical and directly related to the code, are not allowed in the exam.
- Code may only be run for the exam questions related to the homework/exercise, and the code should be the one related to the exercise/homework.

### ❓ Example Exam Questions

1. **Question**: What kind of environment has a crossword puzzle?
    - A. Dynamic
    - B. Static*
    - C. None of the mentioned
    - D. Stochastic
2. **Question**: Consider the search problem shown in the figure. S is the start-state, G is the (only) goal-state. Break any ties alphabetically. For the questions that ask for a path, please give your answers in the form `S - A - D - G.’` What path would depth-first graph search return for this search problem?
    - A. S – A – D – G
    - B. S – B – G*
    - C. S – A – C – G
    - D. S – B – D – G
3. **Question**: The Bayesian Network LMV below has three nodes for boolean variables, L, M and V. The probabilities for L and M are: P (M = true) = 0.2 and P (L = true) = 0.7. The conditional probabilities for variable V are as shown in the table below. Which value is closest to the value of P(V = false | L = false) ?
    - A. 0.3
    - B. 0.7*
    - C. 0.9
    - D. 0.1
4. **Question**: The homework question is related to: Exercise on Bayesian Networks. Using your homework from Exercise 7, calculate the conditional probability of the fuel tank leaking given that there is a high consumption. What is the conditional probability of the fuel tank leaking given that there is a high consumption?
    - A. approximately 87 %
    - B. approximately 3 %
    - C. approximately 42 %
    - D. approximately 11 %*
    - E. approximately 62 %