import time
import heapq

from utils.puzzle import valid_moves, apply_move, move_cost
from utils.path import reconstruct_path

def ucs(init_state, goal_state):
    frontier = [(0, init_state)]
    best_cost = {init_state: 0}

    parent = {init_state: None}
    action = {}

    nodes_expanded = 0
    nodes_generated = 0
    max_frontier_size = 1

    start_time = time.perf_counter()

    while frontier:
        current_cost, current_state = heapq.heappop(frontier)

        # Ignore outdated frontier entries
        if current_cost != best_cost[current_state]:
            continue

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
            new_cost = current_cost + move_cost(move, True)

            if new_cost < best_cost.get(new_state, float("inf")):
                best_cost[new_state] = new_cost

                parent[new_state] = current_state
                action[new_state] = move

                heapq.heappush(
                    frontier,
                    (new_cost, new_state)
                )

                max_frontier_size = max(
                    max_frontier_size,
                    len(frontier)
                )

    return None
    
if __name__ == "__main__":
    init_state = input().strip()
    goal_state = input().strip()
    
    print(ucs(init_state, goal_state))    
    