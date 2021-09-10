# deque 버전
from collections import deque

graph_list = dict()

graph_list["A"] = ["B", "C"]
graph_list["B"] = ["A", "D", "E"]
graph_list["C"] = ["A", "F", "G"]
graph_list["D"] = ["B"]
graph_list["E"] = ["B"]
graph_list["F"] = ["C"]
graph_list["G"] = ["C"]


root_node = "A"


def BFS_1(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])

    return visited


print(BFS_1(graph_list, root_node))

# deque 없는 버전(위 버전보다 느리다)
# list.pop(0)의 시간복잡도는 O(N) 참조: https://wiki.python.org/moin/TimeComplexity


def BFS_2(graph, root):
    visited = []
    need_visit = []

    need_visit.append(root)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


print(BFS_2(graph_list, root_node))
