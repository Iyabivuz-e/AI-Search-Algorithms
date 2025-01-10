import heapq

def a_star_algorithm(graph, start_node, goal_node, heuristic):
    open_list = []  # A priority queue to store (f(n)-score , node, path)
    # Example: open_list = [4, 'J', ['A', 'Y', 'J']]
    heapq.heappush(open_list, (0, start_node, [start_node]))
    visited = set()  # A dictionary that is going to store visited nodes
    g_score = {start_node: 0}  # A cost from a start to a node

    while open_list:
        current_f_score, current_node, current_path = heapq.heappop(open_list)

        if current_node == goal_node:
            return current_path, g_score[current_node]
        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor in visited:
                continue
            tentative_g_score = g_score[current_node] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor,
                               current_path + [neighbor]))

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0,  # Goal node, heuristic is 0
}

path = a_star_algorithm(graph, 'A', 'D', heuristic)
print(f"The path is: {path}")

