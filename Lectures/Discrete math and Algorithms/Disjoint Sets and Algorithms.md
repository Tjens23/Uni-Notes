A **partition** of a set $S$ is a collection of non-empty subsets $A_i$, $i = 1, ..., k$, which are disjoint and together make up $S$.

- $A_i \neq \emptyset$ for all $i$
- $A_i \cap A_j = \emptyset$ for $i \neq j$
- $A_1 \cup A_2 \cup \cdots \cup A_k = S$

Example: ${a, b, e}, {f}, {c, d, g, h}$ is a partition of ${a, b, c, d, e, f, g, h}$.

### 🧱 Disjoint Sets Data Structure

Disjoint set as a data structure? The following collection of operations has proven relevant in many applications:

- **Make-Set(x)**: Create ${x}$ as a new set (x must not be an element in other sets).
- **Union(x, y)**: Merge ${a, b, c, ..., x}$ and ${h, i, j, ..., y}$ into ${a, b, c, ..., x, h, i, j, ..., y}$.
- **Find-Set(x)**: Return an ID for the set containing x.

Note: There are no requirements for the ID of sets. It should simply be the same for all x in the same set, so that we can check whether two elements x and y are in the same set.

### 🔗 Disjoint Sets via Linked Lists

Each set is a linked list of elements, with the ID for the set being the first element in the list:

- **Find-Set(x)**: Return (via header-pointer) the first element in the list.
- **Make-Set(x)**: Create a new list.
- **Union(x, y)**: Merge lists, keep one header, and change all header-pointers in the other list.

#### Runtime

(Where n is the number of elements, i.e., the number of Make-Sets performed?)

- **Find-Set(x)**: Return (via header-pointer) the first element in the list: $O(1)$.
- **Make-Set(x)**: Create a new list: $O(1)$.
- **Union(x, y)**: Merge lists, keep one header, change all header-pointers in the other list: $O(n)$.

Naive analysis: n Make-Set, up to n-1 Union, and m Find-Set costs $O(m + n^2)$.

#### Version 2

- **Find-Set(x)**: Return (via header-pointer) the first element in the list: $O(1)$.
- **Make-Set(x)**: Create a new list: $O(1)$.
- **Union(x, y)**: Merge lists, keep the header of the longest list, change all header-pointers in the shortest list: $O(n)$.

Observe that now a node can only change its header-pointer $log n$ times, since the size of its set each time grows by at least a factor of two ($1 \cdot 2^k \leq n \Leftrightarrow k \leq log n$).

A better analysis: n Make-Set, up to n-1 Union, and m Find-Set costs $O(m + n log n)$.

### 🌲 Disjoint Sets via Trees

Each set is a tree with elements in nodes, and the root is the ID for the set:

- **Find-Set(x)**: Go to the root.
- **Make-Set(x)**: Create a new tree.
- **Union(x, y)**: Make the root of one tree a child of the other tree.

#### Version 2

**Union by rank**: Add an integer (rank) to all roots. Set to 0 for new trees (during Make-Set(x)). Controls the parent-child decision during Union(x, y): the root with the largest rank gets the other root as a child. In case of equal rank, let y get x as a child and increase y’s rank by 1.

**Path compression**: During Find-Set(x), set all passed nodes as children of the root.

Union by rank and path compression ⇒ very close to $O(m + n)$ time. More precisely, $O(m \cdot \alpha(n) + n)$, where $\alpha(n)$ is a very slowly growing function.

The function $\alpha(n)$ and the proof for the runtime can be found in section 19.4, which is not part of the curriculum (reviewed in a later course at the computer science program).

#### Pseudocode

Pseudocode (with union by rank and path compression) is surprisingly simple.