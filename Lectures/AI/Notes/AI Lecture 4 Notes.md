---
tags:
  - Notes
links: "[[AI Lecture 4]]"
creation date: 2025-05-21 13:35
modification date: Wednesday 21st May 2025 13:35:43
semester: 4
year: 2025
---


---
# [[AI Lecture 4 Notes]]

---



## Informed (Heuristic) Search

This study guide covers informed search algorithms, which use heuristics to guide the search process. The topics include greedy best-first search, A* search, and designing heuristic functions.

### 🤔 Informed Search

- Idea: Give the algorithm **"hints"** about the desirability of different states.
- Use an **evaluation function** to rank nodes and select the most promising one for expansion.
- Types:
    - Greedy best-first search
    - A* search

### 💡 Heuristic Function

- Heuristic function:

> $h(n)$ = estimated cost of the cheapest path from the state at node _n_ to a goal state.

**Example:** The image below depicts a maze with a start state and a goal state. A pink line traverses the maze, originating from the bottom-right corner and extending to a red star within the maze.

![Maze Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/6a1c6f26-7ad7-4a1d-b86d-d22d78e53505.jpeg)

**Heuristic for the Romania Problem:**

The image below depicts a graph with nodes and edges, representing a network of cities and their connections.

![Romania Problem](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/8e9fb891-ae85-45fb-940c-b687fd9d4402.jpeg)

### 贪 Greedy Best-First Search

- Expand the node that has the lowest value of the heuristic function $h(n)$.
- Evaluation function:

> $f(n) = h(n)$

**Example:**

The image below shows a diagram illustrating the expansion of Arad, featuring a central node labeled "Arad" in a purple oval.

![Greedy Best-First Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/1c32f00a-e28a-4146-9359-be940d57307e.jpeg)

The following images show how the greedy best-first search can be applied to the Romania problem to find a path from Arad to Bucharest.

![Greedy Best-First Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/d0d6fda9-8176-4abd-8dd8-139bcc59bd0e.jpeg)

![Greedy Best-First Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/6b4098e8-19f8-4f7a-a769-6fe6752a1ff2.jpeg)

![Greedy Best-First Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/32ee0568-3e66-4d42-91f8-5250916a6c06.jpeg)

**Properties:**

The image shows a network diagram or map with various nodes and connections between them. The nodes are represented by squares and labeled with city names such as Oradea, Arad, and Bucharest. The connections between nodes are labeled with numbers, likely representing distances or weights. Two nodes, "Fagaras" and "Iasi", are highlighted with red circles and labeled as the "goal" and "start", respectively.

![Properties of Greedy Best-First Search](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/8b3dbba3-b0ce-47d6-9944-ba3ce4d5f8bb.jpeg)

- Complete? No – can get stuck in loops.
    - As seen below in the image, GBFS is not complete because it can get stuck in loops
- Time?
    - Worst case: $O(b^m)$
    - Best case: $O(b^d)$ – If $h(n)$ is 100% accurate
- Space? Worst case: $O(b^m)$

The image below compares two paths from Arad to Bucharest: one found by GBFS and another with a shorter total distance.

![Properties of Greedy Best-First Search](https://api-turbo.ai/39e40599-b61f-49f3-8890-4d7037f88114.jpeg)

### ⭐ A* Search

- Idea: Avoid expanding paths that are already expensive.
- The evaluation function $f(n)$ is the estimated total cost of the path through node _n_ to the goal:

> $f(n) = g(n) + h(n)$

```
*   \$g(n)\$: cost so far to reach *n* (path cost)
*   \$h(n)\$: estimated cost from *n* to goal (heuristic)
```

The image below illustrates a flowchart for finding the shortest path in a graph or network, representing the A* search algorithm.

![A* Search](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/ce70a464-0029-4d73-9f63-0f0646250abf.jpeg)

The following images show how the A* search can be applied to the Romania problem to find a path from Arad to Bucharest.

![A* Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/9522c0ef-2c46-450c-bbf4-62e79e0097d7.jpeg)

![A* Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/fff43e61-ed2d-4a93-89a6-ce831f877413.jpeg)

![A* Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/2c950223-8d57-4b40-a0fc-451c1b94db9f.jpeg)

![A* Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/14f3ad9c-fb9e-4ac7-85db-494183fe0e2e.jpeg)

![A* Search Example](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/016726c4-f442-44bc-b615-99878fa7276e.jpeg)

**Properties:**

- Complete? Yes – unless there are infinitely many nodes with $f(n) ≤ C*$
- Optimal? Depends on certain properties of the heuristic. A key property is **admissibility**.

### 🧪 Admissible Heuristics

- An **admissible heuristic** never overestimates the cost to reach the goal; i.e., it is optimistic.
- A heuristic $h(n)$ is admissible if for every node _n_, $h(n) ≤ h*(n)$, where $h*(n)$ is the true cost to reach the goal state from _n_.
- Example: Straight line distance never overestimates the actual road distance.
- **Theorem:** If $h(n)$ is admissible, then A* is optimal.

**Proof by contradiction:**

- Assume A* is not optimal ➔ returns a path with $C > C*$ ($C*$ cost of the optimal path)
- There exists a node _n_ on the optimal path that is unexpanded
- $C = f(n) = g(n) + h(n) > C*$ (otherwise _n_ would have been expanded)
- $f(n) = g*(n) + h(n) > C*$ (because _n_ is on an optimal path)
- $f(n) = g*(n) + h(n) <= g*(n) + h*(n)$ (admissibility of _h_, $h(n)<= h*(n)$)
- $C* < C = f(n) <= g*(n) + h*(n) = C*$ (contradiction)

__Properties of A_ with Admissible Heuristic:_*

- Complete? Yes – unless there are infinitely many nodes with $f(n) ≤ C*$
- Optimal? Yes
- Time? Number of nodes for which $f(n) ≤ C*$ (exponential)
- Space? Exponential

### 🎨 Designing Heuristic Functions

Consider the 8-puzzle problem. Two possible heuristics are:

- $h_1(n)$ = number of misplaced tiles
- $h_2(n)$ = total Manhattan distance (number of squares from desired location of each tile)

The image below presents two 3x3 grids, labeled as the "Start State" and the "Goal State" for the 8-puzzle problem.

![Heuristics for the 8-puzzle](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/35f6a3e4-6d9e-4d8d-aa68-75417770de26.jpeg)

The image below presents a visual representation of the 8-puzzle problem, showcasing both the "Current State" and the "Goal State".

![Heuristics for the 8-puzzle](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/09708f90-7dba-4704-bd3f-f8cb4c4bdba3.jpeg)

Are $h_1$ and $h_2$ admissible?

**Example Calculations:**

- For $h_1(n)$: The number of misplaced tiles (not including the blank). In this case, only “8” is misplaced, so the function evaluates to 1.
- For $h_2(n)$: Total Manhattan distance (not including the blank).

The 3, 8, and 1 tiles are misplaced (by 2, 3, and 3 steps), so the heuristic function evaluates to 8.

The image below presents a visual representation of the 8-puzzle problem, comprising a "Start State" grid and a "Goal State" grid.

![Heuristics for the 8-puzzle](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/5a6db967-1d52-431e-8d28-6cade57db4e4.jpeg)

The image below shows the initial "Start State" and the desired "Goal State" with example heuristic functions.

![Heuristics for the 8-puzzle](https://api-turbo.ai/39e40599-b61f-4f15-8255-204a31adcf2d.jpeg)

Both $h_1$ and $h_2$ are admissible (shortest solution is 26 actions long).

### 👑 Dominance

- If $h_1$ and $h_2$ are both admissible heuristics and $h_2(n) ≥ h_1(n)$ for all _n_, then $h_2$ dominates $h_1$.
- Which one is better for search?
    - A* search expands every node with $f(n) < C*$ ($C*$: optimal cost) or $h(n) < C* – g(n)$
    - Therefore, A* search with $h_1$ will expand more nodes, so $h_2$ is better.

### 😌 Heuristics from Relaxed Problems

- **Relaxed problem:** A problem with fewer restrictions on the actions.
- The state-space graph of the relaxed problem is a supergraph.
- Any optimal solution in the original problem is also a solution (maybe better) in the relaxed one.
- The cost of an optimal solution to a relaxed problem is an admissible heuristic for the original problem.

If the rules of the 8-puzzle are relaxed:

- So that a tile can move anywhere, then $h_1(n)$ gives the shortest solution.
- So that a tile can move to any adjacent square, then $h_2(n)$ gives the shortest solution.

**Example Search Costs:**

Typical search costs for the 8-puzzle (average number of nodes expanded for different solution depths, _d_):

(IDS: iterative deepening search)

|d|IDS|A* ($h_1$)|A* ($h_2$)|
|---|---|---|---|
|12|3,644,035 nodes|227 nodes|73 nodes|
|24|≈ 54,000,000,000|39,135|1,641|

### 🤝 Combining Heuristics

- Suppose we have a collection of admissible heuristics $h_1(n), h_2(n), …, h_m(n)$, but none of them dominates the others.
- How can we combine them?

> $h(n) = max{h_1(n), h_2(n), …, h_m(n)}$

### ⚖️ Weighted A* Search

- Idea: Speed up search at the expense of optimality.
    
- Take an admissible heuristic, “inflate” it by a multiple $α > 1$, and then perform A* search as usual.
    
    - Weighted A*: Expands nodes in the order of $f = g + αh$
- Fewer nodes tend to get expanded, but the resulting solution may be suboptimal (its cost will be at most $α$ times the cost of the optimal solution, $C* < C_{weighted A*}< αC*$)
    
- Weighted A* is biased towards states that are closer to the goal.
    

Weighted A* can be seen as a generalization of other searches:

- A* search: $g(n) + h(n)$ ($α = 1$)
- Uniform cost search: $g(n)$ ($α = 0$)
- Greedy BFS: $h(n)$ ($α = ∞$)
- Weighted A*: $g(n) + αh(n)$ ($1 < α < ∞$)

### 💪 Dealing with Hard Problems

- For large problems, A* may require too much space.
- Variations conserve memory: IDA* and SMA*
    - IDA*, iterative deepening A*, uses successive iteration with growing limits on _f_, e.g.
        - A* but don’t consider a node _n_ where $f(n) > 10$
        - A* but don’t consider a node _n_ where $f(n) > 20$
        - A* but don’t consider a node _n_ where $f(n) > 30$, ...
    - SMA* -- Simplified Memory-Bounded A*
        - Uses queue of restricted size to limit memory use

### 📈 Summary of Search Strategies

**Uninformed search strategies:**

|Algorithm|Complete?|Optimal?|Time complexity|Space complexity|
|---|---|---|---|---|
|BFS|Yes|Yes If all step costs are equal|$O(b^d)$|$O(b^d)$|
|UCS|Yes|Yes If all step costs are equal||Number of nodes with $g(n) ≤ C*$|
|DFS|No|No|$O(b^m)$|$O(bm)$|
|IDS|Yes|Yes|$O(b^d)$|$O(bd)$|

- b: maximum branching factor of the search tree
- d: depth of the optimal solution
- m: maximum length of any path in the state space
- C*: cost of optimal solution

**All search strategies:**

|Algorithm|Complete?|Optimal?|Time complexity|Space complexity|
|---|---|---|---|---|
|BFS|Yes|If all step costs are equal|$O(b^d)$|$O(b^d)$|
|UCS|Yes|If all step costs are equal||Number of nodes with $g(n) ≤ C*$|
|DFS|No|No|$O(b^m)$|$O(bm)$|
|IDS|Yes|Yes|$O(b^d)$|$O(bd)$|
|Greedy|No|No|Worst case: $O(b^m)$ Best case: $O(b^d)$|$O(b^m)$|
|A*|Yes|Yes|Number of nodes with $g(n)+h(n) ≤ C*$|Number of nodes with $g(n)+h(n) ≤ C*$|

### 🗺️ Example Search Space

The image below depicts a directed graph with nodes and edges, commonly used to represent a network or a flow problem in graph theory. The graph features a source node labeled "S" in purple, connected to other nodes labeled A, B, C, D, E, and G.

![Example Search Space](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/3688b9f3-31f1-4701-90cb-518bab14043f.jpeg)

The following images show the g values (current), h values, and arc costs, which are color-coded in blue, black, and red, respectively.

![Example Search Space](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/3d8c7b88-5f64-4428-b7d5-331cdbc75304.jpeg)

![Example Search Space](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/6562024f-10bc-4443-b538-8419d1e5c56b.jpeg)

|Node|g(n)|h(n)|f(n)|h*(n)|
|---|---|---|---|---|
|S|0|8|8|9|
|A|1|8|9|9|
|B|5|4|9|4|
|C|8|3|11|5|
|D|4|∞|∞|∞|
|E|8|∞|∞|∞|
|G|9|0|9|0|

- $h*(n)$ is (hypothetical) perfect heuristic (an oracle)
- Since $h(n) <= h*(n)$ for all _n_, _h_ is admissible (optimal)
- Optimal path = S B G with cost 9
- $f(n) = h(n)$

The image below depicts a complex graph with nodes and edges, representing a network or system. The graph features a central node labeled "S" in purple, connected to other nodes (A, B, C, D, E, G) via black arrows with numerical labels.

![Greedy Search](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/76548e20-7825-41f4-93cc-77c4415382ea.jpeg)

**Greedy search:**

- Node expanded: S
- Nodes list: { S(8) }
- S { C(3) B(4) A(8) }
- C { G(0) B(4) A(8) }
- G { B(4) A(8) }
- Solution path found is S C G, 3 nodes expanded. See how fast the search is!! But it is NOT optimal.

__A_ search:_*

- $f(n) = g(n) + h(n)$
- Node exp. nodes list { S(8) }
- S { A(9) B(9) C(11) }
- A { B(9) G(10) C(11) D(inf) E(inf) }
- B { G(9) G(10) C(11) D(inf) E(inf) }
- G { C(11) D(inf) E(inf) }
- Solution path found is S B G, 4 nodes expanded. Still pretty fast, and optimal, too.

The image below depicts a weighted graph, which is a type of graph where each edge has a numerical value or weight associated with it.

![A* Search](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/0f0ce515-9c22-4a40-a4c2-e98895cd8afe.jpeg)

The image below illustrates a step-by-step process of a search algorithm, likely A* search, which is used to find the shortest path between two nodes in a weighted graph.

![A* Search](https://api-turbo.ai/39e40599-b61f-498e-8054-fcbe82f10eeb/45383836-637d-48a3-821c-e743194df42b.jpeg)

__Solution using A_ search:_*

- Solution path found is: a, c, d, e, z, and 6 nodes expanded.

### 📝 Summary of Informed Search

- Greedy best-first search uses minimal estimated cost $h(n)$ to the goal state as measure; reduces search time but is neither complete nor optimal.
- A* search combines uniform-cost search & greedy best-first search: $f(n) = g(n) + h(n)$. Handles state repetitions & $h(n)$ never overestimates
    - A* is complete & optimal, but space complexity is high.
    - Time complexity depends on the quality of the heuristic function.
    - IDA* and SMA* reduce the memory requirements of A*.