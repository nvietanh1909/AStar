import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class AStar:
    # Constructor
    def __init__(self) -> None:
        self.graph = nx.Graph()

    # Read dataset form data file
    def read_file_data(self, path: str) -> pd.DataFrame:
        data = pd.read_csv(path)
        return data
    
    # Create graph
    def build_graph(self, data: pd.DataFrame) -> None:
        for _, row in data.iterrows():
            self.graph.add_edge(row['First'], row['Last'], weight=row['Distance'])
            for node in [row['First'], row['Last']]:
                self.graph.nodes[node]['Estimated Distance to Ulm'] = row[f' Estimated Distance to Ulm']

    # Draw graph form dataset
    def draw_graph(self, path: list = None) -> None:
        plt.figure(figsize=(18, 12))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_size=1200, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels, font_size=8)
        if path:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=3.0)
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.show()

    # Estimates of the number of edges to reaching a goal
    def heuristic(self, n: str) -> float:
        return self.graph.nodes[n].get('Estimated Distance to Ulm', float('inf'))

    # A* algorithm
    def a_star_algorithm(self, start: str, goal: str) -> list:
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            return None
        open_set = set([start])
        closed_set = set([])
        g = {start: 0}
        parents = {start: start}
        while open_set:
            n = min(open_set, key=lambda v: g[v] + self.heuristic(v))
            if n == goal:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start)
                path.reverse()
                return path
            open_set.remove(n)
            closed_set.add(n)
            for neighbor in self.graph.neighbors(n):
                if neighbor in closed_set:
                    continue

                tentative_g_score = g[n] + self.graph[n][neighbor]['weight']
                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tentative_g_score > g.get(neighbor, float('inf')):
                    continue
                parents[neighbor] = n
                g[neighbor] = tentative_g_score
        return None