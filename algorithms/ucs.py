import time
import heapq

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

import heapq
import time

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
                "moves": moves[1:],
                "cost": current_cost,
                "nodes_expanded": nodes_expanded,
                "nodes_generated": nodes_generated,
                "max_frontier_size": max_frontier_size,
                "runtime_ms": runtime * 1000
            }

        for move in valid_moves(current_state):
            new_state, move_cost = apply_move(current_state, move)

            nodes_generated += 1
            new_cost = current_cost + move_cost

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
    