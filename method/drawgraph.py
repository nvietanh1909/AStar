import networkx as nx
import matplotlib.pyplot as plt
from readdata import read_dataset_city

# Đọc file
data_table = read_dataset_city("./data/dataset-city.csv")

# Tạo đồ thị
G = nx.Graph()

# Thêm cạnh vào đồ thị từ dữ liệu
for _, row in data_table.iterrows():
    G.add_edge(row['First'], row['Last'], weight=row['Distance'])

# Vẽ đồ thị
plt.figure(figsize=(18, 12))
pos = nx.spring_layout(G, seed= 42)  # Sử dụng thuật toán spring layout để định vị các đỉnh trong đồ thị
nx.draw(G, pos, with_labels=True, node_size=1200, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

plt.title('Graph of Cities and Distances')
plt.tight_layout()
plt.show()
