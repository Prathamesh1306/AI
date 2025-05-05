from queue import PriorityQueue

def heuristic(state, goal):
    return sum([1 for i in range(9) if state[i] != goal[i] and state[i] != 0])

def get_neighbors(state):
    zero = state.index(0)
    neighbors = []

    def swap(s, i, j):
        s = s[:]
        s[i], s[j] = s[j], s[i]
        return s

    directions = {
        -1: "LEFT",
        1: "RIGHT",
        -3: "UP",
        3: "DOWN"
    }
    for move, direction in directions.items():
        new_index = zero + move
        if 0 <= new_index < 9:            
            if move == -1 and zero % 3 == 0: continue
            if move == 1 and zero % 3 == 2: continue
            neighbors.append((swap(state, zero, new_index), direction))

    return neighbors

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

def hill_climbing(start, goal):
    current = start
    steps = 0
    while True:
        h = heuristic(current, goal)
        print(f"\nMove {steps}:")
        print_state(current)
        print(f"Heuristic = {h}")
        neighbors = get_neighbors(current)
        best_neighbor, direction = min(neighbors, key=lambda x: heuristic(x[0], goal))
        if heuristic(best_neighbor, goal) >= h:
            break
        print(f"Move: {direction}")
        current = best_neighbor
        steps += 1
    print(" Goal Reached!" if current == goal else "\nStuck in local minimum.")
hill_climbing([1,2,3,4,0,5,6,7,8], [1,2,3,4,5,6,7,8,0])