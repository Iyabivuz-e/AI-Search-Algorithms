def uniform_cost_search(graph, start, target):
    frontier = [(0, start, [])] # To keep track of the cost, current_node, and the paths we have visited so far.
                                # frontier = [ (cost, current_node, [])] e.x: frontier = [(0, 'A', [])] if start is 'A'
    visited = set()
    
    while frontier:
        frontier.sort(key = lambda x: x[0]) # This will sort the frontier to get the lowest cost
        cost, node, path = frontier.pop(0) # We remove the path with the lowest cost
        
        if node == target:
            return path, cost # This means that we have found the target (reached the goal)
        if node not in visited:
            visited.add(node)
            
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    frontier.append((total_cost, neighbor, path + [node]))
    return "No path found"

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('target', 3)],
    'C': [('target', 2)],
    'target': []
}

path, cost = uniform_cost_search(graph, 'A', 'target')
print(f"Cheapest Path: {path}, Total Cost: {cost}")