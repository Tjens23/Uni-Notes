class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, path_cost=0, heuristic=0, total_cost=0):
        self.total_cost = total_cost  # Fixed typo: totoal_cost -> total_cost
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.path_cost = path_cost
        self.heuristic = heuristic

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def priority(self, search_type='greedy', w=1):
        if search_type == 'greedy':
            return self.heuristic
        elif search_type == 'a_star':
            return self.path_cost + w * self.heuristic
        return None

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - g: ' + str(
            self.path_cost) + ' - h: ' + str(self.heuristic) + ' - f: ' + str(self.total_cost)


# Graph structure with edge costs
GRAPH = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('F', 5), ('G', 4)],
    'C': [('A', 2), ('D', 4), ('E', 1)],
    'D': [('C', 4), ('I', 2)],
    'E': [('C', 1), ('F', 3), ('H', 1)],
    'F': [('B', 5), ('E', 3), ('G', 1)],
    'G': [('B', 4), ('F', 1), ('H', 2), ('K', 6)],
    'H': [('E', 1), ('G', 2), ('I', 3), ('L', 8)],
    'I': [('D', 2), ('H', 3), ('J', 3)],
    'J': [('I', 3), ('L', 3)],
    'K': [],  # Goal node
    'L': []  # Goal node
}


def heuristic(current_state, goal_state):
    heuristic_values = {
        'A': 6, 'B': 5, 'C': 5, 'D': 2,
        'E': 4, 'F': 5, 'G': 4, 'H': 1,
        'I': 2, 'J': 1, 'K': 0, 'L': 0
    }
    return heuristic_values.get(current_state, 0)


def insert_priority(node, queue, search_type='greedy'):
    if search_type == 'greedy':
        node.heuristic = heuristic(node.STATE, GOAL_STATE)
    elif search_type == 'a_star':
        node.heuristic = heuristic(node.STATE, GOAL_STATE)
        node.total_cost = node.path_cost + node.heuristic
    else:
        raise ValueError("Unknown search type: {}".format(search_type))

    queue.append(node)  # append node to the end of the queue
    queue.sort(key=lambda x: x.priority(search_type))  # sort by priority
    return queue


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def TREE_SEARCH(algorithm_type='a_star'):  # Fixed: Added algorithm parameter
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = insert_priority(initial_node, fringe, algorithm_type)  # Fixed: Use insert_priority

    while fringe:  # Fixed: Check if fringe has elements
        node = REMOVE_FIRST(fringe, algorithm_type)  # Fixed: Pass algorithm type
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node, GOAL_STATE)  # Fixed: Pass goal state
        fringe = INSERT_ALL(children, fringe, algorithm_type)  # Fixed: Pass algorithm type
        print("fringe: {}".format([str(n) for n in fringe]))
    return None


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def EXPAND(node, goal_state):
    successors = []
    children_states = successor_fn(node.STATE)  # Fixed: Renamed to avoid conflict

    for child_state in children_states:  # Fixed: Use different variable name
        # Get edge cost from graph
        edge_cost = 1  # Default cost
        if node.STATE in GRAPH:
            for neighbor, cost in GRAPH[node.STATE]:
                if neighbor == child_state:
                    edge_cost = cost
                    break

        new_cost = node.path_cost + edge_cost
        h_value = heuristic(child_state, goal_state)

        s = Node(child_state)  # Fixed: Pass state to constructor
        s.STATE = child_state  # Fixed: Use capital STATE
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.path_cost = new_cost
        s.heuristic = h_value
        s.total_cost = new_cost + h_value  # Fixed: Use total_cost

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


def INSERT_ALL(node_list, queue, algorithm_type='a_star'):  # Fixed: Add algorithm parameter
    for node in node_list:
        queue = insert_priority(node, queue, algorithm_type)  # Fixed: Use insert_priority
    return queue


'''
Removes and returns the first element from fringe
'''


def REMOVE_FIRST(queue, alg='a_star'):
    if not queue:  # Check if queue is empty
        return None

    if alg == 'a_star':
        min_node = min(queue, key=lambda x: x.total_cost)  # Fixed: Use total_cost
        queue.remove(min_node)  # remove the node with minimum total cost
        return min_node  # return the node with minimum total cost
    elif alg == 'greedy':
        min_node = min(queue, key=lambda x: x.heuristic)
        queue.remove(min_node)  # Fixed: Remove node first, then return it
        return min_node  # Fixed: Return the node, not None
    else:
        if len(queue) == 0:  # if queue is empty
            return None  # return None
        else:
            node = queue[0]  # get first element
            del queue[0]  # remove first element from queue
            return node  # return the removed node


'''
Successor function for the graph problem (A to L)
'''


def successor_fn(state):
    # Return neighbors from the graph
    if state in GRAPH:
        return [neighbor for neighbor, cost in GRAPH[state]]
    return []


INITIAL_STATE = 'A'  # Fixed: Use graph node instead of farmer problem
GOAL_STATE = 'K'  # Fixed: Goal is node K (or L)

'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    print("=== A* Search ===")
    path_astar = TREE_SEARCH('a_star')
    if path_astar:
        print('Goal state found with A*!')
        print('Solution path:')
        for node in reversed(path_astar):
            node.display()
        print(f"Path length: {len(path_astar)}")
        print(f"Total cost: {path_astar[0].path_cost}")
    else:
        print('Goal state not found with A*!')

    print("\n=== Greedy Best-First Search ===")
    path_greedy = TREE_SEARCH('greedy')
    if path_greedy:
        print('Goal state found with Greedy!')
        print('Solution path:')
        for node in reversed(path_greedy):
            node.display()
        print(f"Path length: {len(path_greedy)}")
        print(f"Total cost: {path_greedy[0].path_cost}")
    else:
        print('Goal state not found with Greedy!')


if __name__ == '__main__':
    run()