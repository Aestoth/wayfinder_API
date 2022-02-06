import abc
import collections as col
from queue import PriorityQueue


class Strategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def calculate_path(cls, graph, index=0) -> list:
        """ Calculates the shortest path from the start node to the end node."""
        pass


class Graph:
    def __init__(self) -> None:
        self.nodes = set() # The set of nodes.
        self.edges = col.defaultdict(list) # The edges of the graph.
        self.distances = {} # The distances of the graph.
        
    
    def add_node(self, value):
        self.nodes.add(value) # Add the node to the graph.
        
    
    def add_edges_from(self, From, To, distance) -> None:
        """ Add an edge from node From to node To.
        
        ARGS:
            From: int: the node from which the edge starts
            To: int: the node at which the edge ends
        
        """
        self.edges[From].append(To) # Add the edge to the graph.
        self.edges[To].append(From) # Add the edge to the graph.
        self.distances[(From, To)] = distance # Add the distance to the graph.
        self.distances[(To, From)] = distance # Add the distance to the graph.


class Dijkstra( Strategy ):
    @classmethod
    def calculate_path(self, graph: Graph, initial):
        """ Finds the shortest path between two nodes in a graph.
        
        ARGS:
            initial: int: the node from which the distances are calculated
        
        """
        visited = {initial: 0} # Initialize the distances to infinity.
        path = {} # Initialize the distances to infinity.
        path_all = col.defaultdict(list) # Initialize the distances to infinity.
        path_all[initial] = [initial] # The distance from the starting node to itself is 0.
        
        
        # Initialize the priority queue.
        pq = PriorityQueue()
        
        # Add the starting node to the priority queue.
        pq.put((0, initial))
        
        # set unvisited nodes
        unvisited = set(graph.nodes)
        
        # While the priority queue is not empty.
        while not pq.empty():
            min = pq.get() # Get the node with the smallest distance.
            for node in unvisited: # For every neighbor of the current node.
                if node in visited: # If the node has already been visited.
                    if min is None: # If the priority queue is empty.
                        min = node # Set the node as the current node.
                elif visited[node] < visited[min]: # If the distance to the neighbor is smaller than the distance to the current node.
                    min = node  # Set the node as the current node.
            
            if min is None: # If the priority queue is empty.
                break # Break the loop.
            
class PathFinder:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        
    @property
    def strategy(self) -> Strategy:
        return self._strategy

    
    def find_path(self, graph, start) -> list:
        """ Finds the shortest path between two nodes in a graph.
        
        ARGS:
            graph: Graph: the graph object describing ...
            start: int: the node from which the distances are calculated
        
        RETURNS:
            the distances from the starting point to every other point
        """
        
        return self.strategy.calculate_path(graph, start)                


def main() -> None:
    graph = Graph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edges_from(0, 1, 7)
    graph.add_edges_from(0, 2, 9)
    graph.add_edges_from(0, 5, 14)
    graph.add_edges_from(1, 2, 10)
    graph.add_edges_from(1, 3, 15)
    graph.add_edges_from(2, 3, 11)
    graph.add_edges_from(2, 5, 2)
    graph.add_edges_from(3, 4, 6)
    
    finder = PathFinder(Dijkstra)
    print(finder.find_path(graph, 0))
    
if __name__ == '__main__':
    main()
        