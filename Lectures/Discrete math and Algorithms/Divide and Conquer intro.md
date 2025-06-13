**Divide-and-Conquer algorithms** are the same as **recursive algorithms**.

It's a general algorithm development method that involves:

1. Dividing a problem into smaller subproblems of the same type.
2. Solving the subproblems recursively, which means calling the algorithm itself but with smaller inputs.
3. Constructing a solution to the original problem from the solutions of the subproblems.

The **base case** involves solving problems of the smallest size directly without recursion.

##  General Structure of Divide-and-Conquer Code

The general structure of the code looks like this:

```
If base case:
    Local work (solve problem of base size)
Else:
    Local work (e.g., build one or more subproblems)
    Recursive call
    Local work (e.g., utilize answer to build next subproblem)
    Recursive call
    Local work (solve main problem based on answers to subproblems)
```

Note that there do not always have to be two recursive calls. Some recursive algorithms have just one, and some have more than two.

## 💫 Flow of Control in Divide-and-Conquer

Here's a locally set flow of control for one call of the algorithm:

- **Base case**
- **Non-base case**

## 🌳 Recursion Trees

**Global flow of control = recursion trees:**

- One node = one call of the algorithm.

Remember that all calls on a path from the root towards active calls are "in progress" but paused. Their local variables and other states are stored by the operating system on a stack, so the calls' executions do not mix.

- Calling a child in the recursion tree = push onto the stack.
- Finishing a child's execution = pop from the stack.

> **Stack**: A data structure used to store and manage the state of function calls during recursion. It ensures that each call's execution remains separate and that control returns to the correct point after a recursive call finishes.