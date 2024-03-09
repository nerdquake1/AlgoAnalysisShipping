import csv
import heapq

def read_data(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            carrier = row['Carrier']
            orig_port_cd = row['orig_port_cd']
            dest_port_cd = row['dest_port_cd']
            min_cost = float(row['minimum_cost'].replace('$', '').replace(',', '').strip())
            tpt_day_cnt = int(row['tpt_day_cnt'])
            
            if orig_port_cd not in data:
                data[orig_port_cd] = {}
            data[orig_port_cd][dest_port_cd] = (min_cost, tpt_day_cnt)
    return data

def dijkstra(data, start):
    distances = {port: (float('inf'), float('inf'), None) for port in data}
    distances[start] = (0, 0, None)
    priority_queue = [(0, 0, start)]

    while priority_queue:
        total_cost, total_days, current = heapq.heappop(priority_queue)

        if total_cost > distances[current][0] or total_days > distances[current][1]:
            continue

        for neighbor, (cost, days) in data.get(current, {}).items():
            new_cost = total_cost + cost
            new_days = total_days + days
            if new_cost < distances[neighbor][0] or (new_cost == distances[neighbor][0] and new_days < distances[neighbor][1]):
                distances[neighbor] = (new_cost, new_days, current)
                heapq.heappush(priority_queue, (new_cost, new_days, neighbor))

    return distances

def shortest_path_to_each_location(data, start):
    shortest_paths = {}
    for port in data:
        distances = dijkstra(data, start)
        shortest_paths[port] = distances[port]
    return shortest_paths

def cheapest_path_to_each_location(data, start):
    cheapest_paths = {}
    for port in data:
        distances = dijkstra(data, start)
        cheapest_paths[port] = min(distances.values())
    return cheapest_paths

if __name__ == "__main__":
    filename = 'data.csv'
    data = read_data(filename)

    start_port = 'PORT03'  # Change this to your desired origin port code

    shortest_paths = shortest_path_to_each_location(data, start_port)
    cheapest_paths = cheapest_path_to_each_location(data, start_port)

    print("Shortest paths to each location:")
    for port, distance in shortest_paths.items():
        print(f"{port}: {distance}")

    print("\nCheapest paths to each location:")
    for port, distance in cheapest_paths.items():
        print(f"{port}: {distance}")
