import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('A','B'),('A','C'), ('C','B')])

Lanes = nx.DiGraph()
LanesRate = nx.DiGraph()

with open("Restructured.csv", 'r', newline='') as file:
        graph = {}
        reader = csv.DictReader(file)
        for row in reader:
            origin = row['orig_port_cd']
            destination = row['dest_port_cd']
            tpt_day_weight = int(row['tpt_day_cnt'])
            rate_weight = float(row['rate'].strip().replace('$', '').replace(',', ''))
            if origin not in graph:
                graph[origin] = []
            graph[origin].append((destination, tpt_day_weight, rate_weight))
            if destination not in graph:
                graph[destination] = []
            graph[destination].append((origin, tpt_day_weight, rate_weight))
            

            if not LanesRate.has_edge(origin,destination):
                LanesRate.add_edge(origin,destination, weight = rate_weight)
            else:
                edgeData = LanesRate.get_edge_data(origin,destination)
                if edgeData["weight"] > rate_weight:
                     LanesRate.remove_edge(origin,destination)
                     LanesRate.add_edge(origin,destination, weight = rate_weight)
            if not Lanes.has_edge(origin,destination):
                Lanes.add_edge(origin,destination, weight = tpt_day_weight)
            else:
                edgeData = Lanes.get_edge_data(origin,destination)
                if edgeData["weight"] > tpt_day_weight:
                     Lanes.remove_edge(origin,destination)
                     Lanes.add_edge(origin,destination, weight = tpt_day_weight)
            
            
            

Lanes.remove_edges_from(nx.selfloop_edges(Lanes))
LanesRate.remove_edges_from(nx.selfloop_edges(LanesRate))

seed = 33
pos1 = nx.spring_layout(Lanes,seed=seed)
nx.draw_networkx_nodes(Lanes,pos1, node_size=500)
nx.draw_networkx_edges(Lanes,pos1, edge_color='black')
nx.draw_networkx_labels(Lanes,pos1)
edge_labels = nx.get_edge_attributes(Lanes, "weight")
nx.draw_networkx_edge_labels(Lanes,pos1, edge_labels, font_size=12)
plt.show()

seed = 33
pos1 = nx.spring_layout(LanesRate,seed=seed)
nx.draw_networkx_nodes(LanesRate,pos1, node_size=500)
nx.draw_networkx_edges(LanesRate,pos1, edge_color='black')
nx.draw_networkx_labels(LanesRate,pos1)
edge_labels = nx.get_edge_attributes(LanesRate, "weight")
nx.draw_networkx_edge_labels(LanesRate,pos1, edge_labels, font_size=15)
plt.show()

# nx.draw_networkx(Lanes) 

# pos1 = nx.spring_layout(Lanes)
# nx.draw_networkx_nodes(Lanes,pos1, node_size=500)
# nx.draw_networkx_edges(Lanes,pos1, edge_color='black')
# nx.draw_networkx_labels(Lanes,pos1)
# edge_labels = nx.get_edge_attributes(Lanes, "weight")
# nx.draw_networkx_edge_labels(Lanes,pos1, edge_labels)
# plt.show()

# pos2 = nx.spring_layout(LanesRate)
# nx.draw_networkx_nodes(LanesRate,pos2, node_size=500)
# nx.draw_networkx_edges(LanesRate,pos2, edge_color='black')
# nx.draw_networkx_labels(LanesRate,pos2)
# edge_labels = nx.get_edge_attributes(LanesRate, "weight")
# nx.draw_networkx_edge_labels(LanesRate,pos2, edge_labels)
# plt.show()




# with open("data.csv", 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             carrier = row['Carrier']
#             orig_port_cd = row['orig_port_cd']
#             dest_port_cd = row['dest_port_cd']
#             min_cost = float(row['minimum_cost'].replace('$', '').replace(',', '').strip())
#             tpt_day_cnt = int(row['tpt_day_cnt'])
#             Lanes.add_edge(orig_port_cd,dest_port_cd, weight = min_cost)




# pos = nx.spring_layout(G)

# nx.draw_networkx_nodes(G,pos, node_size=500)
# nx.draw_networkx_edges(G,pos, edge_color='black')
# nx.draw_networkx_labels(G,pos)
# nx.draw_networkx_edge_labels(G,pos)

# plt.show()