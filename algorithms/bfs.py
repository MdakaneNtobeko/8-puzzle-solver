from collections import deque
import time

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

def reconstruct_path(parent, action, state):
    path = []
    moves = []

    while state is not None:
        path.append(state)

        if parent[state] is not None:
            moves.append(action[state])

        state = parent[state]

    return path[::-1], moves[::-1]

def bfs(init_state, goal_state):
    bfs_queue = deque([(init_state, 0)])
    visited = set()
    parent = {init_state: None}
    action = {}
    nodes_expanded = 0
    nodes_generated = 0
    max_frontier_size = 0
    
    visited.add(init_state)
    start_time = time.perf_counter()
    
    while bfs_queue:
        current_state, current_cost = bfs_queue.popleft()
        nodes_expanded += 1

        if current_state == goal_state:
            path, moves = reconstruct_path(parent, action, current_state)
            runtime = time.perf_counter() - start_time
            return {
                "path": path,
                "moves": moves[1:],
                "cost": current_cost,
                "nodes_expanded": nodes_expanded,
                "nodes_generated": nodes_generated,
                "max_frontier_size": max_frontier_size,
                "runtime_ms": runtime * 1000
            }
        
        for move in valid_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                visited.add(new_state)
                nodes_generated += 1
                max_frontier_size = max(max_frontier_size, len(bfs_queue) + 1)
                parent[new_state] = current_state
                action[new_state] = move
                bfs_queue.append((new_state, current_cost + 1))

if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    print(bfs(init_state, goal_state))    
    