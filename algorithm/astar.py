import csv
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class AStar:
    def __init__(self, file_path):
        self.graph, self.heuristics = self.read_csv(file_path)
    
    def read_csv(self, file_path):
        graph = {}
        heuristics = {}
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            # Bỏ qua dòng đầu tiên
            next(reader)
            for row in reader:
                city1, city2, distance, heuristic = row[0], row[1], int(row[2]), int(row[3])
                
                # Nếu city1 chưa có trong đồ thị, thêm nó vào.
                if city1 not in graph:
                    graph[city1] = []
                # Nếu city2 chưa có trong đồ thị, thêm nó vào.
                if city2 not in graph:
                    graph[city2] = []
                
                # Thêm các kết nối vào đồ thị (cả hai hướng).
                graph[city1].append((city2, distance))
                graph[city2].append((city1, distance))
                
                # Cập nhật giá trị heuristic cho các thành phố.
                heuristics[city1] = heuristic
                heuristics[city2] = heuristics.get(city2, heuristic)
        
        return graph, heuristics

    def a_star(self, start, end):
        def heuristic(node):
            return self.heuristics.get(node, float('inf'))
        
        def get_neighbors(node):
            return self.graph.get(node, [])
        
        open_list = []
        heapq.heappush(open_list, (0, start))  
        # Chi phí từ điểm bắt đầu đến các nút
        g_cost = {start: 0}  
        parent = {start: None} 
        
        while open_list:
            current_f, current_node = heapq.heappop(open_list)
            
            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                path = path[::-1]
                
                # Tổng chi phí chính là g_cost của nút kết thúc
                total_cost = g_cost[end]
                return path, total_cost
            
            for neighbor, distance in get_neighbors(current_node):
                new_g_cost = g_cost[current_node] + distance
                if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_g_cost
                    f_cost = new_g_cost + heuristic(neighbor)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    parent[neighbor] = current_node
        return None, float('inf')  

    def draw_graph(self, path, total_cost):
        G = nx.Graph()
        for city, neighbors in self.graph.items():
            for neighbor, distance in neighbors:
                G.add_edge(city, neighbor, weight=distance)
        
        pos = nx.spring_layout(G, seed=39)
        plt.figure(figsize=(10, 8))
        
        # Vẽ đồ thị với các nút và cạnh
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
        
        if path:
            # Vẽ đường đi tìm được bằng màu đỏ
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        
        # Hiển thị chi phí vào đồ thị
        plt.text(0.05, 0.95, f"Total Cost: {total_cost}", 
            horizontalalignment='left', verticalalignment='top',
            fontsize=20, color='black', weight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
        
        plt.title("A* Algorithm Path")
        plt.show()

