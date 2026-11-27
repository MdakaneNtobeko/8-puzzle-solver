import time
import heapq

from utils.puzzle import valid_moves, apply_move, move_cost
from utils.heuristics import build_goal_positions, manhattan_heu
from utils.path import reconstruct_path

def gbfs(init_state, goal_state, goal_positions):
    parent = {init_state: None}
    action = {}
    
    frontier = [(manhattan_heu(init_state, goal_positions), init_state, 0)]
    
    discovered = {init_state}
    
    nodes_expanded = 0
    nodes_generated = 0
    max_frontier_size = 1
    start_time = time.perf_counter()
        
    while frontier:
        _, current_state, current_cost = heapq.heappop(frontier)

        nodes_expanded += 1

        if current_state == goal_state:
            path, moves = reconstruct_path(
                parent, action, current_state
            )

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
            nodes_generated += 1

            if new_state not in discovered:
                discovered.add(new_state)

                parent[new_state] = current_state
                action[new_state] = move

                heapq.heappush(
                    frontier,
                    (
                        manhattan_heu(new_state, goal_positions),
                        new_state,
                        current_cost + move_cost(move)
                    )
                )

                max_frontier_size = max(
                    max_frontier_size,
                    len(frontier)
                )

if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    goal_positions = build_goal_positions(goal_state)
    
    print(gbfs(init_state,goal_state, goal_positions))    
    