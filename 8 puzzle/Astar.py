from heapq import heappop, heappush

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def h(state):
    return sum(x != y and x != 0 for x, y in zip(state, goal))

def neighbors(state):
    i = state.index(0)
    moves = []
    for d in [-1, 1, -3, 3]:
        ni = i + d
        if 0 <= ni < 9 and (i % 3 != 0 or d != -1) and (i % 3 != 2 or d != 1):
            new_state = state[:]
            new_state[i], new_state[ni] = new_state[ni], new_state[i]
            moves.append(new_state)
    return moves

def print_state(state, g):
    print(f"Step {g}:")
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else ' ' for x in state[i:i+3]))
    print("-" * 10)

def astar(start):
    queue = []
    heappush(queue, (h(start), 0, start))
    visited = set()
    
    while queue:
        f, g, state = heappop(queue)
        print_state(state, g)
        if state == goal:
            print(f"Goal reached in {g} steps.")
            return
        visited.add(tuple(state))
        
        for neighbor in neighbors(state):
            if tuple(neighbor) not in visited:
                heappush(queue, (g + 1 + h(neighbor), g + 1, neighbor))


astar([1, 2, 3, 4, 0, 6, 7, 5, 8])
