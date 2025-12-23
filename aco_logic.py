import numpy as np
import random

class AntColonyOptimizer:
    def __init__(self, distances, n_ants, n_iterations, alpha=1, beta=2, rho=0.5, q=100):
        self.distances = distances
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        self.n_points = len(distances)
        self.pheromone = np.ones((self.n_points, self.n_points))
        
    def run(self):
        best_path = None
        best_distance = float('inf')
        distance_history = []
        for i in range(self.n_iterations):
            all_paths = self.construct_colony_paths()
            self.update_pheromones(all_paths)
            current_best_path, current_best_dist = min(all_paths, key=lambda x: x[1])
            if current_best_dist < best_distance:
                best_distance = current_best_dist
                best_path = current_best_path
            distance_history.append(best_distance)
        return best_path, best_distance, distance_history

    def construct_colony_paths(self):
        paths = []
        for _ in range(self.n_ants):
            path = self.generate_single_path()
            paths.append((path, self.calculate_total_distance(path)))
        return paths

    def generate_single_path(self):
        start_node = random.randint(0, self.n_points - 1)
        path = [start_node]
        visited = {start_node}
        while len(visited) < self.n_points:
            current = path[-1]
            probs = self.calculate_probabilities(current, visited)
            next_node = np.random.choice(range(self.n_points), p=probs)
            path.append(next_node)
            visited.add(next_node)
        path.append(path[0])
        return path

    def calculate_probabilities(self, current, visited):
        tau = np.power(self.pheromone[current], self.alpha)
        eta = np.power(1.0 / (self.distances[current] + 1e-10), self.beta)
        probabilities = tau * eta
        for node in visited:
            probabilities[node] = 0
        return probabilities / probabilities.sum()

    def update_pheromones(self, all_paths):
        self.pheromone *= (1 - self.rho)
        for path, dist in all_paths:
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i+1]] += self.q / dist

    def calculate_total_distance(self, path):
        return sum(self.distances[path[i]][path[i+1]] for i in range(len(path)-1))