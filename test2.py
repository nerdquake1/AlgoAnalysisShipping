import csv
import heapq

def load_data(file_name):
    graph = {}
    with open(file_name, 'r', newline='') as file:
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
    return graph

def dijkstra(graph, start, weight_type):
    visited = {start: (0, [start])}
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > visited[current_node][0]:
            continue
        
        for neighbor, tpt_day_weight, rate_weight in graph[current_node]:
            if weight_type == 'tpt_day_cnt':
                weight = tpt_day_weight
            else:
                weight = rate_weight
                
            distance = current_distance + weight
            path = visited[current_node][1] + [neighbor]
            
            if neighbor not in visited or distance < visited[neighbor][0]:
                visited[neighbor] = (distance, path)
                heapq.heappush(queue, (distance, neighbor))
    
    return visited

def main():
    file_name = 'Restructured.csv'
    start_port = 'PORT01'  # Specify the port you want to start from
    
    graph = load_data(file_name)
    
    # Find shortest path based on tpt_day_cnt
    shortest_paths_tpt = dijkstra(graph, start_port, 'tpt_day_cnt')
    
    # Find cheapest path based on rate
    shortest_paths_rate = dijkstra(graph, start_port, 'rate')
    
    for port, (distance_tpt, path_tpt) in shortest_paths_tpt.items():
        distance_rate, path_rate = shortest_paths_rate[port]
        print(f"Destination: {port}")
        print(f"Shortest path based on tpt_day_cnt: {path_tpt}, Distance: {distance_tpt}")
        print(f"Cheapest path based on rate: {path_rate}, Cost: {distance_rate}")
        print("")
if __name__ == "__main__":
    main()
