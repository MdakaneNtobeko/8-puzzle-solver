from collections import deque
import time

from utils.puzzle import valid_moves, apply_move, move_cost
from utils.path import reconstruct_path

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
                "moves": moves,
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
                bfs_queue.append((new_state, current_cost + move_cost(move)))

if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    print(bfs(init_state, goal_state))    
    