from queue import PriorityQueue

grid = [[0,1,0],[0,1,0],[0,0,0]]
start, goal = (0,0), (2,2)

def h(p): return abs(p[0]-goal[0]) + abs(p[1]-goal[1])

def astar_robot():
    q = PriorityQueue(); q.put((h(start), 0, start))
    visited = set()
    while not q.empty():
        f, g, cur = q.get()
        print(cur)
        if cur == goal: return
        visited.add(cur)
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            x,y = cur[0]+dx, cur[1]+dy
            if 0<=x<3 and 0<=y<3 and grid[x][y]==0 and (x,y) not in visited:
                q.put((g+1+h((x,y)), g+1, (x,y)))

astar_robot()
