---
tags:
  - Notes
links: "[[AI Lecture 7]]"
creation date: 2025-05-21 13:59
modification date: Wednesday 21st May 2025 13:59:13
semester: 4
year: 2025
---


---
# [[AI Lecture 7 Notes]]

---



## 🧩 Constraint Satisfaction Problems (CSPs)

Constraint satisfaction is a powerful problem-solving paradigm where the goal is to assign values to a set of variables, satisfying problem-specific constraints.

### Algorithms for CSPs

- **Backtracking**
- **Constraint propagation**
- **Variable and value ordering heuristics**

## 👑 Motivating Example: 8 Queens

The 8 Queens problem involves placing eight queens on a chessboard such that no queen attacks another.

- A naive generate-and-test approach, without redundancies, results in 8^8 (16,777,216) combinations.
- Placing queens strategically and marking squares that can no longer be used can drastically reduce the search space.

## 🤔 What More Do We Need for 8 Queens?

Beyond a successor function and goal test, we require:

- A way to **propagate constraints** imposed by one queen on others.
- An **early failure test** to avoid exploring unproductive paths.

## 📝 CSP Definitions

- **Variables**: $X_1, X_2, ..., X_n$, each $X_i$ having a non-empty domain $D_i$ of possible values.
- **Constraints**: $C_1, C_2, ..., C_m$ consisting of some subset of variables and specifies allowable combinations of values for that subset.
- **State**: Defined by an assignment of values to some or all variables ($X_1 = v_1, X_j = v_j, ...$).
- **Consistent**: An assignment that does not violate any constraints.
- **Solution**: A complete assignment that satisfies all constraints.

## ⚙️ CSP Formulation

- **Initial state**: Empty assignment (all variables are unassigned).
- **Successor function**: Assigns a value to an unassigned variable that does not conflict with previously assigned variables.
- **Goal test**: The current assignment is complete and satisfies all constraints.
- **Path cost**: Constant cost per step.

## 🗺️ Example: Map Coloring

- **Variables**: WA, NT, Q, NSW, V, SA, T
    
- **Domains**: {red, green, blue}
    
- **Constraints**: Adjacent regions must have different colors (e.g., WA ≠ NT).
    
    - Example Constraint: $(WA, NT) \in {(red, green), (red, blue), (green, red), (green, blue), (blue, red), (blue, green)}$
- **State**: One of many but not a solution, e.g. WA = red, NT = red, Q =red, NSW = red, V = red, SA = red, T = red
    
- **Solutions**: Complete and consistent assignments, e.g., WA = red, NT = green, Q = red, NSW = green, V = red, SA = blue, T = green
    

## 🕸️ Constraint Graph

Nodes are variables, and arcs show constraints. For map coloring, the constraint $a \ne b$ means no adjacent Australian states are the same color.

## ♟️ Example: n-queens problem

Place n queens on an n × n board with no two queens on the same row, column, or diagonal

## 🔢 Example: N-Queens

- **Variables**: $X_{ij}$
    
- **Domains**: {0, 1}
    
- **Constraints**:
    
    - $ \Sigma_{j} X_{ij} = N_{i,j} $
    - $(X_{ij}, X_{ik}) \in {(0, 0), (0, 1), (1, 0)}$
    - $(X_{ij}, X_{kj}) \in {(0, 0), (0, 1), (1, 0)}$
    - $(X_{ij}, X_{i+k, j+k}) \in {(0, 0), (0, 1), (1, 0)}$
    - $(X_{ij}, X_{i+k, j-k}) \in {(0, 0), (0, 1), (1, 0)}$

## ➕ Example: Cryptarithmetic

Each letter stands for a distinct digit. The aim is to find a substitution of digits for letters such that the resulting sum is arithmetically correct.

- **Variables**: T, W, O, F, U, R, $X_1, X_2$
    
- **Domains**: {0, 1, 2, …, 9}
    
- **Constraints**:
    
    - $O + O = R + 10 * X_1$
    - $W + W + X_1 = U + 10 * X_2$
    - $T + T + X_2 = O + 10 * F$
    - `Alldiff(T, W, O, F, U, R)`
    - $T \ne 0, F \ne 0$

## 🧩 Example: Sudoku

- **Variables**: $X_{ij}$
- **Domains**: {1, 2, …, 9}
- **Constraints**: `Alldiff`($X_{ij}$ in the same unit)

## 🏢 Real-world CSPs

- **Assignment problems**: Who teaches what class
- **Timetable problems**: Which class is offered when and where?
- **Transportation scheduling**
- **Factory scheduling**
- More examples: [http://www.csplib.org/](http://www.csplib.org/)

## 🧐 Standard Search Formulation (Incremental)

- **States**: Variables and values assigned so far
- **Initial state**: The empty assignment
- **Action**: Choose any unassigned variable and assign to it a value that does not violate any constraints
- **Fail**: If no legal assignments
- **Goal test**: The current assignment is complete and satisfies all constraints

### Depth and Paths

- **Depth of any solution** (assuming n variables): n
- **Number of paths in the search tree**: $n! \cdot m^n$ (where m is the number of possible values for any variable)

## 🔙 Backtracking Search

In CSPs, variable assignments are commutative. For example, [WA = red then NT = green] is the same as [NT = green then WA = red]. We only need to consider assignments to a single variable at each level (i.e., we fix the order of assignments). Then there are only $m^n$ leaves (n – number of variables and m – number of values). Depth-first search for CSPs with single-variable assignments is called backtracking search.

## 🔄 CSP-BACKTRACKING(PartialAssignment A) Algorithm

```
If A is complete then return A
X ← select an unassigned variable
D ← select an ordering for the domain of X
For each value v in D do
    If v is consistent with A then
        Add (X = v) to A
        result ← CSP-BACKTRACKING(A)
        If result ≠ failure, then return result
        Remove (X = v) from A
Return failure
```

Start with `CSP-BACKTRACKING({})`

## 💡 Improving Backtracking Efficiency

- Which variable should be assigned next?
- In what order should its values be tried?
- Can we detect inevitable failure early?

## 🔣 Which Variable Should Be Assigned Next?

### Most Constrained Variable (Minimum Remaining Values - MRV)

Choose the variable with the fewest legal values.

### Most Constraining Variable

Choose the variable that imposes the most constraints on the remaining variables. This serves as a tie-breaker among most constrained variables. Among the variables with the smallest remaining domains, select the one that appears in the largest number of constraints on variables not in the current assignment.

## 🎯 Given a Variable, in Which Order Should Its Values Be Tried?

### Choose the Least Constraining Value

The value that rules out the fewest values in the remaining variables.

## ⏰ Early Detection of Failure: Forward Checking

Keep track of remaining legal values for unassigned variables and terminate search when any variable has no legal values.

## ⛓️ Constraint Propagation

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures. Constraint propagation repeatedly enforces constraints locally.

## ↔️ Arc Consistency

Simplest form of propagation makes each pair of variables consistent. $X \rightarrow Y$ is consistent iff for every value of X there is some allowed value of Y. When checking $X \rightarrow Y$, throw out any values of X for which there isn’t an allowed value of Y. If X loses a value, all pairs $Z \rightarrow X$ need to be rechecked. Arc consistency detects failure earlier than forward checking and can be run before or after each assignment.

## 🧪 Arc Consistency - Example

- Domains:
    - $D_x = {1, 2, 3}$
    - $D_y = {1, 2, 3}$
- Constraint: X must be less than Y ($C_{xy}$)
- $C_{xy}$ not arc consistent w.r.t. x or y; enforcing arc consistency, we get reduced domains:
    - $D'_x = {1, 2}$
    - $D’_y = {2, 3}$

## 🔑 Summary

|Concept|Description|
|---|---|
|CSPs|States defined by values of a fixed set of variables; goal test defined by constraints on variable values|
|Backtracking|Depth-first search where successor states are generated by considering assignments to a single variable|
|Variable/Value Ordering|Heuristics that can significantly help|
|Forward Checking|Prevents assignments that guarantee later failure|
|Constraint Propagation|(e.g., arc consistency) Simple yet powerful to constrain values and detect inconsistencies|
|Complexity of CSPs|NP-complete in general (exponential worst-case running time)|
