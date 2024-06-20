from algorithm import astar as AStar

# Main
a_star = AStar.AStar()
data = a_star.read_file_data("./data/dataset-city.csv")
a_star.build_graph(data)
start_city = 'Linz'
goal_city = 'Ulm'
path = a_star.a_star_algorithm(start_city, goal_city)
if path:
    print(f"Found path: {path}")
    a_star.draw_graph(path)
else:
    print(f"No path found from {start_city} to {goal_city}")
