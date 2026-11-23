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

def bfs(init_state, goal_state):
    bfs_queue = deque([(init_state, 0)])
    visited = set()
    
    visited.add(init_state)
    
    while bfs_queue:
        current_state, current_cost = bfs_queue.popleft()
        
        if current_state == goal_state:
            return current_cost
        
        for move in valid_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                visited.add(new_state)
                bfs_queue.append((new_state, current_cost + 1))

if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    print(bfs(init_state, goal_state))    
    