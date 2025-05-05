from queue import PriorityQueue

grid = [[0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0]]
start, goal = (0, 0), (2, 3)

def heuristic(p): return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

def best_first_robot():
    q = PriorityQueue(); q.put((0, start))
    visited = set()
    while not q.empty():
        _, current = q.get()
        print(current)
        if current == goal: break
        visited.add(current)
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy
            if 0<=nx<3 and 0<=ny<4 and grid[nx][ny]==0 and (nx,ny) not in visited:
                q.put((heuristic((nx,ny)), (nx,ny)))

best_first_robot()