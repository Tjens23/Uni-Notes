---
tags:
  - Notes
links: "[[AI Lecture 5]]"
creation date: 2025-05-21 13:54
modification date: Wednesday 21st May 2025 13:54:00
semester: 4
year: 2025
---


---
# [[AI Lecture 5 Notes]]

---



## 🧐 Local Search Algorithms

Some search problems can be formulated as optimization problems. In these problems:

- We don't have a start state.
- We don't care about the path to a solution.
- We have an **objective function** that tells us about the quality of a possible solution.
- We want to find a good solution by minimizing or maximizing the value of this function.

## 🪜 Approaches

- **Hill Climbing**
- **Simulated Annealing**
- **Genetic Algorithms**

## ⛰️ Hill-Climbing (Greedy) Search

The main idea behind hill-climbing is to keep a single "current" state and try to locally improve it.

> The analogy for hill-climbing is "Like climbing Mount Everest in thick fog with amnesia."

One way to use Hill-climbing is to use the negative of a heuristic distance to the goal.

The image illustrates the Hill Climbing algorithm, a heuristic search technique. The diagram illustrates the process of finding an optimal solution by iteratively moving towards a better state.

![Illustration of the Hill Climbing algorithm](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/698f34ad-99a2-4c55-b086-afb1c0020608.jpeg)

For example, a possible heuristic function, $f(n)$, can be defined as the negative of the number of tiles out of place:

$f(n) = -(\text{number of tiles out of place})$

## ✈️ Example: Traveling Salesman Problem

The traveling salesman problem seeks to find the shortest tour connecting a given set of cities.

- **State space**: all possible tours
- **Objective function**: length of tour
- **Possible local improvement strategy**: Start with any complete tour and perform pairwise exchanges.

![A map of the United States with a route traversing the country, visualizing the Traveling Salesman Problem](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/14cf0c29-84d4-41d9-976e-dc17f508a9b8.jpeg)

The image depicts a map of the United States with a blue route line traversing the country. The route begins in Washington state, marked by a green pin, and ends in San Diego, California, marked by a red pin.

![A visual representation of a graph transformation, showcasing node connections and alterations in the graph structure.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/2bc855f4-1916-43e4-962f-a5beaa5c2b93.jpeg)

The image presents a visual representation of a graph transformation, comprising two graphs side by side.

## 👑 Example: n-queens problem

The n-queens problem involves placing n queens on an n × n board such that no two queens attack each other (i.e., no two queens are on the same row, column, or diagonal).

- **State space**: all possible n-queen configurations
- **Objective function**: number of pairwise conflicts
- **Possible local improvement strategy**: Move one queen within its column to reduce conflicts

![Visual representation of two 4x4 checkerboards, each with three black crowns placed on specific squares.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/8c740db0-f124-4c44-9139-fe7564724f3b.jpeg)

The image depicts two 4x4 checkerboards, each featuring three black crowns placed on specific squares. The crowns on each board are situated in different locations.

![Progression of three chessboards, illustrating a problem-solving or optimization process related to the n-queens puzzle.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/3956d790-cfcd-4a76-b952-bda4d4bdfe16.jpeg)

The image displays a sequence of three chessboards with black and white squares, each containing four black hand-like figures, representing the queens.

![A 10x10 grid with numerical values and crown icons, representing an example of a hill-climbing solution to the n-queens problem.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/8df726ad-bd8a-4e20-bbdb-951597ec6e78.jpeg)

The figure has a heuristic cost estimate value of h=17, the number of conflicting pairs of queens. The figure gives the estimate of each successor state. The successor function returns all possible 8*7=56 states reachable after a given move in a column.

![Sudoku puzzle grid with numerical values and crown symbols, illustrating an example of a problem-solving or optimization process.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/df96558d-d589-4ee7-93dd-86212b5258ed.jpeg)

The image is a grey and white Sudoku puzzle grid, in which some numbers are already filled in, ranging from 12 to 18, while others remain blank; there are also five black crown symbols present.

![Visual puzzle comprising three chessboards, each with a distinct arrangement of black crowns, showcasing an example solution to the n-queens problem.](https://api-turbo.ai/c90e0eff-6ec2-b2c2-7b03-4cc9-9748-b8df972c7b0e.jpeg)

The image presents a visual puzzle comprising three chessboards, each with a distinct arrangement of black crowns or hand-like symbols on a gray and white checkered background.

## 💻 Hill-Climbing Algorithm

- Initialize `current` to starting state
    
- Loop:
    
    - Let `next` = highest-valued successor of `current`
    - If `value(next) < value(current)` return `current`
    - Else let `current = next`
- Variants: choose first better successor, randomly choose among better successors
    

## 🛑 Limitations of Hill-Climbing

- **Completeness**: No
- **Optimality**: No
- Can get stuck in **local optima** (peak higher than neighbors but lower than global maximum)

![Line graph illustrating a local maximum and a global maximum, representing the challenges of the Hill Climbing algorithm](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/fc1b7b7e-e7bd-4508-96e1-d45ac722f3da.jpeg)

The line graph presents a visual representation of a local maximum and a global maximum, key concepts in understanding the challenges of the Hill Climbing algorithm.

![Chessboard with eight black crowns and the notation "h=15", representing the state space "landscape."](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/45eb202f-de6c-41c0-8b4a-47b19d2c3839.jpeg)

The chessboard illustrates the state space "landscape," a concept used to visualize the search space in optimization problems.

![Graph illustrating an objective function with labeled points, visualizing the optimization landscape.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/14904f90-1ded-42ac-92c8-ef1faffb21e0.jpeg)

The graph illustrates an objective function, which is a mathematical representation used to optimize a problem.

One way to escape local maxima is to iteratively perform hill-climbing, each time with a random initial condition. The best result is kept; if a new run of hill climbing produces a better state than the stored state, it replaces the stored state.

## 🌡️ Simulated Annealing Search

The hill-climbing algorithm never makes downhill moves and is always incomplete. Simulated annealing addresses this by escaping local maxima by allowing some "bad" moves but gradually decreasing their frequency.

- Probability of taking downhill move decreases with number of iterations, steepness of downhill move.
- Controlled by annealing schedule.

It is inspired by the annealing process used to harden metals and glass by heating them to a high temperature and then gradually cooling them, thus allowing the material to reach a low-energy crystalline state.

## ⚙️ Simulated Annealing Algorithm

- Initialize `current` to starting state
    
- For `i = 1 to ∞`:
    
    - Let `T = Schedule(t)`
    - Let `next` = random successor of `current`
    - Let `Δ = value(next) – value(current)`
    - If `Δ > 0` then let `current = next`
    - Else let `current = next` with probability `exp(Δ/T(i))`

The schedule, as the algorithm input, determines the value of the “Temperature” $T$ as a function of time. $T$ gradually decreased to 0 over time t. Picks random rather than best state move as in hill-climbing. If move is an improvement over the current state, always accepted, otherwise accepted with probability < 1. Probability decreases exponentially when move is worse than current and as T decreases over time; bad moves more likely to be accepted early.

$$T \to 0, \quad \Delta/T(i) \to -\infty, \quad \exp(\Delta/T(i)) \to 0, \quad \Delta < 0$$

![Graph illustrating the relationship between exp(Δ/T) and Δ for various temperatures, showcasing the effect of temperature on simulated annealing.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/388e92c3-a01e-40f8-bb4b-3d75b8b910d4.jpeg)

The image presents a graph illustrating the relationship between exp⁡(Δ/T)exp(Δ/T) and ΔΔ for various temperatures, denoted as TT.

## 📉 Properties of Simulated Annealing

One can prove: If temperature decreases slowly enough, then simulated annealing search will find a global optimum with probability approaching one.

However:

- This usually takes impractically long.
- The more downhill steps you need to escape a local optimum, the less likely you are to make all of them in a row.
- More modern techniques: general family of Markov Chain Monte Carlo (MCMC) algorithms for exploring complicated state spaces.

## 🧬 Genetic Algorithms - History

- Pioneered by John Holland in the 1970’s
- Got popular in the late 1980’s
- Based on ideas from Darwinian Evolution
- Can be used to solve a variety of problems that are not easy to solve using other techniques

## 🌍 Evolution in the Real World

- Each cell of a living thing contains **chromosomes** - strings of DNA
- Each chromosome contains a set of **genes** - blocks of DNA
- Each gene determines some aspect of the organism (like eye color)
- A collection of genes is sometimes called a **genotype**
- A collection of aspects (like eye color) is sometimes called a **phenotype**
- Reproduction involves recombination of genes from parents and then small amounts of mutation (errors) in copying
- The **fitness** of an organism is how much it can reproduce before it dies
- Evolution based on “survival of the fittest”
- Suppose you have a problem. You don’t know how to solve it. What can you do?

![Illustration of the structural components of a cell, highlighting the relationship between a cell, chromosome, DNA molecule, and gene.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/c5b3b186-4a63-4c3f-a970-eabae28e4fdd.jpeg)

The image is a detailed illustration of the structural components of a cell, specifically highlighting the relationship between a cell, chromosome, DNA molecule, and gene.

## 😵‍💫 A Dumb Solution

A “blind generate and test” algorithm:

```
Repeat
    Generate a random possible solution
    Test the solution and see how good it is
Until solution is good enough
```

### Can we use this dumb idea?

- Sometimes - yes:
    
    - if there are only a few possible
    - and you have enough time
    - then such a method could be used
- For most problems - no:
    
    - many possible solutions
    - with no time to try them all
    - so this method cannot be used

## 🧠 A “Less-Dumb” Idea (GA)

```
Generate a set of random solutions
Repeat
    Test each solution in the set (rank them)
    Remove some bad solutions from set
    Duplicate some good solutions
    make small changes to some of them
Until the best solution is good enough
```

## 🧩 How Do You Encode a Solution?

- Obviously, this depends on the problem!
- GAs often encode solutions as fixed-length “bitstrings” (e.g., 101110, 111111, 000101)
- Each bit represents some aspect of the proposed solution to the problem
- For GAs to work, we need to be able to “test” any string and get a “score” indicating how “good” that solution is

## 🛢️ Silly Example - Drilling for Oil

Imagine you had to drill for oil somewhere along a single 1km desert road. The problem is to choose the best place on the road that produces the most oil per day. We could represent each solution as a position on the road, e.g., a whole number between [0..1000].

### Where to drill for oil?

```
Road
Solution1 = 300
Solution2 = 900
```

## ⛏️ Digging for Oil

- The set of all possible solutions [0..1000] is called the **search space** or **state space**
- In this case, it’s just one number, but it could be many numbers or symbols
- Often GAs code numbers in binary producing a bitstring representing a solution
- In our example, we choose 10 bits which are enough to represent 0..1000

### Convert to binary string

|      | 512 | 256 | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 900  | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| 300  | 0   | 1   | 0   | 0   | 1   | 0   | 1   | 1   | 0   | 0   |
| 1023 | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |

In GAs, these encoded strings are sometimes called “**genotypes**” or “**chromosomes**,” and the individual bits are sometimes called “**genes**”.

![Visual representation of the process of drilling for oil, featuring a graph and two drilling rigs.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/2ba1beb3-fa43-458b-9616-5365f149c7c5.jpeg)

The image effectively illustrates the concept of drilling for oil, highlighting the relationship between location and oil presence. The use of a graph and drilling rigs provides a clear visual representation of the process.

## 📝 Summary (So Far)

We have seen how to:

- represent possible solutions as a number
- encode a number into a binary string
- generate a score for each number given a function of “how good” each solution is - this is often called a **fitness function**
- Our silly oil example is really optimization over a function f(x) where we adapt the parameter x

## 🗺️ Search Space

- For a simple function f(x), the search space is one-dimensional.
- By encoding several values into the chromosome many dimensions can be searched, e.g., two dimensions f(x,y)
- Search space can be visualized as a surface or fitness landscape in which fitness is height
- A GA tries to move the points to better places (higher fitness) in the space

### Fitness landscapes

## 🏞️ Search Space

- The nature of the search space dictates how a GA will perform
- A completely random space - bad for a GA
- Also, GA can get stuck in local maxima if search spaces contain lots of these
- Generally, spaces in which small improvements get closer to the global optimum are good

## ⚙️ Back to the (GA) Algorithm

```
Generate a set of random solutions
Repeat
    Test each solution in the set (rank them)
    Remove some bad solutions from set
    Duplicate some good solutions
    make small changes to some of them
Until best solution is good enough
```

## 👶 Adding Reproduction - Crossover

Although it may work for simple search spaces - our algorithm is still very simple, it relies on random mutation to find a good solution. Introducing reproduction gives better results.

### Adding Reproduction - Crossover

- Two high scoring “parent” bit strings (chromosomes) are selected and with some probability (crossover rate) combined
- Producing two new offspring (bit strings)
- Each offspring may then be changed randomly (mutation)

## 👪 Selecting Parents

- Many schemes are possible; the goal is that better scoring chromosomes are more likely to be selected
    
- Score is often termed the fitness
    
- “Roulette Wheel” selection can be used:
    
    - Add up the fitness's of all chromosomes
    - Generate a random number R in that range
    - Select the first chromosome in the population that - when all previous fitness’s are added - gives you at least the value R

### Example population

|No.|Chromosome|Fitness|Cumulative Sum|
|---|---|---|---|
|1|1010011010|1|1|
|2|1111100001|2|3|
|3|1011001100|3|6|
|4|1010000000|1|7|
|5|0000010000|3|10|
|6|1001011111|5|15|
|7|0101010101|1|16|
|8|1011100111|2|18|

![Genetic algorithm crossover process, illustrating single-point or two-point crossover.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/77c7278b-0a8f-4b27-9aa9-12d1ec5de3f4.jpeg)

The image depicts a genetic algorithm crossover process, specifically a single-point crossover or two-point crossover illustration.

## 🧬 Crossover - Recombination

![Illustration of a genetic algorithm crossover operation, showing the exchange of genetic material between two parent binary strings.](https://api-turbo.ai/c90e0eff-6ec2-4d46-90f6-17e74c4bf871/4bdde4fe-ee6c-4993-8abe-c73785f8795d.jpeg)

The image illustrates a genetic algorithm process, specifically the crossover operation.

### Mutation

With some small probability (the mutation rate), flip each bit in the offspring (typical values between 0.1 and 0.001)

## ⚙️ Back to the (GA) Algorithm

```
Generate a population of random chromosomes
Repeat (each generation)
    Calculate fitness of each chromosome
    Repeat
        Use roulette selection to select pairs of parents
        Generate offspring with crossover and mutation
    Until a new population has been produced
Until best solution is good enough
```

## 🧬 Many Variants of GA

- Different kinds of selection (not roulette)
    
    - Tournament
    - Elitism, etc.
- Different recombination
    
    - Multi-point crossover
    - 3-way crossover etc.
- Different kinds of encoding other than bitstring
    
    - Integer values
    - Ordered set of symbols
- Different kinds of mutation
    

## ⚙️ Many Parameters to Set

Any GA implementation needs to decide on a number of parameters: Population size (N), mutation rate (m), crossover rate (c). Often these have to be “tuned” based on results obtained - no general theory to deduce good values. Typical values might be: N = 50, m = 0.05, c = 0.9

## 🧬 Genetic Algorithms - Summarized

- Start with a randomly generated population of valid candidate solutions
    
- For generation in (0..n):
    
    - Select 2 solutions (parents) randomly from the population for reproduction based on the fitness of each state. The more fit a solution, the more likely selected to reproduce.
    - Reproduce a new solution (child) by combining random parts of the 2 selected solutions (crossover)
    - Mutate a random number of new solutions to allow exploration of other possible solutions
    - Population = new solutions
- The best solution is the fittest of population solutions
    

## 📝 Summary: Local Search

- Hill-climbing algorithms keep only a single solution in memory but can get stuck on local optima
- Simulated annealing escapes local optima and is optimal given a “long enough” cooling schedule
- Genetic algorithms can search a large space by modeling biological evolution