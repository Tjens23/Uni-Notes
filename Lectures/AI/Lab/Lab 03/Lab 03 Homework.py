class Node:
    def __init__(self, state, parent=None, depth=0, path_cost=0, heuristic=0, total_cost=0):
        self.total_cost = total_cost
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.path_cost = path_cost
        self.heuristic = heuristic

    def path(self):
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:
            current_node = current_node.PARENT_NODE
            path.append(current_node)
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


# Vacuum Cleaner Environment
# State representation: (position, dirt_status)
# position: 'A' or 'B'
# dirt_status: tuple of (dirt_in_A, dirt_in_B) where True means dirty

def vacuum_successor_fn(state):
    """Generate successor states for vacuum cleaner problem"""
    position, (dirt_A, dirt_B) = state
    successors = []

    if position == 'A':
        # From A, can move to B
        successors.append(('B', (dirt_A, dirt_B)))
        # From A, can clean A if it's dirty
        if dirt_A:
            successors.append(('A', (False, dirt_B)))
    else:  # position == 'B'
        # From B, can move to A
        successors.append(('A', (dirt_A, dirt_B)))
        # From B, can clean B if it's dirty
        if dirt_B:
            successors.append(('B', (dirt_A, False)))

    return successors


def vacuum_heuristic(state, goal_state):
    """Heuristic function for vacuum cleaner problem"""
    position, (dirt_A, dirt_B) = state

    # Count remaining dirt
    dirt_count = sum([dirt_A, dirt_B])

    # If there's dirt, we need at least that many actions to clean
    # Plus potential movement costs
    if dirt_count == 0:
        return 0
    elif dirt_count == 1:
        # If only one room is dirty and we're not there, need move + clean
        if (dirt_A and position == 'B') or (dirt_B and position == 'A'):
            return 2
        else:
            return 1
    else:  # dirt_count == 2
        # Need to clean both rooms, minimum 3 actions (clean, move, clean)
        return 3


def is_goal_state(state, goal_state):
    """Check if current state is a goal state"""
    position, (dirt_A, dirt_B) = state
    return not dirt_A and not dirt_B


class SearchProblem:
    """Generic search problem class"""

    def __init__(self, initial_state, goal_state, successor_fn, heuristic_fn, is_goal_fn):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.successor_fn = successor_fn
        self.heuristic_fn = heuristic_fn
        self.is_goal_fn = is_goal_fn
        self.explored_nodes = 0

    def reset_counters(self):
        self.explored_nodes = 0


def insert_priority(node, queue, search_type, problem):
    """Insert node into priority queue"""
    if search_type == 'greedy':
        node.heuristic = problem.heuristic_fn(node.STATE, problem.goal_state)
    elif search_type == 'a_star':
        node.heuristic = problem.heuristic_fn(node.STATE, problem.goal_state)
        node.total_cost = node.path_cost + node.heuristic
    else:
        raise ValueError("Unknown search type: {}".format(search_type))

    queue.append(node)
    queue.sort(key=lambda x: x.priority(search_type))
    return queue


def TREE_SEARCH(problem, algorithm_type='a_star'):
    """Generalized tree search algorithm"""
    problem.reset_counters()
    fringe = []
    initial_node = Node(problem.initial_state)
    fringe = insert_priority(initial_node, fringe, algorithm_type, problem)

    while fringe:
        node = REMOVE_FIRST(fringe, algorithm_type)
        problem.explored_nodes += 1

        if problem.is_goal_fn(node.STATE, problem.goal_state):
            return node.path(), problem.explored_nodes

        children = EXPAND(node, problem)
        fringe = INSERT_ALL(children, fringe, algorithm_type, problem)

    return None, problem.explored_nodes


def EXPAND(node, problem):
    """Expand node and get successors"""
    successors = []
    children_states = problem.successor_fn(node.STATE)

    for child_state in children_states:
        # Cost is 1 for each action (move or clean)
        edge_cost = 1
        new_cost = node.path_cost + edge_cost
        h_value = problem.heuristic_fn(child_state, problem.goal_state)

        s = Node(child_state)
        s.STATE = child_state
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.path_cost = new_cost
        s.heuristic = h_value
        s.total_cost = new_cost + h_value

        successors = INSERT(s, successors)
    return successors


def INSERT(node, queue):
    """Insert node into queue"""
    queue.append(node)
    return queue


def INSERT_ALL(node_list, queue, algorithm_type, problem):
    """Insert list of nodes into fringe"""
    for node in node_list:
        queue = insert_priority(node, queue, algorithm_type, problem)
    return queue


def REMOVE_FIRST(queue, alg='a_star'):
    """Remove and return first element from fringe based on algorithm"""
    if not queue:
        return None

    if alg == 'a_star':
        min_node = min(queue, key=lambda x: x.total_cost)
        queue.remove(min_node)
        return min_node
    elif alg == 'greedy':
        min_node = min(queue, key=lambda x: x.heuristic)
        queue.remove(min_node)
        return min_node
    else:
        node = queue[0]
        del queue[0]
        return node


def print_solution(path, cost, explored_nodes, algorithm_name):
    """Print solution details"""
    print(f"=== {algorithm_name} ===")
    if path:
        print(f'Goal state found!')
        print('Solution path:')
        for i, node in enumerate(reversed(path)):
            action = get_action_description(node, i)
            print(f"Step {i}: {node.STATE} {action}")
        print(f"Path length: {len(path)} steps")
        print(f"Total cost: {cost}")
        print(f"Explored nodes: {explored_nodes}")
    else:
        print('Goal state not found!')
        print(f"Explored nodes: {explored_nodes}")
    print()


def get_action_description(node, step):
    """Get human-readable action description"""
    if step == 0:
        return "(Initial state)"

    parent_state = node.PARENT_NODE.STATE
    current_state = node.STATE

    # Check if we're dealing with vacuum cleaner problem (tuple state)
    if isinstance(parent_state, tuple) and len(parent_state) == 2:
        parent_pos, parent_dirt = parent_state
        current_pos, current_dirt = current_state

        if parent_pos != current_pos:
            return f"(Move from {parent_pos} to {current_pos})"
        elif parent_dirt != current_dirt:
            return f"(Clean room {current_pos})"
        else:
            return "(Unknown action)"
    else:
        # For graph problem, just show movement between nodes
        return f"(Move from {parent_state} to {current_state})"


def run_vacuum_cleaner():
    """Run vacuum cleaner problem"""
    # Initial state: vacuum at A, both rooms dirty
    initial_state = ('A', (True, True))
    goal_state = ('A', (False, False))  # Goal: both rooms clean

    # Create problem instance
    problem = SearchProblem(
        initial_state=initial_state,
        goal_state=goal_state,
        successor_fn=vacuum_successor_fn,
        heuristic_fn=vacuum_heuristic,
        is_goal_fn=is_goal_state
    )

    print("Vacuum Cleaner Problem")
    print("Initial state: Vacuum at A, both rooms dirty")
    print("Goal: Clean both rooms")
    print()

    # Run A* search
    path_astar, explored_astar = TREE_SEARCH(problem, 'a_star')
    cost_astar = path_astar[0].path_cost if path_astar else 0
    print_solution(path_astar, cost_astar, explored_astar, "A* Search")

    # Run Greedy search
    path_greedy, explored_greedy = TREE_SEARCH(problem, 'greedy')
    cost_greedy = path_greedy[0].path_cost if path_greedy else 0
    print_solution(path_greedy, cost_greedy, explored_greedy, "Greedy Best-First Search")


def run_graph_problem():
    """Run the original graph problem for comparison"""
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

    def graph_successor_fn(state):
        if state in GRAPH:
            return [neighbor for neighbor, cost in GRAPH[state]]
        return []

    def graph_heuristic(current_state, goal_state):
        heuristic_values = {
            'A': 6, 'B': 5, 'C': 5, 'D': 2,
            'E': 4, 'F': 5, 'G': 4, 'H': 1,
            'I': 2, 'J': 1, 'K': 0, 'L': 0
        }
        return heuristic_values.get(current_state, 0)

    def graph_is_goal(state, goal_state):
        return state == goal_state

    initial_state = 'A'
    goal_state = 'K'

    problem = SearchProblem(
        initial_state=initial_state,
        goal_state=goal_state,
        successor_fn=graph_successor_fn,
        heuristic_fn=graph_heuristic,
        is_goal_fn=graph_is_goal
    )

    print("Graph Search Problem (A to K)")
    print()

    # Run A* search
    path_astar, explored_astar = TREE_SEARCH(problem, 'a_star')
    cost_astar = path_astar[0].path_cost if path_astar else 0
    print_solution(path_astar, cost_astar, explored_astar, "A* Search")

    # Run Greedy search
    path_greedy, explored_greedy = TREE_SEARCH(problem, 'greedy')
    cost_greedy = path_greedy[0].path_cost if path_greedy else 0
    print_solution(path_greedy, cost_greedy, explored_greedy, "Greedy Best-First Search")


if __name__ == '__main__':
    run_vacuum_cleaner()
    print("=" * 50)
    run_graph_problem()