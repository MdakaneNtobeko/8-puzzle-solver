def valid_moves(state):
    empty_pos = state.index("#")
    
    moves = []
    
    if empty_pos >= 3:
        moves.append("UP")
    if empty_pos < 6:
        moves.append("DOWN")
    if empty_pos % 3 != 0:
        moves.append("LEFT")
    if empty_pos % 3 != 2:
        moves.append("RIGHT")
    
    return moves


def apply_move(state, move):
    new_state = list(state)
    empty_pos = state.index("#")
    target = 0

    if move == "UP":
        target = empty_pos - 3
    elif move == "DOWN":
        target = empty_pos + 3
    elif move == "LEFT":
        target = empty_pos - 1
    else:
        target = empty_pos + 1
        
    new_state[empty_pos], new_state[target] = new_state[target], new_state[empty_pos]
    
    return "".join(new_state)

def build_goal_positions(goal_state):
    pos = {}
    for idx, tile in enumerate(goal_state):
        if tile != '#':
            pos[tile] = (idx // 3, idx % 3)
    return pos

def manhattan_heu(state, goal_positions):
    h = 0
    for idx, tile in enumerate(state):
        if tile == '#': continue
        r1,c1 = idx // 3, idx % 3
        r2,c2 = goal_positions[tile]
        h += abs(r1-r2) + abs(c1-c2)
    return h

def reconstruct_path(parent, action, state):
    path = []
    moves = []
    while state is not None:
        path.append(state)
        moves.append(action.get(state))
        state = parent[state]
    return path[::-1], moves[::-1]


def a_star(init_state, goal_positions):
    parent = {init_state: None}
    action = {}
    frontier = [(manhattan_heu(init_state, goal_positions), init_state, 0)]
    visited = set()
        
    while frontier:
        frontier.sort(key=lambda item : (item[0], item[1]))
        _, current_state, current_cost = frontier.pop(0)
        
        if current_state in visited:
            continue
        visited.add(current_state)
        
        if current_state == goal_state:
            path, moves = reconstruct_path(parent, action, current_state)
            return {
                "path": path,
                "moves": moves[1:],
                "cost": current_cost
            }
        
        for move in valid_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                parent[new_state] = current_state
                action[new_state] = move
                frontier.append((manhattan_heu(new_state, goal_positions) + current_cost, new_state, current_cost + 1))

if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    goal_positions = build_goal_positions(goal_state)
    
    print(a_star(init_state, goal_positions))
    