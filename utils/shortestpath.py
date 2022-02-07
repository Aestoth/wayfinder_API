import abc
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Strategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def calculate_path(cls, graph, initial, end) -> list:
        """ Calculates the shortest path from the start node to the end node."""
        pass


class Graph():
    def __init__(self):
        """
        Initialize a graph object.
        """
        self.edges = defaultdict(list) # dictionary of neighbors
        self.weights = {} # dictionary of weights
    
    def add_edge(self, from_node, to_node, weight): # add an edge to the graph
        self.edges[from_node].append(to_node) # add the to_node to the list of neighbors of the from_node
        self.edges[to_node].append(from_node) # add the from_node to the list of neighbors of the to_node
        self.weights[(from_node, to_node)] = weight # add the weight of the edge to the dictionary of weights
        self.weights[(to_node, from_node)] = weight # add the weight of the edge to the dictionary of weights
    
     

class Dijkstra( Strategy ):
    @classmethod
    def calculate_path(cls, graph, initial, end) -> list:
        """calculates the shortest path between two nodes using the Dijkstra algorithm.

            The Dijsktra algorithm is a greedy algorithm that finds the shortest path between two nodes in a graph.
        
            ARGS:
                graph: Graph: the graph object describing ...
                start: int: the node from which the distances are calculated
                target: int: the node to which the distances are calculated
        
            RETURNS:
                the distances from the starting point to every other point
        """
        shortest_paths = {initial: (None, 0)} # dictionary of shortest paths
        current_node = initial # the current node
        visited = set() # the set of visited nodes
        
        while current_node != end:  # while the current node is not the end node
            visited.add(current_node) # add the current node to the set of visited nodes
            destinations = graph.edges[current_node] # get the neighbors of the current node
            weight_to_current_node = shortest_paths[current_node][1] # get the weight of the current node

            for next_node in destinations: # for every neighbor of the current node
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node # get the weight of the edge between the current node and the neighbor
                if next_node not in shortest_paths: # if the neighbor is not in the dictionary of shortest paths
                    shortest_paths[next_node] = (current_node, weight) # add the neighbor to the dictionary of shortest paths
                else:
                    current_shortest_weight = shortest_paths[next_node][1] # get the weight of the shortest path to the neighbor
                    if current_shortest_weight > weight: # if the weight of the shortest path to the neighbor is greater than the weight of the edge between the current node and the neighbor
                        shortest_paths[next_node] = (current_node, weight) # update the shortest path to the neighbor
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited} # get the neighbors of the current node that are not visited
            if not next_destinations: # if there are no neighbors that are not visited
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1]) # get the node with the lowest weight
        path = [] # the path from the start node to the end node
        while current_node is not None: # while the current node is not None
            path.append(current_node) # add the current node to the path
            next_node = shortest_paths[current_node][0] # get the next node in the path
            current_node = next_node # set the current node to the next node
        path = path[::-1] # reverse the path
        return path # return the path
    

class PathFinder:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    def find_path(self, graph, initial, end) -> list:
        """ Finds the shortest path between two nodes in a graph.
        
        ARGS:
            graph: Graph: the graph object describing ...
            start: int: the node from which the distances are calculated
        
        RETURNS:
            the distances from the starting point to every other point
        """
        return self.strategy.calculate_path(graph, initial, end)
                  

def main() -> None:
    graph = Graph()
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (1, 3, 1),
        (3, 4, 1),
        (3, 5, 1),
        (5, 6, 1),
        (5, 7, 1),
        (5, 8, 1),
        (8, 9, 1),
        (8, 10, 1),
        (8, 11, 1),
        (11, 12, 1),
        (11, 13, 1),
    ]
    for edge in edges:
        graph.add_edge(*edge)
    
    path_finder = PathFinder(Dijkstra)
    path = path_finder.find_path(graph, 0, 6)
    for vertex in range(len(path)):
        print("Distance from vertex 0 to vertex", vertex, "is", path[vertex])

if __name__ == '__main__':
    main()
    
   
   
   
    