def reconstruct_path(parent, action, state):
    path = []
    moves = []

    while state is not None:
        path.append(state)

        if parent[state] is not None:
            moves.append(action[state])

        state = parent[state]

    return path[::-1], moves[::-1]