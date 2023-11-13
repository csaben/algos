"""
Citadel special nodes question Summer 2023.

Given a tree with N nodes, and a list of edges, find the special nodes.
Special node == endpoints of the longest path in the tree (diameter).

e.g.
[1,2,3,4,5,6,7]

6         5
 \       /
  1--2--3
 /       \
7         4

[0,0,0,1,1,1,1]

given: tree_nodes, tree_from, tree_to
return: special_nodes (integer arr)
"""

tree_nodes = 7
tree_from = [1, 2, 3, 3, 1, 1]
tree_to = [2, 3, 4, 5, 6, 7]

from collections import defaultdict


def is_special_node(nodes, tree_from, tree_to):
    """3*O(n) time, O(n) space"""
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for v, w in zip(tree_from, tree_to):
        graph[v].append(w)
        graph[w].append(v)

    # Depth-First Search function to find the farthest nodes from a given start node
    def dfs(node, level, previous, farthest_nodes):
        nonlocal max_level
        # Update the farthest nodes set if a new max level is found
        if level > max_level:
            max_level = level
            farthest_nodes.clear()
            farthest_nodes.add(node)
        elif level == max_level:
            farthest_nodes.add(node)
        # Explore adjacent nodes
        for neighbor in graph[node]:
            # if neighbor is previous, don't explore it
            if neighbor != previous:
                dfs(neighbor, level + 1, node, farthest_nodes)

    # First DFS to find one endpoint of the longest path
    max_level = -1
    farthest_nodes_from_start = set()
    dfs(1, 0, -1, farthest_nodes_from_start)

    # Second DFS from one of the farthest nodes found in the first DFS
    max_level = -1
    farthest_nodes_from_end = set()
    # bc trees are not cyclic, we start from other end to get endpoints
    # of the longest path from other direction
    dfs(next(iter(farthest_nodes_from_start)), 0, -1, farthest_nodes_from_end)

    # Combine the results of both DFS calls to get all endpoints of the longest path
    special_nodes = list(farthest_nodes_from_start | farthest_nodes_from_end)

    # in O(n) time, set the special nodes to 1 and rest to 0
    expected_return = [0] * nodes
    for i in range(1, tree_nodes + 1):
        if i in special_nodes:
            expected_return[i - 1] = 1
    return expected_return


print(is_special_node(tree_nodes, tree_from, tree_to))
