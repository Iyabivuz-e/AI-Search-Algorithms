
#  What is Greedy Best-First Search?
    # Greedy Best-First Search (GBFS) is a pathfinding algorithm.
    # It always chooses the path that looks closest to the goal (like a magnet pulling you towards the goal).
    # It doesn’t care how long the path is, only how close it thinks it is to the goal.
    
import heapq # To make sure that our frontier is always sorted and gives us the least value.

def greedy_search(graph, start, goal, heuristic):
    frontier = [(heuristic[start], start, [])] # A list of the curent path we are exploring
    visited = set() # An object to keep tracking of visited nodes so that we dont repeat the node twice
    
    while frontier:
        _, node, path = heapq.heappop(frontier)
        path = path + [node]
        
        if node == goal:
            return path
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, path))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Estimated distance to the goal (heuristic)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0  # Goal node, heuristic is 0
}

path = greedy_search(graph, 'A', 'G', heuristic)
print(f"The path to take is: ", path)