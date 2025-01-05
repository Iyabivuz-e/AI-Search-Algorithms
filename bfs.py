# It’s called Breadth-First because it widens the search 
# by looking at all possible options at each level before going deeper.

# 🛠️ ***How Does BFS Work in AI?***
# In Artificial Intelligence (AI), BFS helps:

# - Solve puzzles (like Rubik’s cubes or mazes).
# - Find the best path (like GPS).
# - Explore possibilities (like in chess).
# - BFS guarantees finding the shortest solution if one exists.
# - Pathfinding algorithms (like maps or games).
# - Puzzle-solving (like Sudoku or crosswords).
# - Web crawling (like how search engines scan websites).


# 🔑 Key BFS Concepts:
# Queue: BFS uses a "queue" (like waiting in line). First in, first out!
# Level by Level: BFS checks all paths equally.

def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': []
}

bfs(graph, 'A')