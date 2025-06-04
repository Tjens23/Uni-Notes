---
tags:
  - Notes
links: "[[AI Lecture 11]]"
creation date: 2025-05-30 11:30
modification date: Friday 30th May 2025 11:30:12
semester: 4
year: 2025
---


---
# [[AI Lecture 11 Notes]]

---



## Decision Trees

**Decision trees** are a type of supervised learning algorithm used for both classification and regression tasks. They work by recursively partitioning the input space into smaller and smaller regions, until each region contains data points that belong to the same class or have similar values.

### Restaurant Example 🍽️

Imagine deciding whether to wait for a table at a restaurant. Factors include:

1. Alternate: Another restaurant nearby?
2. Bar: Comfortable waiting area?
3. Fri/Sat: Is it Friday or Saturday?
4. Hungry: Are you hungry?
5. Patrons: Number of people (None, Some, Full).
6. Price
7. Raining: Is it raining?
8. Reservation: Do you have a reservation?
9. Type: Restaurant type (French, Italian, Thai, Burger).
10. WaitEstimate: (0-10, 10-30, 30-60, >60 minutes).

### Function Approximation ⚙️

- **Problem Setting**:
    
    - Set of possible instances: $X$
    - Set of possible labels: $Y$
    - Unknown target function $f : X\rightarrow Y$
    - Set of function hypotheses $H=\{h\mid h : X \rightarrow Y\}$
    - Input: Training examples of unknown target function $f:\{x_i,y_i\}_{i=1}^{n}=\{(x_{1}, y_{1}), \dots , (x_{n},y_{n})\}$
    - Output: The Hypothesis $h\in H$ that best approximates ff
- **Classification**: Learning a target function $f$ that maps attribute set $χ$ to predefined class labels $Y$.


### Tennis Game Example 🎾

Consider a dataset for deciding whether to play a tennis game.

- Columns: Features $(x_i​)$.
- Rows: Labeled instances $(x_{i}, y_{i})$.
- Class label: Whether a tennis game was played.

### Decision Tree Structure 🌲

- **Model**: A possible decision tree for the data.
- **Question**: Will a tennis game be played under (outlook=sunny, temperature=hot, humidity=high, wind=weak)?
- Each internal node: Tests an attribute $x_{i}$​.
- Each branch: Selects a value for $x_{i}=x_{ij}$.
- Each leaf node: Predicts $Y$ or $(p(Y\mid x \in \text{leaf}))$.

### Decision Tree Learning Setup 🎯

- **Instances**: Each instance $x$ in $χ$ is a feature vector (e.g., Humidity=low, Wind=weak, Outlook=rain, Temp=hot).
- **Target Function**: $f : χ \rightarrow Y$, where $Y$ is discrete-valued.
- **Hypotheses**: $H=\{h\mid h : χ \rightarrow Y\}$. Each hypothesis $h$ is a decision tree that sorts $x$ to a leaf, assigning $Y$.

### Tax Evasion Example 💸

A new tax return for 2012 is assessed to determine if it is a cheating tax return based on tax return data for 2011.

|Tid|Refund|Marital Status|Taxable Income|Cheat|
|---|---|---|---|---|
|1|Yes|Single|125K|No|
|2|No|Married|100K|No|
|3|No|Single|70K|No|
|4|Yes|Married|120K|No|
|5|No|Divorced|95K|Yes|
|6|No|Married|60K|No|
|7|Yes|Divorced|220K|No|
|8|No|Single|85K|Yes|
|9|No|Married|75K|No|
|10|No|Single|90K|Yes|

### Splitting Attributes ✂️

Splitting attributes creates a decision tree model.

|Tid|Refund|Marital Status|Taxable Income|Cheat|
|---|---|---|---|---|
|1|Yes|Single|125K|No|
|2|No|Married|100K|No|
|3|No|Single|70K|No|
|4|Yes|Married|120K|No|
|5|No|Divorced|95K|Yes|
|6|No|Married|60K|No|
|7|Yes|Divorced|220K|No|
|8|No|Single|85K|Yes|
|9|No|Married|75K|No|
|10|No|Single|90K|Yes|

First, split by Refund:

- If yes, then No Cheat.
- If no, then split by Marital Status.
    - If Single or Divorced, then split by Taxable Income.
        - If < 80K, then No Cheat.
        - If > 80K, then Yes Cheat.
    - If Married, then No Cheat.

### Decision Tree Classification Task 📊

1. **Tree Induction**: Learn Model using a training set.
2. **Deduction**: Apply the Decision Tree Model to a test set.

- Start from the root of the tree.

|Tid|Attrib1|Attrib2|Attrib3|Class|
|---|---|---|---|---|
|11|No|Small|55K|?|
|12|Yes|Medium|80K|?|
|13|Yes|Large|110K|?|
|14|No|Small|95K|?|
|15|No|Large|67K|?|

### Hunt's Algorithm 👨‍💻

- **General Structure**:

> Let D be the set of training records that reach a node t.
> 
> - If D contains records that belong to the same class yy, then tt is a leaf node labeled as yy.
> - If D is an empty set, then tt is a leaf node labeled by the default class, ydyd​.
> - If D contains records that belong to more than one class, use an attribute test to split the data into smaller subsets. Recursively apply the procedure to each subset.

- **Example**: Applying Hunt’s Algorithm to the tax evasion dataset.

### Tree Induction Strategy 🌱

> Use a greedy strategy to split records based on an attribute test that optimizes a certain criterion.

- **Issues**:
    - Determine how to split the records.
    - How to specify the attribute test condition?
    - How to determine the best split?
    - Determine when to stop splitting.

### Splitting Based on Attribute Types ➗

- **Nominal and Ordinal Attributes**:
    - Multi-way split: Use as many partitions as distinct values.
    - Binary split: Divides values into two subsets; need to find optimal partitioning.
- **Continuous Attributes**:
    - Discretization to form an ordinal categorical attribute
        - Static – discretize once at the beginning
        - Dynamic – ranges found by equal interval bucketing, equal frequency bucketing (percentiles), or clustering.
    - Binary Decision: $(A \lt v)$ or $(A \geq v)$
        - Consider all possible splits and find the best cut.
        - Can be more compute-intensive.

### Determining the Best Split 🥇

- **Greedy Approach**: Nodes with homogeneous class distribution are preferred.
- **Measure of Node Impurity**:
    - Gini Index
    - Entropy
    - Misclassification error

### GINI Index 🧮

>$\text{GINI}(t)=1-\sum[p(j\mid t)]^{2}$
> 
> where $p(j\mid t)$ is the relative frequency of class j at node t.

- Maximum $(1 - 1/n)$ when records are equally distributed among all classes.
- Minimum (0.0) when all records belong to one class.

### Splitting Based on GINI ➗

- Used in CART, SLIQ, SPRINT.

> $GINI_{split}=\sum_{i=1}^{k} \frac{n_{i}}{n}GINI(i)$ 
> 
> where $n_{i}$ = number of records at child i, and $n$ = number of records at node $p$.

### Computing GINI Index for Binary Attributes ➕

- Splits into two partitions.
- Larger and purer partitions are sought for.

### Computing Gini Index for Continuous Attributes

- Use binary decisions based on one value.
- Sort the attribute on values.
- Linearly scan these values, each time updating the count matrix and computing the Gini index.
- Choose the split position that has the least Gini index.

### Alternative Splitting Criteria Based on Information (INFO) ℹ️

> $Entropy(t) = -\sum p(j\mid t)\log_{2}p(t\mid j)$
> 
> where $p(j\mid t)$ is the relative frequency of class $j$ at node $t$.

- Measures homogeneity of a node.
- Maximum (log n) when records are equally distributed among all classes.
- Minimum (0.0) when all records belong to one class.

### Splitting Criteria based on Classification Error ❌

> $Error (t) = 1-\text{maxP}(i\mid t)$
> 
> where $P(i\mid t)$ is the probability of class i at node $t$.

- Measures misclassification error made by a node.
- Maximum $(1 - \frac{1}{n})$ when records are equally distributed among all classes.
- Minimum $(0.0)$ when all records belong to one class.

### Stopping Criteria for Tree Induction 🛑

- Stop expanding a node when all records belong to the same class.
- Stop expanding a node when all records have similar attribute values.
- Use hyperparameters such as `max_depth`, `min_samples_leaf`, `min_samples_split`, etc.
- Early termination.

### Advantages of Decision Tree Based Classification ✅

- Inexpensive to construct.
- Extremely fast at classifying unknown records.
- Easy to interpret for small-sized trees.
- Accuracy is comparable to other classification techniques for many simple datasets.

### Practical Issues of Classification ❓

- Underfitting and Overfitting
- Missing Values
- Costs of Classification

### Underfitting vs Overfitting ⚖️

- **Overfitting**: Model is more complex than necessary, and training error no longer provides a good estimate of how well the tree will perform on unseen records.
- **Underfitting**: Model is too simple, both training and test errors are large.

### Addressing Overfitting 🛠️

- **Pre-Pruning (Early Stopping Rule)**:
    - Stop the algorithm before it becomes a fully grown tree.
    - Stop if all instances belong to the same class or if all attribute values are the same.
    - More restrictive conditions:
        - Stop if the number of instances is less than a user-specified threshold.
        - Stop if the class distribution of instances are independent of the available features (e.g., using chi-squared test).
        - Stop if expanding the current node does not improve impurity measures (e.g., Gini or information gain).
- **Post-Pruning**:
    - Grow the decision tree to its entirety.
    - Trim the nodes of the decision tree in a bottom-up fashion.
    - If the generalization error improves after trimming, replace the sub-tree by a leaf node.
    - The class label of the leaf node is determined from the majority class of instances in the sub-tree.
    - Can use MDL (Minimum Description Length) for post-pruning.

### How Well Do Decision Trees Work? 🤔

Many case studies have shown that decision trees are at least as accurate as human experts.