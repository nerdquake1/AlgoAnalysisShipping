import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A','B'),('A','C'), ('C','B')])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos, node_size=500)
nx.draw_networkx_edges(G,pos, edge_color='black')
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos)

plt.show()