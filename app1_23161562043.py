from collections import deque

def bfs_shortest_path(city_map, start, goal):
    queue = deque([(start, [start])])  
    visited = set()  
    
    while queue:
        node, path = queue.popleft() 
        
        if node == goal:
            return path  
        
        if node not in visited:
            visited.add(node)
            for neighbor in city_map.get(node, []):
                queue.append((neighbor, path + [neighbor]))
    
    return None  

city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)
print("Jalur Terpendek:", shortest_path)
