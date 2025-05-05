graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('E', 10)],
    'D': [('E', 3), ('F', 8)],
    'E': [('F', 2)],\
    'F': []
}
heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'F': 0}

from queue import PriorityQueue

def best_first_city(start, goal):
    q = PriorityQueue(); q.put((heuristic[start], start))
    visited = set()
    while not q.empty():
        _, city = q.get()
        print(city)
        if city == goal: return
        visited.add(city)
        for neighbor, _ in graph[city]:
            if neighbor not in visited:
                q.put((heuristic[neighbor], neighbor))

best_first_city('A', 'B')
