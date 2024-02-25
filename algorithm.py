# greedy heuristic algorithm for the map coloring problem
import networkx as nx
import matplotlib.pyplot as plt

# check if the coloring is valid
def is_valid_coloring(graph, coloring):
    if not coloring:
        return False
    for u, v in graph.edges():      # for each edge (tuples) in the graph
        if coloring[u] == coloring[v]:      # if the colors of the nodes are the same
            return False    # return False  (not a valid coloring)       
    return True             # if all edges have different colored nodes return True (valid coloring)

# greedy heuristic algorithm for the map coloring problem
def greedy_coloring(graph, domain):
    coloring = {}       # create an empty dictionary
    # for each node in the graph
    for node in graph.nodes():
        # get the colors of the adjacent nodes
        adjacent_colors = {coloring.get(neighbour) for neighbour in graph.neighbors(node)}
        try:
            # assign the first available color to the current node
            coloring[node] = next(color for color in domain if color not in adjacent_colors)
        except StopIteration:
            print("Error: not enough colors in the domain")
            return None
    return coloring




