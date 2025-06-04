---
creation date: 2025-05-13 13:06
modification date: Tuesday 13th May 2025 13:36:25
tags:
  - Assignments
year: 2025
semester: 4
links: "[[AI Lecture 2]]"
---

---
# [[AI Lecture 2 Assignments]]


solution:

```python
# Solution for 4-location vacuum world
# Extended from reflex_vacuum_agent.py

A = 'A'
B = 'B'
C = 'C'
D = 'D'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}

def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Right'
    if loc_st[0] == C:
        return 'Right'
    if loc_st[0] == D:
        return 'Left'

def Sensors():  # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])

def Actuators(action):  # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right':
        if location == A:
            Environment['Current'] = B
        elif location == B:
            Environment['Current'] = C
        elif location == C:
            Environment['Current'] = D
    elif action == 'Left':
        if location == B:
            Environment['Current'] = A
        elif location == C:
            Environment['Current'] = B
        elif location == D:
            Environment['Current'] = C

def run(n):  # run the agent through n steps
    print('    Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))

# Solution for Reflex Agent with State - 4 locations
# Extended from reflex_agent_with_state.py

class ReflexAgentWithState:
    def __init__(self):
        self.state = {}
        self.action = None
        self.model = {A: None, B: None, C: None, D: None}  # Initially ignorant
        
        self.RULE_ACTION = {
            1: 'Suck',
            2: 'Right',
            3: 'Left',
            4: 'NoOp'
        }
        
        self.rules = {
            (A, 'Dirty'): 1,
            (B, 'Dirty'): 1,
            (C, 'Dirty'): 1,
            (D, 'Dirty'): 1,
            (A, 'Clean'): 2,
            (B, 'Clean'): 2,
            (C, 'Clean'): 2,
            (D, 'Clean'): 3,
            (A, B, C, D, 'Clean'): 4
        }

    def UPDATE_STATE(self, state, action, percept):
        (location, status) = percept
        state = percept
        if all(self.model[loc] == 'Clean' for loc in [A, B, C, D]):
            state = (A, B, C, D, 'Clean')
        self.model[location] = status  # Update the model state
        return state

    def RULE_MATCH(self, state, rules):
        rule = rules.get(tuple(state))
        return rule

    def REFLEX_AGENT_WITH_STATE(self, percept):
        self.state = self.UPDATE_STATE(self.state, self.action, percept)
        rule = self.RULE_MATCH(self.state, self.rules)
        self.action = self.RULE_ACTION[rule]
        return self.action

```
