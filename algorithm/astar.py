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
        
        # Danh sách các thành phố cần kiểm tra
        open_list = []
        # Thêm thành phố bắt đầu vào danh sách mở với chi phí f = 0.   
        heapq.heappush(open_list, (0, start))  
        # Dict lưu trữ chi phí g từ điểm bắt đầu đến các thành phố khác
        g_cost = {start: 0}
        # Từ điển lưu trữ cha của từng thành phố để xây dựng đường đi
        parent = {start: None}

        while open_list:
            # Lấy thành phố với chi phí f thấp nhất
            current_f, current_node = heapq.heappop(open_list)
            # Nếu đã đến thành phố kết thúc, xây dựng và trả về đường đi
            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                return path[::-1]
            
            for neighbor, distance in get_neighbors(current_node):
                # Tính toán chi phí g mới cho neighbor
                new_g_cost = g_cost[current_node] + distance  
                if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_g_cost
                    # Tính toán chi phí f = g + h
                    f_cost = new_g_cost + heuristic(neighbor) 
                    # Thêm neighbor vào danh sách mở 
                    heapq.heappush(open_list, (f_cost, neighbor))  
                    parent[neighbor] = current_node
        return None

    def draw_graph(self, path):
        G = nx.Graph()
        # Tạo đồ thị từ dữ liệu
        for city, neighbors in self.graph.items():
            for neighbor, distance in neighbors:
                G.add_edge(city, neighbor, weight=distance)
        
        # Tạo vị trí cho các nút trong đồ thị với seed = 39
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
        
        plt.title("A* Algorithm Path")
        plt.show()
    class Node:
        def __init__(self, position, parent=None):
            # Vị trí của nút (thành phố)
            self.position = position 
            # Nút cha của nút này
            self.parent = parent
            # Chi phí từ điểm bắt đầu đến nút hiện tại
            self.g = 0
            # Dự đoán chi phí từ nút hiện tại đến điểm kết thúc (heuristic)              
            self.h = 0
            # Tổng chi phí f = g + h         
            self.f = 0               
        
        def __lt__(self, other):
            # So sánh hai nút dựa trên giá trị f để sử dụng
            return self.f < other.f

