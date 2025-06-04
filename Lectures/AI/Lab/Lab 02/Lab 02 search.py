class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))
    return None


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)  # append node to the end of the queue
    return queue  # return the updated queue


'''
Insert list of nodes into the fringe
'''

def INSERT_ALL(list, queue):
    for node in list:
        queue = INSERT(node, queue)
    return queue



'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    if len(queue) == 0:  # if queue is empty
        return None  # return None
    else:
        node = queue[0]  # get first element
        del queue[0]  # remove first element from queue
        return node  # return the removed node


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):
    # state is a tuple (farmer, wolf, goat, cabbage)
    # 'W' = west side, 'E' = east side
    farmer, wolf, goat, cabbage = state

    # Possible new states (including potentially invalid ones)
    possible_states = []

    # Farmer moves alone
    new_state = ('E' if farmer == 'W' else 'W', wolf, goat, cabbage)
    possible_states.append(new_state)

    # Farmer moves with wolf
    if farmer == wolf:  # They're on the same side
        new_state = ('E' if farmer == 'W' else 'W',
                     'E' if wolf == 'W' else 'W',
                     goat, cabbage)
        possible_states.append(new_state)

    # Farmer moves with goat
    if farmer == goat:  # They're on the same side
        new_state = ('E' if farmer == 'W' else 'W',
                     wolf,
                     'E' if goat == 'W' else 'W',
                     cabbage)
        possible_states.append(new_state)

    # Farmer moves with cabbage
    if farmer == cabbage:  # They're on the same side
        new_state = ('E' if farmer == 'W' else 'W',
                     wolf, goat,
                     'E' if cabbage == 'W' else 'W')
        possible_states.append(new_state)

    # Filter out invalid states - where wolf eats goat or goat eats cabbage
    valid_states = []
    for state in possible_states:
        f, w, g, c = state
        # If goat and wolf are on same side without farmer, wolf eats goat
        if g == w and g != f:
            continue
        # If goat and cabbage are on same side without farmer, goat eats cabbage
        if g == c and g != f:
            continue
        valid_states.append(state)

    return valid_states


INITIAL_STATE = ('W', 'W', 'W', 'W')  # (farmer, wolf, goat, cabbage)

# Goal state: all on east bank
GOAL_STATE = ('E', 'E', 'E', 'E')  # (farmer, wolf, goat, cabbage)

#STATE_SPACE = {'A': ['B', 'C'],
 #              'B': ['D', 'E'], 'C': ['F', 'G'],
  #             'D': [], 'E': [], 'F': [], 'G': ['H', 'I', 'J'],
   #            'H': [], 'I': [], 'J': [], }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    if path:
        print('Goal state found!')
        for node in reversed(path):
            node.display()
    else:
        print('Goal state not found!')


if __name__ == '__main__':
    run()