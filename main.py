from algorithm import astar

file_path = './data/dataset-city.csv'
astar_search = astar.AStar(file_path)

start_city = "Linz"
end_city = "Ulm"
path, total_cost = astar_search.a_star(start_city, end_city)

if path:
    print(f"Đường đi từ {start_city} -> {end_city} :", path)
    print("Tổng chi phí:", total_cost)
    astar_search.draw_graph(path, total_cost)
else:
    print("Không tìm thấy đường đi")
