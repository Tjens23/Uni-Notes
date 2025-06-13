Graphs consist of: 
- A set $V$ of vertices  (nodes)
- A set $E \subseteq V \cdot V$ of edges, which are pairs of vertices. 
	- Directed graphs : edges are ordered pairs
	- Undirected graphs: Edges are unordered pairs
	- Weighted graphs: Each edge has an associated number (weight).
- Notation: 
	- `n = |V|` (number of vertices)
	- `m = |E|` (number of edges/nodes)
- -Note: $0 \leq m \leq n^2$ for directed graphs and $0 \leq m \leq (n^2 + n)/2$ for undirected graphs.

Graphs can model many things, including:
- Utility networks (telephone, electricity, oil, water)
- Road networks (intersections as vertices, roads as edges)
- Social media connections (friends, followers)
- Websites (WWW pages)
- Co-authorships


## Algorithmic Questions on Graphs

There are many algorithmic questions you could ask about graphs:

- How to represent graphs on a computer (data structure)?
- Is there a path between two given nodes?
- What is the shortest path between two given nodes?
- What is the smallest subset of edges that still keeps all nodes connected?
- What is the largest collection of edges where no edges share nodes?

One example of an algorithmic question is determining if there exists a path between two given nodes.

## Data Structures for Graphs

Two common data structures for graphs are **adjacency lists** and **adjacency matrices**.

- **Adjacency Lists**:
    - The list for vertex u contains v for all edges $(u, v) \in E$.
    - Nodes are represented as integers between 1 and `n` (or 0 and `n - 1`).
    - Space complexity: $O(n+m)$
- **Adjacency Matrix**:
    - Space complexity: $O(n^2)$


Unless otherwise specified, algorithms in this course use the **adjacency lists** representation. In undirected graphs, each edge is represented as two directed edges.

## Generic Graph Traversal

The goal is to visit all nodes and edges in a graph represented using adjacency lists to learn about different properties of the graph.

The general idea is to visit a start node `s` and use edges in the neighbor lists of visited nodes to visit more nodes. Mark nodes along the way to keep track of the process:

- **White nodes**: Not yet visited.
- **Gray nodes**: Visited, but not all edges in the neighbor list have been used.
- **Black nodes**: Visited, all edges in the neighbor list have been used.

The life cycle of a node is white →→ gray →→ black. When the algorithm stops, all nodes are either white or black.

Here is the pseudocode for a generic graph traversal algorithm:

![Pseudocode for a generic graph traversal algorithm.](https://api-turbo.ai/7bc6453d-d1af-489b-a468-47dedf45fbd2/f811ce75-78b4-45fd-a46a-9335c8d12ed3.jpeg)

## Graph Traversal Variants

Later in the course, we will encounter three variants with different strategies for choosing the next edge `(v, u)` to use:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Priority Search (Dijkstra's algorithm, A*)**



## Reachability in a Graph

A key theorem states that if there is a path from `s` to `v`, then `v` will be black (and therefore visited) when `GenericGraphTraversal1(s)` stops. The proof relies on the fact that if the algorithm stops, all nodes are either white or black, and any node `v` must be black if it's reachable from `s`.

To traverse the entire graph, a global approach can be used:

![Text boxes containing code written in a programming language, likely pseudocode.](https://api-turbo.ai/7bc6453d-d1af-489b-a468-47dedf45fbd2/57cfdca7-f55c-4c67-8ab9-75d336bd31a2.jpeg)

If the edge selection takes O(1)O(1) time, the total running time is O(n+m)O(n+m).

Another theorem states that if there is a path from `s` to `v` consisting of white nodes (including `v`) at the start of a call to `GenericGraphTraversal2(s)`, then `v` will be black when `GenericGraphTraversal2(s)` stops.

## Node Discovery and Predecessors

When a node `u` (≠s=s) is first visited, store the node that discovered `u` in the variable `u.π` (predecessor). The value of `u.π` is set at most once (after initialization to NIL) since `u` is made gray simultaneously.

![Text boxes containing pseudocode for graph traversal algorithms.](https://api-turbo.ai/7bc6453d-d1af-489b-a468-47dedf45fbd2/bd9312ce-93b7-4cda-aaf5-d33e05fcf5df.jpeg)

The nodes discovered in a call to `GenericGraphTraversal3(s)` form a tree with `s` as the root, and `π` in discovered nodes as parent pointers. For each path from a node `v` to the root in the tree, the same path exists in the graph, but in the opposite direction (from `s` to `v`). Each call to `GenericGraphTraversal3(s)` in `GenericGraphTraversalGlobalWithParents()` creates a tree. The trees from different calls do not share nodes and together contain all nodes in the graph.

## Breadth-First Search (BFS)

The strategy for BFS is to keep the gray nodes in a **queue** and process neighbor lists immediately. A variable `v.d` is added to all nodes `v` to represent **distance**. The most used version is without the Global part.

Invariant: The queue contains all gray nodes.

## Breadth-First Search (BFS) Example

![Technical diagram or schematic, comprising two columns of intricate illustrations.](https://api-turbo.ai/7bc6453d-d1af-489b-a468-47dedf45fbd2/4c73c6a4-b70a-4c71-a623-87d63d97224b.jpeg)

For BFS, the theorem about `GenericGraphTraversal3(s)` can be extended to include information about the values of `v.d`:

The nodes discovered in a call to `GenericGraphTraversal3(s)` form a tree with `s` as the root and `π` in discovered nodes as parent pointers. For each path from a node `v` to the root in the tree, the same path exists in the graph, but in the opposite direction (from `s` to `v`), and `v.d` is equal to the number of edges on this path. The value `v.d` is set at most once (after initialization to −∞−∞).

## Properties of BFS

- Running Time:  $O(n+m)$
- We define $\delta(s,v)$ as the length of the shortest path (measured in the number of edges) from the start node ss to the node $v$ if no path exists, $\delta(s,v)=\infty$ 
- **Theorem**: When BFS stops, $v,d = \delta(s,v)$ for all nodes.

This means BFS can find the shortest paths (measured in the number of edges) from $s$ to all $v$.

# Proof of BFS Theorem

The possible values for $\delta(s, v)$ are $0, 1, 2, 3, \ldots$ and $\infty$.

- For nodes $v$ with $\delta(s, v) = \infty$, there is no path from $s$ to $v$. Thus, $v$ cannot be discovered, and the value $v.d = \infty$ set during initialization cannot change. Therefore, when BFS stops, $v.d = \delta(s, v)$ for these nodes.
    
- For the remaining nodes, $\delta(s, v) = i < \infty$. For them, we show, via induction on $i$, that $\delta(s, v) = i \Rightarrow v.d = i$ when BFS stops.
    
    1. The BFS algorithm will extract all nodes with $d$-value equal to $i$ while inserting all nodes with $d$-value equal to $i + 1$.
        
    2. We already know that $\delta(s, v) \leq v.d$.
        

## Induction Proof

**Basis** ($i = 0$): If $\delta(s, v) = 0$, then $v = s$. BFS sets $s.d = 0$.

**Induction Step** ($i > 0$): We assume that $\delta(s, v) = i - 1 \Rightarrow v.d = i - 1$ is true and must show that $\delta(s, v) = i \Rightarrow v.d = i$ is true.

If $\delta(s, v) = i$, there exists a path from $s$ to $v$ of length $i$. For the penultimate node $u$ on this path, $\delta(s, u) = i - 1$. From the induction hypothesis, we have $u.d = \delta(s, u)$. Since $u$ was taken out of the queue, $v$ (a neighbor of $u$) was either undiscovered (white) and is now discovered by $u$, or $v$ was already discovered from a node $t$, which has $t.d \leq u.d$.

In BFS, $v$ is assigned a $d$-value that is one greater than the $d$-value of the node that discovers it. Thus, whether $v$ is discovered by $u$ or $v$, $v.d$ is set to at most $u.d + 1 = \delta(s, u) + 1 = (i - 1) + 1 = i = \delta(s, v)$. We know that $v.d$ is at least $\delta(s, v)$. In total, we have $v.d = \delta(s, v)$.

## Depth-First Search (DFS)

The strategy for DFS is to keep the gray nodes in a **stack** and advance minimally in the neighbor list each time we look at a node.

The stack is implicit in the recursive formulation (i.e., it is equal to the recursion stack), but can also be coded explicitly. More precisely, the elements on the stack are the gray nodes, each with a partially traversed neighbor list.

DFS also adds timestamps `u.d` for "discovery" (white → gray) and `u.f` for "finish" (gray → black) to all nodes `u`.


## Depth-First Search (DFS) Example

![Molecular structures, arranged in four rows of five diagrams each.](https://api-turbo.ai/7bc6453d-d1af-489b-a468-47dedf45fbd2/ad51d665-7e07-47ce-a700-1dda75f081db.jpeg)

## Properties of DFS

-  Running time: $O(n+m)$
- Discovery (white → gray) of $v$ = set $v.d$ = call of `DFS-Visit` on $v = \text{PUSH}$ of $v$ onto the stack.
- Finish (gray → black) of $v$ = set $v.f$ = return from call of `DFS-Visit` on $v$ = POP of $v$ from the stack.
- The value $v.\pi$ is set when calling `DFS-Visit` on v.

From this, it follows that:

- The edges (v.π,v)(v.π,v) form the recursion trees for `DFS-Visit` (one tree for each call from DFS).
- The interval [v.d,v.f]is the period v is on the stack.
- The node v is gray if and only if it is on the stack.

Because of how a stack works, if two nodes u and v are on the stack at the same time, and v is on top, then v must be popped before u can be popped.

The interval [v.d,v.f][v.d,v.f] is the period v is on the stack. Therefore, for all pairs of nodes u and v, the intervals [u.d,u.f] and [v.d,v.f]must either be disjoint (u and v were never on the stack at the same time) or one interval must be completely contained in the other (u and v were on the stack at the same time, the node with the largest interval came on first).

Discovery and finish times are therefore nested as parentheses are.

When an edge (u,v) is examined from u, the following cases exist:

1. **Tree-edges**: v is white.
2. **Back-edges**: v is gray (is on the stack).
3. **Forward-edges**: v is black (is no longer on the stack, but has been there with u).
4. **Cross-edges**: v is black (is no longer on the stack, and has not been there with u).



## Edge Classifications in DFS

1. **Tree-edges**: $v$ is white. Here, $u.d < v.d < v.f < u.f$.
2. **Back-edges**: $v$ is gray (is on the stack – it must be under $u$, which is the top of the stack). Here, $v.d \leq u.d < u.f \leq v.f$.
3. **Forward-edges**: $v$ is black (is no longer on the stack, but has been there with $u$). Here, $u.d < v.d < v.f < u.f$.
4. **Cross-edges**: $v$ is black (is no longer on the stack and has not been there with $u$). Here, $v.d < v.f < u.d < u.f$.

These cases can be recognized when an edge is examined during DFS, namely via the white/gray/black coloring and the d-values in the edge's two nodes.

For undirected graphs, there are only tree-edges and back-edges (as long as an edge is categorized the first time it is examined from one of its ends).

This follows from the fact that u must already have been examined from v if v is black (the entire neighbor list has been traversed), and the edge (v,u) must therefore already be categorized. Thus, cases 3 and 4 cannot occur.


## White-Path Lemma

If there exists a path of white nodes (including $w$) from $u$ to $w$ at time $u.d$, then $u.d < w.d < w.f < u.f$.

**Proof:**

Since the path is white at time $u.d$, $u.d \leq v.d$ for all nodes $v$ on the path. From the parenthesis structure for $d$- and $f$-times, either 1) $u.d \leq v.d < v.f \leq u.f$ or 2) $u.d < u.f < v.d < v.f$.

Assume that 2) occurs, and let $y$ be the first node on the path that satisfies 2) with $y$ inserted in $vs place. Then $y$ has a predecessor $x$ that satisfies 1) with $x$ inserted in $vs place. But because of the edge $(x, y)$, $y$ must be discovered before time $x.f$, which contradicts that $y$ satisfies 2).

## DAGs and Topological Sorting

- **DAG**: Directed Acyclic Graph. A directed graph without cycles.
- Often used to model dependencies.
- **Topological sorting** of a DAG: a linear ordering of the nodes such that all edges go from left to right.


## DAGs and Topological Sorting Lemma

An oriented graph has a cycle $\Leftrightarrow$ there are back-edges during a DFS traversal.

**Proof:**

$\Rightarrow$: DFS (with Global outer loop) discovers all nodes. Look at the first node $v$ in the cycle that turns gray. Thus, at time $v.d$, all other nodes are white.

From the white-path lemma, $v.d < u.d < u.f < v.f$ for the last node $u$ in the cycle (which points to $v$), whereby the edge $(u, v)$ is declared a back-edge ($v$ is gray when this edge is examined).

$\Leftarrow$: When a back-edge is found: There is a cycle of zero or more tree-edges (between nodes that are currently on the stack) and a back-edge.

## DAGs and Topological Sorting Lemma

For an edge $(u, v)$, $u.f \leq v.f \Leftrightarrow$ the edge is a back-edge.

**Proof:**

Check the four cases for edges (tree, back, forward, cross) and their ordering of $u.f$ and $v.f$.

**Corollary to the preceding lemmas:** Graph is a DAG $\Leftrightarrow$ DFS finds no back-edges $\Leftrightarrow$ ordering of nodes after decreasing finish times gives a topological sorting.

S˚a følgende algoritme finder en topologisk sortering i en DAG


![[{BB86BDBC-88D9-40CC-B535-500D4A4BB1B7}.png]]

Time: $O(n+m)$