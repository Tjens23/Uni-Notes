---
tags:
  - Notes
links: "[[AI Lecture 2]]"
creation date: 2025-02-11 16:25
modification date: Tuesday 11th February 2025 16:25:43
semester: 4
year: 2025
---


---
# [[AI Lecture 2 Notes]]

---

# Intelligent Agents Overview


- An agent is defined as any entity that perceives its environment through sensors and acts upon it through actuators.
- Examples of agents include human agents (using senses like eyes and ears as sensors and body parts for actions), robotic agents (using cameras and motors), and software agents (using data inputs like keystrokes).
- The terms associated with agents include "percept" as the sensory input, "percept sequence" as the complete history of inputs, and "agent function" which maps percept sequences to actions.
- An agent is characterized as a combination of its architecture and its program.

## Rational Agents  

- Rational agents are designed to select actions that maximize their performance based on percept sequences and inherent knowledge.
- The performance measure (utility function) is an objective criterion for evaluating the success of an agent's actions.
- The rationality of an agent depends on the design of performance measures relevant to intended outcomes or behavioral expectations.
- An example of a rational agent is a vacuum cleaner, which can have performance measures such as the amount of dirt cleaned up or the time taken to clean.


## Autonomy in Agents  

- Autonomous agents determine their behavior through experience and possess the capability to learn and adapt.
- Contrastingly, non-autonomous agents are primarily guided by their designers.
- The design of an autonomous agent enables it to make decisions independently, learn from prior experiences, and adapt its rules based on new information.

## Task Environment Specification (PEAS)  

- PEAS (Performance measure, Environment, Actuators, Sensors) defines the problem context for agents:
- A spam filter serves as another example, measuring performance by minimizing false positives and negatives within its email environment.

## Types of Environments

Environments in the context of intelligent agents can be categorized based on various attributes. Understanding these types is crucial for designing effective agents that can operate optimally within their environments. Below, we break down the key types of environments:

### 1. **Observable vs. Partially Observable**

- **Fully Observable**: The agent's sensors provide complete access to the state of the environment.
- **Partially Observable**: The agent lacks complete information about the environment, which may affect its decision-making.

### 2. **Deterministic vs. Stochastic**

- **Deterministic**: The next state of the environment is entirely determined by the current state and the agent's actions.
- **Stochastic**: The next state is not completely predictable and can be influenced by random factors.

### 3. **Episodic vs. Sequential**

- **Episodic**: The agent's experience is divided into independent episodes, where the outcome of one episode does not affect the next.
- **Sequential**: The agent's actions are interconnected, and the outcome of one action can influence future actions.

### 4. **Static vs. Dynamic**

- **Static**: The environment remains unchanged while the agent is deliberating.
- **Dynamic**: The environment can change while the agent is making decisions, requiring real-time adaptation.

### 5. **Discrete vs. Continuous**

- **Discrete**: The environment has a finite number of distinct states and actions.
- **Continuous**: The environment can have an infinite number of states and actions, often involving continuous variables.

### 6. **Single-Agent vs. Multi-Agent**

- **Single-Agent**: The environment contains only one agent operating independently.
- **Multi-Agent**: Multiple agents interact within the environment, which can lead to competition or cooperation.

## Hierarchy of Agent Types

Agents can be classified into various types based on their complexity and functionality. Understanding this hierarchy helps in designing intelligent systems that can effectively interact with their environments. Below is a structured overview of the different types of agents.

### 1. Table-Driven Agents

- **Description**: These agents use a large lookup table that maps precept sequences to actions.
- **Challenges**:
    - **Size**: The table can become impractically large.
    - **Design**: Requires significant time and knowledge to create.

### 2. Simple Reflex Agents

- **Description**: Operate based on condition-action rules (if-then statements).
- **Example**: plain text If the environment is dirty, then suck.
- **Limitations**:
    - They do not retain memory of past states, making them ineffective in partially observable environments.

### 3. Model-Based Reflex Agents

- **Description**: These agents maintain an internal state to keep track of past states of the world.
- **Functionality**:
    - Use a model to update their understanding of the environment.
    - Can handle partially observable environments.
- **Example**: plain text function REFLEX-AGENT-WITH-STATE(precept) returns an action state ← UPDATE-STATE(state, action, precept, model) rule ← RULE-MATCH(state, rules) action ← RULE-ACTION[rule] return action

### 4. Goal-Based Agents

- **Description**: These agents have goals that guide their decision-making.
- **Functionality**:
    - They evaluate possible actions based on how well they achieve their goals.

### 5. Utility-Based Agents

- **Description**: These agents make decisions based on a utility function, which quantifies the desirability of different states.
- **Functionality**:
    - They choose actions that maximise their expected utility, allowing for more nuanced decision-making compared to goal-based agents.

## Learning and Autonomous Agents  

- Learning agents utilise mechanisms to adapt and improve their decision-making process in unknown environments.
- Their ability to learn empowers them to determine effectiveness and explore potential actions continuously.
- A practical example includes an autonomous taxi adapting its driving rules after experiencing hazardous conditions and learning from such environmental feedback.
