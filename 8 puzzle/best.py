from heapq import heappush, heappop

def heuristic(s, g):
    return sum(1 for i in range(9) if s[i] != g[i] and s[i] != 0)

def get_neighbors(state):
    zero = state.index(0)
    moves = [(-1, "LEFT"), (1, "RIGHT"), (-3, "UP"), (3, "DOWN")]
    neighbors = []
    for move, name in moves:
        ni = zero + move
        if 0 <= ni < 9:
            if move == -1 and zero % 3 == 0: continue
            if move == 1 and zero % 3 == 2: continue
            new_state = state[:]
            new_state[zero], new_state[ni] = new_state[ni], new_state[zero]
            neighbors.append((new_state, name))
    return neighbors

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def best_first(start, goal):
    visited = set()
    pq = [(heuristic(start, goal), start, "Start")]
    steps = 0
    while pq:
        h, state, move = heappop(pq)
        print(f"\nMove {steps}: {move}")
        print_board(state)
        if state == goal:
            print(" Goal reached!")
            return
        visited.add(tuple(state))
        for neighbor, direction in get_neighbors(state):
            if tuple(neighbor) not in visited:
                heappush(pq, (heuristic(neighbor, goal), neighbor, direction))
        steps += 1
    print("No solution.")

# Example run
best_first([1,2,3,4,5,6,0,7,8], [1,2,3,4,5,6,7,8,0])
