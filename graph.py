import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A','B'),('A','C'), ('C','B')])

Lanes = nx.DiGraph()


with open("data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            carrier = row['Carrier']
            orig_port_cd = row['orig_port_cd']
            dest_port_cd = row['dest_port_cd']
            min_cost = float(row['minimum_cost'].replace('$', '').replace(',', '').strip())
            tpt_day_cnt = int(row['tpt_day_cnt'])
            Lanes.add_edge(orig_port_cd,dest_port_cd, weight = min_cost)

pos1 = nx.spring_layout(Lanes)
nx.draw_networkx_nodes(Lanes,pos1, node_size=500)
nx.draw_networkx_edges(Lanes,pos1, edge_color='black')
nx.draw_networkx_labels(Lanes,pos1)
edge_labels = nx.get_edge_attributes(Lanes, "weight")
nx.draw_networkx_edge_labels(Lanes,pos1, edge_labels)
plt.show()


# pos = nx.spring_layout(G)

# nx.draw_networkx_nodes(G,pos, node_size=500)
# nx.draw_networkx_edges(G,pos, edge_color='black')
# nx.draw_networkx_labels(G,pos)
# nx.draw_networkx_edge_labels(G,pos)

# plt.show()
