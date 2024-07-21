from algorithm import astar

file_path = './data/dataset-city.csv'
astar_search = astar.AStar(file_path)

start_city = "Linz"
end_city = "Ulm"
path = astar_search.a_star(start_city, end_city)

print("Path found:", path)
astar_search.draw_graph(path)
