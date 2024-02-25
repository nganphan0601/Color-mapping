import networkx as nx
import matplotlib.pyplot as plt
from algorithm import greedy_coloring, is_valid_coloring

#Canada map

# variables for the provinces and their neighbors
provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE',
             'QC', 'SK', 'YT']
neighbors = [('AB', 'BC'), ('AB', 'NT'), ('AB', 'SK'), ('BC', 'NT'), ('BC', 'YT'),
             ('MB', 'NU'), ('MB', 'ON'), ('MB', 'SK'), ('NB', 'NS'), ('NB', 'QC'),
             ('NL', 'QC'), ('NT', 'NU'), ('NT', 'SK'), ('NT', 'YT'), ('ON', 'QC')]

#Canada map
Canada = nx.Graph()
Canada.add_nodes_from(provinces)
Canada.add_edges_from(neighbors)
colors = ['y', 'r', 'b']

# draw the graph

print("Graph nodes: ", Canada.nodes())
print("Graph edges: ", Canada.edges())

nx.draw(Canada, with_labels=True)
plt.show()


# apply the greedy algorithm
coloring = greedy_coloring(Canada, colors)

print("Coloring result: ", coloring)
print("Is valid coloring: ", is_valid_coloring(Canada, coloring))
print("K: ", len(set(coloring.values())))

# draw the graph
color_map = [coloring[node] for node in Canada.nodes()]
nx.draw(Canada, with_labels=True, node_color=color_map, font_weight='bold')
plt.show()