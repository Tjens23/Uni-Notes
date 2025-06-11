### Adding Extra Information to Nodes

Binary search trees can be augmented by storing additional information in each node.

For example, each node could store the size of its subtree (i.e., the number of nodes in its subtree).

### New Functionality via Augmentation

The goal of adding extra information to nodes is to introduce new functionalities. For instance, with subtree sizes stored, operations like finding the rank of a given key or finding the key with a given rank can be performed in $O(\log{n})$ time.

> Rank: The rank of a key is its index in sorted order among the stored keys.
> 
> Example: Keys: 3 7 10 12 14 14 16 17 19 20 21 ... Ranks: 1 2 3 4 5 6 7 8 9 10 11 ...

### Implementation of New Functionality

With subtree sizes stored in each node, we can implement:

- Finding the rank of a given key.
- Finding the key which has a given rank.

###  Maintaining Extra Information in Nodes

Assume the following property holds for the extra information: If a node's two children have correct values $k1$​ and $k2$​, the node's own value, kk, can be computed in $O(1)$ time. Leaf values can also be computed in $O(1)$ time.

In the subtree size example, $k$ can be found as $1+k1+k2$.

The values can be maintained during updates in red-black search trees without affecting the $O(\log{n})$ runtime:

- Nodes outside the path from the inserted/deleted node to the root do not need to have their values changed (bottom-up computation gives unchanged results).
- During rebalancing, recompute for affected nodes after each rotation and after each step upwards. Finally, recompute on the path from the last rebalancing spot to the root.

###  Other Examples of Useful Extra Information

The maintenance system described works when: If a node's two children have correct values $k1$​ and $k2$, the node's own value,  $k$, can be computed in $O(1)$ time. Leaf values can also be computed in $O(1)$ time.

Consider that each element has associated data (a number) in addition to the search key. Here are a few examples of information that satisfies this criterion:

- Maximum of data values in the subtree.
- Minimum of data values in the subtree.
- Sum of data values in the subtree.

With such information, additional functionality can be added to the tree. For instance, one can search for elements with the maximum data value or find the average of the data values in a node's subtree (average = sum of data values / number of nodes).