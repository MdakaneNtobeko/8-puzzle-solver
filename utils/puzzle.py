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
    offsets = {
        "UP": -3,
        "DOWN": 3,
        "LEFT": -1,
        "RIGHT": 1
    }

    target = empty_pos + offsets[move]
        
    new_state[empty_pos], new_state[target] = new_state[target], new_state[empty_pos]
    
    return "".join(new_state)

def move_cost(move, weighted=False):
    if weighted and move == "UP":
        return 5
    
    return 1