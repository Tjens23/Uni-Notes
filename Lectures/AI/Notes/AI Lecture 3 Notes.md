---
tags:
  - Notes
links: "[[AI Lecture 3]]"
creation date: 2025-05-13 13:46
modification date: Tuesday 13th May 2025 13:46:21
semester: 4
year: 2025
---


---
# [[AI Lecture 3 Notes]]

---


## 🤖 Solving Problems by Searching

### Search as Problem-Solving Strategy

Many problems can be framed as reaching a **goal state** from a given **starting point**. When the correct action isn't immediately obvious, an agent might need to plan a sequence of actions to reach the goal state. This agent is called a **problem-solving agent**.

![Flowchart for Dealing with Malfunctioning Items](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/c0cea7a6-cc59-4941-8e28-8be00c95439f.jpeg)

Here's an image depicting a flowchart that illustrates a problem-solving strategy when dealing with a malfunctioning item.

Examples of such problems include:

- Getting from home to SDU
    - Start: Home
    - Goal: SDU
    - Operators: Move one block, turn
- Loading a moving truck
    - Start: Apartment full of boxes and furniture
    - Goal: Empty apartment, all boxes and furniture in the truck
    - Operators: Select item, carry item from apartment to truck, load item
- Getting settled
    - Start: Items randomly distributed
    - Goal: Satisfactory arrangement of items
    - Operators: Select item, move item

### 🎯 Motivation

**Search strategies** are important methods for problem-solving. Using search requires an abstract formulation of the problem and the available steps. **Search algorithms** form the basis for many optimization and planning methods.

### 📝 Objectives

- Formulate problems as search tasks, defining:
    - States
    - Initial state
    - Goal state
    - Successor functions (operators)
    - Cost
- Understand fundamental search strategies and algorithms:
    - **Uninformed search**
        - Breadth-first
        - Depth-first
        - Uniform-cost
        - Iterative deepening
    - **Informed search**
        - Best-first (Greedy, A*)
        - Heuristics
- Evaluate the suitability of a search strategy for a problem based on:
    - Completeness
    - Optimality

### 🔎 Search

We consider designing goal-based agents in observable, deterministic, discrete, known environments.

![Maze with Start and Goal States](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/aa442fc6-027d-4e35-ab56-50bc069ef6d0.jpeg)

The image above shows a maze that demonstrates the concept of searching for a path from a start state to a goal state.

- **Solution**: A fixed sequence of actions.
- **Search**: The process of finding the sequence of actions that reaches the goal. The agent can ignore percepts during execution.

### 🧩 Search Problem Components

- **Initial state**: The starting point.
- **Successor Function (Operator)**: The result of doing an action in a state.
- **Goal state**: The desired end state.
- **Path cost**: The sum of non-negative step costs.

The **optimal solution** is the sequence of actions with the lowest path cost to reach the goal.

### 🗺️ Example: Romania

Imagine you are on vacation in Romania, currently in Arad, and your flight leaves tomorrow from Bucharest.

- **Initial state**: Arad
- **Goal state**: Bucharest
- **Successor Function**: S(Arad) = {Zerind, Timisoara, Sibiu}
- **Path Cost**: Sum of edge costs

A **solution** is a sequence of actions leading from the initial state to a goal state.

![Map of Romania with Arad and Bucharest Highlighted](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/ddfa33ce-13ea-450a-adaf-d35aaedcbcc8.jpeg)

The image above presents a map of Romania, visually depicting the problem of finding a route from Arad to Bucharest, with the path cost represented by the distances between cities.

### 🌌 State Space

> The **state space** of a problem is defined by the initial state and the successor function. It is the set of all states reachable from the initial state by any sequence of actions, and can be represented as a directed graph. Nodes are states, and links between nodes are actions.

What is the state space for the Romania problem?

### 🧹 Example: Vacuum World

- **Initial State**: Any
    
- **Goal State**: All clean
    
- **Successor function**: Described by state space
    
    ![Vacuum World State Space Graph](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/c20e9836-ceee-4069-b8ba-724da98cfda3.jpeg)
    
    The image above is the state space graph for the vacuum world problem.
    
- **Path Cost**: Sum of electricity consumed with each move.
    

### 🧩 Example: The 8-Puzzle

- **Initial State**: Any locations of tiles
- **Successor Function**: Move blank left, right, up, down, and consequent states
- **Path cost**: 1 per move

![8-Puzzle Initial State](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/8600a805-8b86-4dab-80de-36899a7213a2.jpeg)

The image above depicts an example of an initial state for the 8-puzzle.

- Number of states:
    - 8-puzzle: $9!/2 = 181,440$ states
    - 15-puzzle: $16!/2 > 10$ trillion states
    - 24-puzzle: $10^{25}$ states
- Optimal solution of n-Puzzle is NP-hard

![8-Puzzle State Transitions](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/82960008-6344-435a-9100-6c3cc9835ec0.jpeg)

The image above shows the matrix transformation process of the 8-puzzle.

### 🧩 Simpler: 3-Puzzle

![3-Puzzle Solution](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/112a19da-8a52-42a2-af72-9d6be8388b48.jpeg)

The image above is a visual representation of the solution to the 3-puzzle.

### 🏗️ Building Goal-Based Agents

We must answer the following questions:

- How do we represent the state of the “world”?
- What is the goal and how can we recognize it?
- What are the possible actions?
- What relevant information do we encode to describe states, actions, and their effects to solve the problem?

### 🛣️ Example: Route Planning

Find a route from Arad to Bucharest.

![Map of Romania with Route from Arad to Bucharest](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/afd5d27a-e365-4b11-bdf9-296993479d2d.jpeg)

The image shows the map of Romania with a route from Arad to Bucharest.

### 👑 Example: The 8-Queens Puzzle

Place eight queens on a chessboard such that no queen attacks any other. This can be generalized to an NxN chessboard.

![8-Queens Puzzle on a Chessboard](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/7eb040ff-15c3-4c12-976e-f137a13f9904.jpeg)

The image above shows an example of the 8-queens puzzle on a chessboard.

### 🌳 Tree Search

![Tree Search Illustration](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/b7048c3e-41fc-4ff8-80d5-a85a02a86889.jpeg)

The image above presents a detailed illustration of a search tree.

### ⚙️ Tree Search Algorithm Outline

1. Initialize the **fringe** using the starting state.
2. While the fringe is not empty:
    - Choose a fringe node to expand according to a search strategy.
    - If the node contains the goal state, return the solution.
    - Else, expand the node and add its children to the fringe.
3. To handle repeated states:
    - Keep an **explored set**; add each node to it when expanded.
    - When adding a node to the fringe, check if it already exists with a higher path cost; if so, replace it.

### 🗺️ Tree Search Example

![Tree Search Example - Romania Map and Tree](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/0a0c1e55-ac9e-4e0a-87f9-a11eddb03aab.jpeg)

![Tree Search Example - Arad with Sibiu, Timisoara, Zerind](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/21c674fb-d866-41d4-9713-5d3bfccaa77c.jpeg)

![Tree Search Example - Fringe with Sibiu, Timisoara, Zerind](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/bd70d563-de24-4124-a6a8-5e285dfb478d.jpeg)

![Tree Search Example - Map with Distances](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/94141bf6-6fef-4c14-8ee9-c61a7da4f74b.jpeg)

![Tree Search Example - Fringe Expansion](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/22ac4f85-d7e2-4629-b2d6-2b2b2ab12df7.jpeg)

### 🧭 Search Strategies

A **search strategy** is defined by the order of node expansion. Strategies are evaluated based on:

- **Completeness**: Does it always find a solution if one exists, and correctly report failure when there is none?
- **Optimality**: Does it always find a least-cost solution?
- **Time complexity**: How long does it take to find the solution?
- **Space complexity**: How much memory is needed?

Time and space complexity are measured in terms of:

- b: Maximum branching factor of the search tree
- d: Depth of the least-cost solution
- m: Maximum length of any path in the state space (may be infinite)

### 🧐 Uninformed Search Strategies

> **Uninformed search strategies** use only the information available in the problem definition.

Examples include:

- Breadth-first search (BFS)
- Uniform-cost search (UCS)
- Depth-first search (DFS)
- Iterative deepening search (IDS)

### 🍞 Breadth-First Search

> **Breadth-first search (BFS)** expands the shallowest unexpanded node. The fringe is a FIFO queue, so new successors go at the end.

![Breadth-First Search - Initial State](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/f46a5cae-6e14-4a15-9b58-e930d9ee8fdc.jpeg)

![Breadth-First Search - Expanding A](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/53de2241-a019-4622-ae46-050f51d78b0f.jpeg)

![Breadth-First Search - Expanding B](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/5dee623a-e420-4cf0-80a0-af86c0f6de0c.jpeg)

![Breadth-First Search - Expanding C](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/d569c919-be8a-43b5-b81c-63339af2c126.jpeg)

![Breadth-First Search - Expanding D and E](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/078b43a1-459a-44e3-8128-c501d9d17de5.jpeg)

#### Properties of Breadth-First Search

- **Complete?** Yes
- **Optimal?** Yes, if cost = 1 per step
- **Time?** $O(b^d)$
- **Space?** $O(b^d)$

Space is the bigger problem, and exponential-complexity search problems cannot be solved by uninformed search for anything but the smallest instances.

### 🪙 Uniform-Cost Search

> **Uniform-cost search (UCS)** expands the least-cost unexpanded node. The fringe is ordered by path cost (priority queue).

- Equivalent to breadth-first if step costs are all equal.
- **Complete?** Yes
- **Optimal?** Yes, nodes are expanded in increasing order of path cost.
- **Time?** $O(b^{1+[C*/ε]})$
- **Space?** $O(b^{1+[C*/ε]})$

The time and space complexity can be greater than $b^d$ because the search can explore long paths with small steps before exploring shorter paths with larger steps.

#### Uniform-Cost Search Example

![Uniform-Cost Search Graph](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/aea41dfd-7ed2-43a7-8286-2b98a20f3590.jpeg)

**Start Node: A, Goal Node: G**

## Step 1

1. **Fringe:** Node A Cost 0, **Explored:** -

## Step 2

2. **Expand A, Fringe:** Node D B Cost 3 5, **Explored:** A

## Step 3

3. **Expand D, Fringe:** Node B E F Cost 5 5 5, **Explored:** A D

## Step 4

4. **Expand B, Fringe:** Node E F C Cost 5 5 6, **Explored:** A D B

## Step 5

5. **Expand E, Fringe:** Node F C Cost 5 6, **Explored:** A D B E

## Step 6

6. **Expand F, Fringe:** Node C G Cost 6 8, **Explored:** A D B E F

## Step 7

7. **Expand C, Fringe:** Node G Cost 14, **Explored:** A D B E F C

## Step 8

8. **Expand G, Found the path:** A to D to F to G

**Final Path:** A → D → F → G

### 깊 Depth-First Search

> **Depth-first search (DFS)** expands the deepest unexpanded node. It uses a LIFO queue, putting successors at the front.

The order of exploration is A -> D -> F.

### Depth-First Search Example

![[frame_61.webp]]
## Depth-First Search

**Depth-First Search (DFS)** expands the deepest unexpanded node in a search tree. It's implemented using a **LIFO (Last-In, First-Out) queue**, where successors are placed at the front of the queue.

![Tree diagram illustrating depth-first search](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/d73ff26e-4083-4f9b-910a-2c7a1708423f.jpeg)

The image above shows a tree diagram with nodes A to G. In a depth-first search, you start at the root (A) and explore as far as possible along each branch before backtracking.

![Tree diagram with arrows and nodes](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/5cab2c83-b58a-4b56-ac14-81146d9472b7.jpeg)

The second image highlights the traversal path in a depth-first manner. Notice how the algorithm dives deep into the tree before exploring other branches.

![Tree diagram showing path from C to A](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/533b551e-bab1-4bc9-8bec-11d125fdee88.jpeg)

This third image shows a tree diagram with a red arrow pointing from Node C back to Node A. The image is showing that DFS may not know when to quit if it has expanded nodes that it has already seen, and has to backtrack.

### Properties of Depth-First Search

- **Completeness:**
    
    - Fails in infinite-depth spaces, i.e., spaces with loops.
    - Can be modified to avoid repeated states along a path, making it complete in finite spaces.
- **Optimality:** Not optimal because it returns the first solution it finds, which may not be the best.
    
- **Time Complexity:** $O(b^m)$, where `m` is the maximum depth of the tree. This can be terrible if `m` is much larger than the actual depth `d`, but it can be faster than Breadth-First Search (BFS) if there are many solutions.
    
- **Space Complexity:** $O(bm)$, which means it has linear space complexity.
    

## Iterative Deepening Search

**Iterative deepening search** is a strategy to prevent DFS from going down an infinite path. It uses DFS as a subroutine, iteratively increasing the depth limit.

1. Check the root.
2. Perform a DFS, searching for a path of length 1.
3. If no path of length 1 is found, perform a DFS searching for a path of length 2.
4. Continue this process, incrementing the depth limit until a solution is found.

![Diagrams illustrating iterative deepening search](https://api-turbo.ai/45450a35-daf0-4700-9927-791f2cad505f/dcd1736a-8947-42c7-9eb8-66de39b42a00.jpeg)

The image showcases the iterative process, demonstrating how the search expands layer by layer.

![Series of tree diagrams showing nodes from A-O](https://api-turbo.ai/45450a35-daf0-4700-991f2cad505f/1fb09559-991f-4df1-aba7-912dda4c1643.jpeg)

Here we see another visualization of iterative deepening, with each iteration exploring deeper levels of the tree.

### Properties of Iterative Deepening Search

- **Completeness:** Yes, it is complete.
- **Optimality:** Yes, if step costs are uniform (e.g., 1).
- **Time Complexity:** $(d+1)b^0 + d b^1 + (d-1)b^2 + … + b^d = O(b^d)$
- **Space Complexity:** $O(bd)$

