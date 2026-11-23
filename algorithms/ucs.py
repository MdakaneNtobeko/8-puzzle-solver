from collections import deque

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
    cost = 1

    if move == "UP":
        cost = 5
        target = empty_pos - 3
    elif move == "DOWN":
        target = empty_pos + 3
    elif move == "LEFT":
        target = empty_pos - 1
    else:
        target = empty_pos + 1
        
    new_state[empty_pos], new_state[target] = new_state[target], new_state[empty_pos]
    
    return "".join(new_state), cost

def reconstruct_path(parent, action, state):
    path = []
    moves = []
    while state is not None:
        path.append(state)
        moves.append(action.get(state))
        state = parent[state]
    return path[::-1], moves[::-1]

# Uniform Cost Search (UCS) implementation
def ucs(init_state, goal_state):
    frontier = {0: deque([init_state])}
    best_cost = {init_state: 0}
    parent = {init_state: None}
    action = {}
    
    current_cost = 0
    frontier_count = 1
    
    while frontier_count > 0:
        while current_cost not in frontier or not frontier[current_cost]:
           current_cost += 1
        
        current_state = frontier[current_cost].popleft()
        frontier_count -= 1
        
        if current_cost != best_cost[current_state]:
            continue
        
        if current_state == goal_state:
            path, moves = reconstruct_path(parent, action, current_state)
            return {
                "path": path,
                "moves": moves[1:],
                "cost": current_cost
            }
        
        for move in valid_moves(current_state):
            new_state, move_cost = apply_move(current_state, move)
            new_cost = current_cost + move_cost
            
            if new_cost < best_cost.get(new_state, float("inf")):
                best_cost[new_state] = new_cost
                parent[new_state] = current_state
                action[new_state] = move
                
                if new_cost not in frontier:
                    frontier[new_cost] = deque()
                
                frontier[new_cost].append(new_state)
                frontier_count += 1
    
if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    print(ucs(init_state, goal_state))    
    