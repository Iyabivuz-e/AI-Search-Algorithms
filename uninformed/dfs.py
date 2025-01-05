# DFS is like exploring a forest by following one path to the end before switching.
# In AI, DFS is useful for puzzle-solving, game AI, and exploring graphs deeply.
# It’s easy to implement and great for recursive problem-solving.

def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop() #removes the last element
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # for neighbor in reversed(graph[node]): For the rightmost-first traversal
            for neighbor in graph[node]: # For the leftmost-first traversal
                if neighbor not in visited:
                    stack.append(neighbor)
graph = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5],
    5: [2, 4],
    6: [3]
}
dfs(graph, 1)