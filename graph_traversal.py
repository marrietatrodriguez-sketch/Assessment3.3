"""
Assessment 3.3 - Graph (RODRIGUEZ)

Vertices: R1, O, D, R2, I, G, U, E, Z
(R1 and R2 are both "R" in the assessment; they are labeled separately here
so the two vertices stay distinct.)

Edges (from the diagram):
  R1-O, R1-D, O-R2, O-I, I-G, D-G, D-U, G-U, G-E, R2-E, U-Z

Traversals start at R1. Neighbors are visited in the order listed in the
adjacency lists below, which reproduces the expected output.

  BFS -> R1 O D R2 I G U E Z   (shown as R O D R I G U E Z)
  DFS -> R1 O R2 E G D U Z I   (shown as R O R E G D U Z I)
"""

from collections import deque


def build_rodriguez_graph():
    """Adjacency list for the graph shown in the diagram."""
    return {
        "R1": ["O", "D"],
        "O":  ["R1", "R2", "I"],
        "D":  ["R1", "G", "U"],
        "R2": ["O", "E"],
        "I":  ["O", "G"],
        "G":  ["D", "U", "E", "I"],
        "U":  ["D", "G", "Z"],
        "E":  ["R2", "G"],
        "Z":  ["U"],
    }


def bfs(graph, start):
    """Breadth-First Search: explore all neighbors of a vertex before going deeper."""
    order = []
    visited = {start}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)      # mark when enqueued to avoid duplicates
                queue.append(neighbor)
    return order


def dfs(graph, start):
    """Depth-First Search: go as deep as possible along a path, then backtrack."""
    order = []
    visited = set()

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def display(label, order):
    """Print labels with R1/R2 shown as plain R, as in the assessment."""
    return " - ".join(v[0] if v in ("R1", "R2") else v for v in order)


def main():
    graph = build_rodriguez_graph()
    start = "R1"

    print("Graph - RODRIGUEZ")
    print("BFS (Breadth-First Search):", display("BFS", bfs(graph, start)))
    print("DFS (Depth-First Search):  ", display("DFS", dfs(graph, start)))


if __name__ == "__main__":
    main()
