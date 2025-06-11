### Datastructures (Recap)

> Datastructure = **data** + **operations** on data.

- **Data**: An ID (**key**) + associated data
- **Operations**: The properties of the datastructure are made up of the offered operations (**API** for data access), as well as their runtimes. Different implementations of the same API can give different runtimes.

### Priority Queue

Datastructure that supports the operations:

- **Extract-Min()**: Remove an element with the smallest key from the priority queue and return it.
- **Insert(key)**: Add new element to the priority queue.
- **Build(list of elements)**: Build a priority queue containing the elements.
- **Decrease-Key(key, reference to element in queue)**: Sets the key for the element to min{key, old key}.

## 📖 Dictionaries

Datastructure that supports the operations:

- **Search(key)**: return element with the key `key` (or tell if it does not exist).
- **Insert(key)**: Insert new element with the key `key`.
- **Delete(key)**: Remove element with the key `key`.
- **Predecessor(key)**: Find the element with the highest key < `key`.
- **Successor(key)**: Find the element with the lowest key > `key`.
- **OrderedTraversal()**: Print elements in sorted order.

For the last three operations it is required that the keys have an ordering. If only the first three operations are to be supported, it is called an **unordered dictionary**. If all six are supported, it is called an **ordered dictionary**.

### Implementations

Dictionaries in:

- **Java**: interface `Map`
- **Python**: `dict`

Implementations:

- **Balanced binary search trees**: Supports all of the above operations in $O(log n)$ time.
- **Hashing**: Supports the first three operations expected time $O(1)$.

These implementations exist in Java as respectively `TreeMap` and `HashMap`. In Python, the built-in datatype `dict` is implemented with hashing. There are no balanced binary search trees in Python's standard modules, but one can find modules with them from other sources.

## 🌲 Binary Search Tree

- A binary tree
- With nodes in inorder

> A binary tree with keys in all nodes observes inorder if it for all nodes `v` applies: keys in `v`'s left subtree ≤ key in `v` ≤ keys in `v`'s right subtree

### Typical Implementation

Node-objects with:

- Reference to parent
- Reference to left subtree
- Reference to right subtree

As well as a tree-object with reference to the root.

### Node Objects

Java class for nodes:

```java
class  Node {
	int key;
	Node leftchild;
	Node rightchild;
	Node parent;
	... (constructor)
	... (other methods)
}
```

Python class for nodes:

```python
class Node:
	def __init__(self):
		self.key = None
		self.leftchild = None
		self.rightchild = None
		self.parent = None
		... (other methods)
```


Python via lists:

`Node = [key, leftchild, rightchild, parent]`


### Inorder

Because of the definition of inorder

> keys in v’s left subtree ≤ key in v ≤ keys in v’s right subtree

Binary search trees are said to contain data in sorted order. More precisely: inorder traversal will print keys in sorted order, with a runtime of $O(n)$ (O(1) work per node in the tree).


### Search in Binary Search Trees

If the element searched for exists, it is in the subtree we have reached.

### Insertions in Binary Search Trees

- Search downwards from root: in each node `v` met, continue down in the subtree (right/left), where the new element should be according to inorder-requirement for `v`.
- When leaf (NIL/empty subtree) is reached, replace this with the new node (with two empty subtrees).

Inorder is observed for nodes on search path (because of search rule), and for all other nodes (because they have not gotten any new descendants in their two subtrees).

### Deletions in Binary Search Trees

Deletion of node z:

- **Case 1**: At least one child is NIL: Remove z as well as this child, let other child take z’s place.
- **Case 2**: No children are NIL: Then the successor-node y to z is the smallest node in z’s right subtree. Remove y (which is a Case 1 removal, since its left child is NIL), and insert it in z’s place.

Both cases leave the tree in inorder: In Case 1 no nodes get new descendants in their two subtrees. In Case 2 y (and only y) get new descendants in its two subtrees, but since y is z’s successor, there are no keys in the tree with value between z’s and y’s keys, so the keys in y’s new subtrees observe inorder in relation to y, since they did in relation to z.

Structurally in the tree, all deletions are a Case 1 deletion.

### Time for Operations in Binary Search Trees

For all operations (except inorder traversal): traverse path from root to leaf. I.e. runtime = $O(\text{height})$
A tree with height `h` cannot contain more nodes than the full tree with height `h`. This contains $2^{h+1}-1$ nodes.

So for a tree with `n` nodes and height `h` applies:

$n\leq 2^{h+1}-1\leftrightarrow \log_{2}{n+1}-1\leq h$

The best possible height is $\log{n} (\pm1)$. Can we keep the height close to optimal – e.g. $O(\log{ n})$ – during updates (insertions and deletions)?

## Balanced Binary Search Trees

Can we keep the height $O(log n)$ during updates (insertions and deletions)?

Requires rebalancing (restructuring of the tree) after updates, since deep trees can otherwise occur. Maintenance of $O(log n)$ height first achieved with AVL-trees [1961]. Many later suggestions. A suggestion consists of:
- Balance information in nodes.
- Structure requirements based on balance information, which ensures $O(log n)$ height.
- Algorithms which restore the structure after an update.

### Red-Black Trees

Balanceinformation in nodes: 1 bit (called red/black color).

Structure requirements:

- Root and leaves black.
- Same number of black on all root-leaf paths.
- Not two red in a row on any root-leaf path.

Note: the concept leaves are in red-black trees used about NIL-subtrees (which technically increases the height of a tree by one).

Structure requirements (recap):

- Root and leaves black.
- Same number of black on all root-leaf paths.
- Not two red in a row on any root-leaf path.

Do these structure requirements ensure $O(log n)$ height? Yes:

Let the number of black on all root-leaf paths be k (i.e. k−1 black nodes plus a black leaf). Then all root-leaf paths contain at least k −1 nodes (the black plus perhaps some red). There are therefore at least k−1 full layers of nodes in the tree.

Therefore is $n \geq 2^{0}+2^{1}+2^{2}+\dots + 2^{k-2} = 2^{k-1}-1$
From this follows $\log(n+1)\geq k−1\log(n+1)\geq k−1$.
Since there are not two red nodes in a row, the longest root-leaf path contains at most 2(k −1) 
edges.


so the height is at most $2(k-1)\leq 2\log(n+1)=O(\log{n})$


### Insertion

1. Insert a node in the tree
2. Remove any arising unbalance (violation of red-black structure requirements).

Recall insertion: a leaf (NIL) is replaced by a node with two leaves as children.

### Unbalance

Recall insertion: a leaf (NIL) is replaced by a node with two leaves as children.

Violation of red-black structure requirements?

- Root and leaves black.
- Same number of black on all root-leaf paths.
- Not two red in a row on any root-leaf path.

The two new leaves must be black.

We choose to make the new inserted node red.

Possible violation of structure requirements now: Two red nodes in a row on a root-leaf path one place in the tree.

Idea for plan: If the problem cannot be solved immediately, then push it upwards in the tree until it can (hopefully easy to do, if it reaches the root).

### Rebalancing

  

Detailed plan: push red-red problem upwards in the tree, under use of recolorings and restructurings of the tree.

  

The basic restructuring will be a rotation ($\alpha,\beta,\gamma$ are subtrees, perhaps empty):

  

Central observation: Rotations cannot destroy in-order in the tree:

  

Only $x$ and $y$ can get inorder violated (all other nodes have the same elements in their subtrees before and after). But this does not happen, since the following applies both before and after a rotation:

  

$\text{keys in } \alpha \leq x \leq \text{keys in } \beta \leq y \leq \text{keys in } \gamma$

  

So we do not have to worry about preservation of inorder, if we only restructure using rotations.

  

### Plan for Rebalancing (after insertion)

  

Recap of plan: push red-red problem upwards in the tree, under use of recolorings and restructurings (rotations) of the tree.

  

Principle along the way:

  

- Two red nodes in a row on a root-leaf path at most one place in the tree.

- Apart from this, the red-black requirements are observed.

  

Goal: In $O(1)$ time, remove the problem or push it one step closer to the root.

  

This will give rebalancing in $O(\text{height}) = O(\log n)$ time.

  

### Cases in Rebalancing (after insertion)

  

Case 1: Red uncle to $z$ (uncle = parent's sibling $y$).

  

Case 2: Black uncle to $z$ (uncle = parent's sibling $y$).

  

Here $z$ is the lowest node in the red-red problem. Check that principle is maintained. Check that problem is removed or moved closer to the root (one fewer black node on path to root). If $z$ becomes the root, it can simply be colored black ($\Rightarrow$ all paths get one more black).

  

### Deletion

  

1. Delete a node in the tree  

2. Remove any arising unbalance (violation of red-black requirements)

  

Recall deletion: there is structurally always removed one node whose one child is a leaf (NIL), which is also removed.

  

### Unbalance?

  

Violation of red-black requirements?

  

- Root and leaves black.

- Same number of black on all root-leaf paths.

- Not two red in a row on any root-leaf path.

  

Removed node red: All red-black requirements still observed.

  

Removed node black: Not longer same number of black on all paths.

  

Very useful formulation:

  

Let the removed node's other child be "blackened" and count for "one more" black than its color indicates, when we count black on paths (blackened black = 2 black, blackened red = 1 black). Then the requirements are observed, except for the existence of a blackened node.

  

Idea for plan: If the problem cannot be solved immediately, then push it upwards in the tree until it can (hopefully easy to do, if it reaches the root).

  

### Rebalancing

  

Push blackened node upwards in the tree, under use of recolorings and rotations:

  

Principle along the way:

  

- At most one node in the tree is blackened.

- If the blackening is counted, the red-black requirements are observed.

  

Easy stop cases:

  

- Blackened node is red $\Rightarrow$ blackening can be removed by coloring the node black.

- Blackened node is root $\Rightarrow$ blackening can just be removed ($\Rightarrow$ all paths get one black less).

  

(So enough to look at the case that the blackened node is black.)

  

Goal: In $O(1)$ time, remove the problem or push it one step closer to the root.

  

This will give rebalancing in $O(\text{height}) = O(\log n)$ time.

  

Cases for blackened black node $x$ with sibling $w$:

  

1. Red sibling.  

2. Black sibling, and this has two black children.  

3. Black sibling, and this' closest child is red, the furthest black.  

4. Black sibling, and this' furthest child is red.  

  

Here $x$ is blackened node. Check that principle is maintained. Check $O(1)$ time before blackening is removed or moved one step closer to the root.

  

## 🗄️ Hashing

  

In hashing, it is assumed that keys are integers up to a max-limit $u$.

  

That is, we have a universe of possible integer keys: $U = \{0, 1, 2, \dots, u-1\}$

  

The starting point in hashing is (just like in Counting sort) the idea about using keys as indexes in an array:

  

This takes $O(1)$ time for Search, Insert and Delete.

  

### Problem: Space Consumption

  

This idea can easily generate wasted space, because array-size is $u = |U|$, while the number $n = |K|$ of stored elements often is much smaller.

  

Example: store 5 CPR-numbers. I.e. keys of the type 180781-2345, that can be seen as integers in $U = \{0, 1, 2, \dots, 10^{10}-1\}$. Here is $u = 10^{10}$, while $n=5$.

  

So we use at least $10^{10}$ bytes ($> 8$ Gb RAM) to store 5 CPR-numbers.

  

If 32 or 64 bits integers are stored, then $u = 2^{32} \approx 10^{10}$ or $u = 2^{64} \approx 10^{20}$. That is, same situation or much worse.

  

### Hash Functions

  

A solution to the problem with space consumption: find a function $h$, which maps from key's large universe $U$ to a smaller:

  

$$

h: U \rightarrow \{0, 1, 2, \dots, m-1\}

$$

  

Here $m$ is the wanted array-size. Often $m = O(n)$ is chosen, so not more space is used on the array than on the elements themselves.

  

Such a function is called a **hash function**. An example of a hash function can be:

  

$$

h(k) = k \bmod m

$$

  

Concrete example with $m = 41$:

  

- $h(12) = 12 \bmod 41 = 12$ (since $0 \cdot 41 + 12 = 12$)  

- $h(100) = 100 \bmod 41 = 18$ (since $2 \cdot 41 + 18 = 100$)  

- $h(479869) = 479869 \bmod 41 = 5$ (since $11704 \cdot 41 + 5 = 479869$)

  

### Collisions

  

Hash functions solve the problem with space consumption. But they generate another problem: Two keys can hash to the same array index.

  

- $h(479869) = 479869 \bmod 41 = 5$ (since $11704 \cdot 41 + 5 = 479869$)

- $h(46) = 46 \bmod 41 = 5$ (since $1 \cdot 41 + 5 = 46$)

  

This is called a **collision**.

  

When $h$ must map $U$ into a smaller set $\{0, 1, 2, \dots, m-1\}$, there will always be some keys $k$ and $k'$ where $h(k) = h(k')$. So collisions cannot be avoided, and we must therefore find a solution.


### Chaining


One simple solution: an array-entry contains the start of a linked list with all the inserted elements, whose key hashes to this array-entry.

  

This is called **chaining**.


The price is that linked lists must be traversed during Search and Delete, whereby the time for these operations increases from $\Theta(1)$ to $\Theta(\text{|list|})$. Insert is still $O(1)$, since we can just insert first in the list.

### Open Addressing

Open addressing is an alternative to chaining: Try to find empty slot in the array itself.

- Linear probing (alias linear hashing):
	- $h(k,i)=(h_{1}(k)+i)\mod m$
- **Quadratic hashing**:
	- $h(k,i)=(h_{1}(k)+c_{1}\cdot i + c_{2}\cdot i^{2})\mod m$
- **Double hashing**
	- $h(k,i)=(h_{1}​(k)+i⋅h_{2}​(k))\mod m$

Here $h_1(k)$ and $h_2(k)$ are two hash-functions (called "auxiliary" in book).

Insert: `i = 0, 1, 2, ...` are tried until an empty slot is found.

Search: `i = 0, 1, 2, ...` are tried until element or empty slot is found.

### Open Addressing, Remarks

- At implementing Delete is more complicated. A simple solution: let deleted elements stand, mark them as deleted, clean up once in a while by rebuilding the hash table (insert the remaining elements from the beginning). For linear hashing there is a more direct method, see Cormen et al. 4. edition, section 11.5.1 (not curriculum).
- It is necessary that `n ≤ m` (since all n elements are in the array). Preferably `n ≈ m/4` to avoid runtimes degenerate.
- The searched indexes `{h(k,0), h(k,1), h(k,2), ..., h(k,m-1)}` should be `{0, 1, 2, ..., m-1}` for all k (so the whole array is searched). This can e.g. be ensured by choosing m as a prime number.

### Runtime for Hashing

We want a hash-function `h` which spreads keys from the concrete input well out over `{0, 1, 2, ... m-1}`, so there will be few collisions. One often thinks of good hash-functions as some that map keys to indexes in an apparently random way.

However, for a given hash function, one can always find at least `|U|/m` (i.e. `u/m`) keys, which hashes to the same array-index. Often `u/m > n`, which makes worst case time to Θ(n).

In practice, one often just hopes that this does not happen for one's concrete input and concrete choice of hash function. There are actually methods to guarantee that this rarely happens.

In practice, one can expect that hashing supports Search, Insert and Delete in $O(1)$ runtime, unless one is very unlucky.

One can also lower worst case time to $O(log n)$ by using balanced search trees instead of linked lists in chaining. This is what Java does, when the linked list gets big.

### Universal Hashing

Consider the following family of hash functions:
$$h(k)=((a⋅k+b)\mod  p)\mod  m$$
where `p` is a fixed prime number larger than `|U|` and `a,b` are fixed, but randomly chosen integers with `1 ≤ a ≤ p-1` and `0 ≤ b ≤ p-1`.

One can prove that above hashfunction is good in the following sense (called universal hashing):

For all datasets we can for a random choice of `a` and `b` expect so few collisions that the operations (Search, Insert, Delete) takes $O(1)$ time.

### Other Uses of Hash functions

Hash functions have many use areas, besides as implementation of unordered dictionaries.

Some examples:

- Fingerprint of files and documents.
- Digital signatures.
- Load balancing
- Coordinated sampling

The different uses have each their specific requirements for the hash functions.