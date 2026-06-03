from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx
        self.name = name
        self.line = line
        self.neighbors: List[Tuple['Station', int]] = []  # (station, time) tuples

    def append_neighbor(self, station: 'Station', time: int):
        self.neighbors.append((station, time)) #Neighbors station and the time to reach it

class MetroNetwork: #It manages all the stations and the line.
    def __init__(self):
        self.stations: Dict[str, Station] = {} #All stations dictionary
        self.lines: Dict[str, List[Station]] = defaultdict(list)#Dictionary that stores which station is on which line.

    def append_station(self, idx: str, name: str, line: str) -> None:
        if idx not in self.stations:
            station = Station(idx, name, line)
            self.stations[idx] = station
            self.lines[line].append(station)

    def append_connection(self, station1_id: str, station2_id: str, time: int) -> None:
        station1 = self.stations[station1_id]
        station2 = self.stations[station2_id]
        station1.append_neighbor(station2, time)
        station2.append_neighbor(station1, time)

    def find_least_transfers_route(self, start_id: str, target_id: str) -> Optional[List[Station]]:
        """Finds the route with the fewest transfers using the BFS algorithm

        Complete this function:
        1. Check for the existence of starting and destination stations.
        2. Find the route with the fewest transfers using the BFS algorithm.
        3. Return None if the route is not found, and a list of stations if it is found.
        4. After completing the function, remove the #TODO and pass lines.

        Tips:
        - Create a queue using collections.deque, HINT: queue = deque([(start, [start])])
        - Track visited stations.
        - Discover neighboring stations at each step.
        """
        if start_id not in self.stations or target_id not in self.stations:#If it does not include either the starting or target stations, none will be returned.
            return None
        start = self.stations[start_id]
        target = self.stations[target_id]
        visited = {start_id} # The reason we keep the stations we visit in a set is because we want to visit each station only once.
        queue = deque([(start, [start])]) # The starting station is added to the queue and stored.
        while queue: # It will run until the queue is empty.
            station, path = queue.popleft() # I took the station at the beginning of the queue. I would have done it with pop(0), but I used popleft() after researching the issue.
            if station == target:
             return path # If the target is reached, the route is found and the path is returned.
            for neighbor, _ in station.neighbors:## It checks the neighbor and time values ​​among the neighboring stations of the current station. However, since the time value is not useful in this minimum_transfer_find function we defined, we showed it as "_".
               if neighbor not in visited:# I checked if the neighboring station has been visited before.
                visited.add(neighbor)  # I add the neighbor I visited to the visited_neighbor set.
                queue.append((neighbor, path + [neighbor]))  # I add the neighbor of the station I am working on and the neighbor to the end of the current path.
        return None # If the destination is not reached, none is returned.

            
    
        
        
    def find_fastest_route(self, start_id: str, target_id: str) -> Optional[Tuple[List[Station], int]]:
        """Finds the fastest route using the A* algorithm

        Complete this function:
        1. Check for the existence of starting and destination stations.
        2. Find the fastest route using the A* algorithm.
        3. Return None if no route is found, and (station_list, total_time) tuple if found.
        4. After completing the function, remove the #TODO and pass lines.

        Tips:
        - Create a priority queue using the heapq module, HINT: pq = [(0, id(start), start, [start])]
        - Track visited stations.
        - Calculate total time at each step.
        - Select the route with the shortest time.
        """
        
        if start_id not in self.stations or target_id not in self.stations:#If it does not include either the starting or target stations, none will be returned.
            return None

        start = self.stations[start_id]
        target = self.stations[target_id]
        visited = set()#We created a set to store the neighboring stations we recently visited.
        pq = [(0, id(start), start, [start])]#I'm creating a list with a starting station and including (time, ID, station, route). 
        while pq:#I used the `while` keyword to make it run until the queue is empty.
            total_time, _, station, path = heapq.heappop(pq)#We are using the station with the lowest output using 'heapq.heappop(pq)'.
            if station == target:
                return path, total_time#The route and total time are returned when the target station is reached. #I updated the total time by visiting neighboring stations.
            for neighbor, time in station.neighbors:#Neighboring houses at neighboring stations to the current station are watching the time.
                if neighbor not in visited:  # Neighbor hasn't been visited yet.
                   visited.add(neighbor)#We're adding neighbors we haven't visited to the visited list.
                   new_total_time = total_time + time#I'm getting a new total time by adding the neighbor's time to the initial total time.
       #I'm adding the total time and route to the neighboring station to the queue.
                   heapq.heappush(pq, (new_total_time, id(neighbor), neighbor, path + [neighbor])) 
        return None
#Example Usage
if __name__ == "__main__":
    metro = MetroNetwork()
    
# Adding stations
# Red Line
    metro.append_station("K1", "Kızılay", "Red Line")
    metro.append_station("K2", "Ulus", "Red Line")
    metro.append_station("K3", "Demetevler", "Red Line")
    metro.append_station("K4", "OSB", "Red Line")
    
    # Blue Line
    metro.append_station("M1", "AŞTİ", "Blue Line")
    metro.append_station("M2", "Kızılay", "Blue Line")  # Trasfer point
    metro.append_station("M3", "Sıhhiye", "Blue Line")
    metro.append_station("M4", "Gar", "Blue Line")
    
    # Orange Line
    metro.append_station("T1", "Batıkent", "Orange Line")
    metro.append_station("T2", "Demetevler", "Orange Line")  # Transfer point
    metro.append_station("T3", "Gar", "Orange Line")  # Transfer point
    metro.append_station("T4", "Keçiören", "Orange Line")
    
    # Append connections
    # Red Line connections
    metro.append_connection("K1", "K2", 4)  # Kızılay -> Ulus
    metro.append_connection("K2", "K3", 6)  # Ulus -> Demetevler
    metro.append_connection("K3", "K4", 8)  # Demetevler -> OSB
    
    # Blue Line connections
    metro.append_connection("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.append_connection("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.append_connection("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Orange Line connections
    metro.append_connection("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.append_connection("T2", "T3", 9)  # Demetevler -> Gar
    metro.append_connection("T3", "T4", 5)  # Gar -> Keçiören
    
    # Line transfer connections (same station, different lines)
    metro.append_connection("K1", "M2", 2)  # Kızılay transfer
    metro.append_connection("K3", "T2", 3)  # Demetevler transfer
    metro.append_connection("M4", "T3", 2)  # Gar transfer
    
    # Test Scenarios
    print("\n=== Test Scenarios ===")
    
    # Scenario 1: From AŞTİ to OSB
    print("\n1.From AŞTİ to OSB:")
    rota = metro.find_least_transfers_route("M1", "K4")
    if rota:
        print("The route with the fewest transfers:", " -> ".join(i.name for i in rota))
    
    result = metro.find_fastest_route("M1", "K4")
    if result:
        route, time = result
        print(f"The fastest route ({time} minutes):", " -> ".join(i.name for i in route))
    
    # Scenario 2: From Batıkent to Keçiören
    print("\n2. From Batıkent to Keçiören:")
    rota = metro.find_least_transfers_route("T1", "T4")
    if rota:
        print("The route with the fewest transfers:", " -> ".join(i.name for i in rota))
    
    result = metro.find_fastest_route("T1", "T4")
    if result:
        route, time = result
        print(f"The fastest route ({time} minutes):", " -> ".join(i.name for i in route))
    
    # Scenario 3: From Keçiören to AŞTİ
    print("\n3. From Keçiören to AŞTİ:")
    route = metro.find_least_transfers_route("T4", "M1")
    if route:
        print("The route with the fewest transfers:", " -> ".join(i.name for i in route))
    
    result = metro.find_fastest_route("T4", "M1")
    if result:
        route, time = result
        print(f"The fastest route ({time} minutes):", " -> ".join(i.name for i in route))
    # Scenario 4: From Kızılay to Demetevler (I added this)
    print("\n4. From Kızılay to Demetevler:")
    route = metro.find_least_transfers_route("K1", "K3")
    if route:
        print("The route with the fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("K1", "K3")
    if result:
        route, time = result
        print(f"The fastest route ({time} minutes):", " -> ".join(i.name for i in route))
