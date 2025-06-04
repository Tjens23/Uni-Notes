def minmax_decision(state):
    infinity = float('inf')

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0, 1, 2, 3, 'X', 5, 6, 7, 8]
    :return: True if the game is over, False otherwise
    """
    # Check for a winner
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in winning_combinations:
        if state[a] == state[b] == state[c] and isinstance(state[a], str):
            return True  # We have a winner

    # Check if the board is full (tie)
    return all(isinstance(x, str) for x in state)

def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0, 1, 2, 3, 'X', 5, 6, 7, 8]
    :return: +1, -1, or 0
    """
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in winning_combinations:
        if state[a] == state[b] == state[c] and isinstance(state[a], str):
            if state[a] == 'X':
                return +1
            elif state[a] == 'O':
                return -1
    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0, 1, 2, 3, 'X', 5, 6, 7, 8]
    :return: List of (move, new_state) pairs
    """
    # Determine which player's turn it is
    # Count how many Xs and Os are on the board
    x_count = state.count('X')
    o_count = state.count('O')

    # If X has more moves than O, it's O's turn, otherwise X's turn
    next_player = 'O' if x_count > o_count else 'X'

    successors = []
    for i in range(len(state)):
        if isinstance(state[i], int):  # Check if the cell is empty
            new_state = state[:]
            new_state[i] = next_player
            successors.append((i, new_state))
    return successors


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
