graph_list = dict()

graph_list["A"] = ["B", "C"]
graph_list["B"] = ["A", "D", "E"]
graph_list["C"] = ["A", "F", "G"]
graph_list["D"] = ["B"]
graph_list["E"] = ["B"]
graph_list["F"] = ["C"]
graph_list["G"] = ["C"]


root_node = "A"


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            stack.extend(reversed(graph[node]))
    return visited


print(DFS(graph_list, root_node))
