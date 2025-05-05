graph = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2)],
    'C': [('D',3)],
    'D': []
}
h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

from queue import PriorityQueue

def a_star_city(start, goal):
    q = PriorityQueue(); q.put((h[start], 0, start))
    visited = set()
    while not q.empty():
        f, g, node = q.get()
        print(node)
        if node == goal: return
        visited.add(node)
        for nei, cost in graph[node]:
            if nei not in visited:
                q.put((g+cost+h[nei], g+cost, nei))

a_star_city('A', 'D')
