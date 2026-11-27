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