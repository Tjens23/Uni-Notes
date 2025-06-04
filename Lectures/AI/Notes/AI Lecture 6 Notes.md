---
tags:
  - Notes
links: "[[AI Lecture 6]]"
creation date: 2025-05-21 13:57
modification date: Wednesday 21st May 2025 13:57:04
semester: 4
year: 2025
---


---
# [[AI Lecture 6 Notes]]

---



## 🎮 Games and Adversarial Search

This section delves into environments where multiple agents, often with conflicting goals, interact. These are **competitive, multiagent environments** where other agents might be actively working against us. Examples include games like Chess, Go, and Poker.

### 🤔 Why Study Games?

- Games have traditionally been seen as a **hallmark of intelligence**.
- They are **easy to formalize**, making them suitable for study.
- Games provide a good model for **real-world competitive activities**, such as military confrontations, negotiations, and auctions.

### 🕹️ Types of Game Environments

|                        | Deterministic      | Stochastic           |
|------------------------|-------------------|---------------------|
| **Perfect Information**    | Chess, Checkers, Go | Backgammon, Monopoly |
| **Imperfect Information**  | Battleships       | Scrabble, Bridge     |

### ⚔️ Alternating Two-Player Zero-Sum Games

- Players take turns.
- **Zero-sum:** One player's gain is equivalent to the other's loss; there's no win-win.
- Each player has a **utility** for each game outcome (e.g., 1 for win, 0 for loss).
- The **sum of both players' utilities is constant**.

### ♟️ Games vs. Single-Agent Search

- In games, the opponent's actions are unknown. Thus, we need a **strategy or policy**, which maps each state to the best move in that state.
- **Efficiency is critical** due to limited time, large branching factors, search depths, and numerous terminal configurations.
- For example, in chess, the branching factor is ≈ 35, and the depth is ≈ 80 ply, resulting in a search tree of approximately 35<sup>80</sup> ≈ 10<sup>123</sup> nodes. Exhaustive search isn't feasible.

### 🌳 Game Tree

A **game tree** is a visual representation of a game's possible states and transitions, alternating between "MAX" nodes (representing the maximizing player) and "MIN" nodes (representing the minimizing player).

![Game Tree Example](https://api-turbo.ai/55b487ec-5a80-4c9d-8a57-7a254b206389/977eac41-67e2-43e3-b037-e78acf686c05.jpeg)

The image above illustrates a game tree for Tic Tac Toe, with nodes representing game states and branches showing possible moves. The tree alternates between "MAX (X)" and "MIN (O)" nodes, terminating at leaf nodes with utility values (-1, 0, or +1).

### 💡 Minimax Algorithm

- **Minimax value of a node:** The utility (for MAX) of being in the corresponding state, assuming perfect play on both sides.
- **Minimax strategy:** Choose the move that gives the best worst-case payoff.

#### Computing the Minimax Value of a State

The minimax value of a state can be computed recursively as follows:

$$\text{Minimax}(\text{state}) = \begin{cases}
\text{Utility}(\text{state}) & \text{if state is terminal} \\
\max \text{Minimax}(\text{successors}(\text{state})) & \text{if player = MAX} \\
\min \text{Minimax}(\text{successors}(\text{state})) & \text{if player = MIN}
\end{cases}$$

The minimax strategy is optimal against an optimal opponent. If the opponent is suboptimal, the utility can only be higher. While a different strategy might perform better against a suboptimal opponent, it will necessarily be worse against an optimal opponent.

### 🪙 Coins Game Example

Consider a game with a stack of N coins. Players take turns removing 1, 2, or 3 coins. The player who takes the last coin loses.

- **Initial State:** The number of coins in the stack.
- **Operators:**
    1. Remove one coin
    2. Remove two coins
    3. Remove three coins
- **Terminal Test:** There are no coins left on the stack.
- **Utility Function:** F(S) = 1 if MAX wins, 0 if MIN wins

In this example, even with a trivial setup, the game trees can become very large, highlighting the exponential complexity O(b<sup>d</sup>), where `b` is the branching factor and `d` is the depth of the tree.

### ✂️ Alpha-Beta Pruning

To improve the performance of the minimax algorithm, **alpha-beta pruning** can be used. As Pat Winston from MIT put it, "If you have an idea that is surely bad, don't take the time to see how truly awful it is."

- **Main idea:** Avoid processing subtrees that have no effect on the result.
- **Two new parameters:**
    - **α:** The best (highest) value for MAX seen so far.
    - **β:** The best (lowest) value for MIN seen so far.
- α is used in MIN nodes and assigned in MAX nodes (Think: α = "at least").
- β is used in MAX nodes and assigned in MIN nodes (Think: β = "at most").

#### Alpha-Beta Pruning Rules

- Traverse the tree in depth-first order.
- At MAX node `n`, α(n) = max value found so far. Alpha values start at -∞ and only increase.
- At MIN node `n`, β(n) = min value found so far. Beta values start at +∞ and only decrease.
- **Beta cutoff:** Stop the search below MAX node N if α(N) >= β(i) for some MIN node ancestor `i` of N.
- **Alpha cutoff:** Stop the search below MIN node N if β(N) <= α(i) for a MAX node ancestor `i` of N.

Alpha-beta pruning allows the computation of the exact minimax decision without expanding every node in the game tree.

### 🎲 Games of Chance

To incorporate chance (e.g., dice throwing) into the game tree:

- **Expectiminimax:** For chance nodes, average values weighted by the probability of each outcome. This results in a nasty branching factor, making evaluation functions and pruning algorithms more difficult.
- **Monte Carlo simulation:** When a chance node is reached, simulate a large number of games with random dice rolls and use the win percentage as the evaluation function. This can work well for games like Backgammon.

### 🏆 Game Playing Algorithms Today

- Computers are better than humans in some games:
    - Checkers: solved in 2007
    - Chess: IBM Deep Blue defeated Kasparov in 1997
- Computers are competitive with top human players in others:
    - Backgammon: TD-Gammon used reinforcement learning.
    - Bridge: Top systems use Monte Carlo simulation and alpha-beta search.
- Computers are becoming increasingly competitive in more complex games:
    - Go: AlphaGo uses a Monte Carlo tree search based on knowledge learned by a deep learning neural network.
    - StarCraft II: Google AI beats top human players.

### 📜 Origins of Game Playing Algorithms

- **Ernst Zermelo (1912):** Minimax algorithm
- **Claude Shannon (1949):** Chess playing with evaluation function
- **John McCarthy (1956):** Alpha-beta search
- **Arthur Samuel (1956):** Checkers program that learns its own evaluation function by playing against itself