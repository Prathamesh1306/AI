from collections import deque

def bfs(max1,max2,target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        j1, j2 = q.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        print(f"(Jug1: {j1}, Jug2: {j2})")

        if j1 == target or j2 == target:
            print("Target reached!")
            break

        q.extend([
            (0, j2),  # empty jug1
            (j1, 0),  # empty jug2
            (max1, j2),  # fill jug1
            (j1, max2),  # fill jug2
            (min(j1 + j2, max1), j2 - (min(j1 + j2, max1) - j1)),  # pour jug2 -> jug1
            (j1 - (min(j1 + j2, max2) - j2), min(j1 + j2, max2))   # pour jug1 -> jug2
        ])

if __name__ == "__main__":
      target=int(input("Enter the storgage: "))
      max1 = int(input("Enter size of Jug 1: "))
      max2 = int(input("Enter size of Jug 2: "))

      if target > max1 and target > max2:
        print("Target cannot be greater than both jug sizes.")
        exit(1)

      bfs(max1,max2,target)