import abc
from queue import PriorityQueue


class Strategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def calculate_path(cls, graph, start_vertex) -> list:
        """ Calculates the shortest path from the start node to the end node."""
        pass


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

class Dijkstra( Strategy ):
    @classmethod
    def calculate_path(cls, graph: Graph, start_vertex) -> list:
        """calculates the shortest path between two nodes using the Dijkstra algorithm.
        
        The Dijkstra algorithm is a greedy algorithm that finds the shortest path between two nodes in a graph.
            
        ARGS:
            graph: Graph: the graph object describing ...
            start: int: the node from which the distances are calculated
            
        RETURNS:
            the distances from the starting point to every other point

        """
        """
        :param nodes: list of nodes
        :param index: index of the starting node
        :return: the shortest path from the starting node to all the other nodes
        """
        D = {v:float('inf') for v in range(graph.v)} # initialize the distances to infinity
        D[start_vertex] = 0 # the distance from the starting node to itself is 0

        pq = PriorityQueue() # initialize the priority queue
        pq.put((0, start_vertex)) # add the starting node to the priority queue

        while not pq.empty(): # while the priority queue is not empty
            (dist, current_vertex) = pq.get() # get the node with the smallest distance
            graph.visited.append(current_vertex) # add the node to the visited list

            for neighbor in range(graph.v): # for every neighbor of the current node
                if graph.edges[current_vertex][neighbor] != -1: # if the edge exists
                    distance = graph.edges[current_vertex][neighbor] + dist # calculate the distance
                    if neighbor not in graph.visited:   # if the neighbor has not been visited
                        old_cost = D[neighbor] # get the old cost
                        new_cost = D[current_vertex] + distance # calculate the new cost
                        if new_cost < old_cost: # if the new cost is smaller than the old cost
                            pq.put((new_cost, neighbor)) # update the cost of the neighbor
                            D[neighbor] = new_cost # update the cost of the neighbor
        return D # return the distances
    

class PathFinder:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    def findPath(self, graph, start_vertex) -> list:
        """ Finds the shortest path between two nodes in a graph.
        
        ARGS:
            graph: Graph: the graph object describing ...
            start: int: the node from which the distances are calculated
        
        RETURNS:
            the distances from the starting point to every other point
        """
        
        return self.strategy.calculate_path(graph, start_vertex)
    


def main() -> None:
    graph = Graph(14)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 4, 1)
    graph.add_edge(3, 5, 1)
    graph.add_edge(5, 6, 1)
    graph.add_edge(5, 7, 1)
    graph.add_edge(5, 8, 1)
    graph.add_edge(8, 9, 1)
    graph.add_edge(8, 10, 1)
    graph.add_edge(8, 11, 1)
    graph.add_edge(11, 12, 1)
    graph.add_edge(11, 13, 1)
    
    path_finder = PathFinder(Dijkstra)
    path = path_finder.findPath(graph, 0)
    for vertex in range(len(path)):
        print("Distance from vertex 0 to vertex", vertex, "is", path[vertex])


if __name__ == '__main__':
    main()