def is_valid(state, color, neighbors):
    for n in neighbors[state]:
        if colors[n] == color:
            return False
    return True

def backtrack(state, neighbors, available_colors):
    if state == len(neighbors):
        return True
    for color in available_colors:
        if is_valid(state, color, neighbors):
            colors[state] = color
            if backtrack(state + 1, neighbors, available_colors):
                return True
            colors[state] = None
    return False


n = int(input("Enter number of nodes: "))
neighbors = {}

print("Enter neighbors for each node (space-separated indices from 0 to", n-1, "):")
for i in range(n):
    neighbor_input = input(f"Neighbors of node {i}: ").strip()
    if neighbor_input:
        raw = list(map(int, neighbor_input.split()))
        neighbors[i] = [x for x in raw if 0 <= x < n and x != i]
    else:
        neighbors[i] = []

colors = [None] * n
available_colors = input("Enter available colors (comma-separated): ").replace(",", " ").split()


if backtrack(0, neighbors, available_colors):
    print("\n Color Assignment:")
    for i, color in enumerate(colors):
        print(f"Node {i} → {color}")
else:
    print("No solution found.")
