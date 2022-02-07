import networkx as nx
from matplotlib import pyplot as plt


def draw_graph() -> None:
    """ Draws the path on the graph. """
    
    g = nx.Graph() # create a directed graph
    g.add_nodes_from(range(14)) # add nodes to the graph
    g.add_edges_from([(0,1),(1,2),(1,3),(3,4),(3,5),(5,6),(5,7),(5,8),
        (8,9),(8,10),(8,11),(11,12),(11,13)])  # add edges to the graph
    labelmap = dict(zip(g.nodes(), ["0","1","2","3","4","5","6","7",
        "8","9","10","11","12","13"])) # create a dictionary mapping the nodes to their labels
    nx.draw(g, labels=labelmap, with_labels=True, node_size=1500, 
         node_color='black', edge_color='red', font_size=8, font_color='white') # draw the graph
    plt.show() # show the graph
    

def draw() -> None:
    edge_objects = [(0,1),(1,2),(1,3),(3,4),(3,5),(5,6),(5,7),(5,8),
        (8,9),(8,10),(8,11),(11,12),(11,13)]

    entrance = [0] # Mark two nodes (2 & 7) to be Entrances
    common_nodes = [1,3,5,8,11] #all the other nodes

    node_types = [(0, 'entrance')]

    #create the networkx Graph with node types and specifying edge distances
    G = nx.Graph()

    for n,typ in node_types:
        G.add_node(n, type=typ) #add each node to the graph

    for from_loc, to_loc in edge_objects:
        G.add_edge(from_loc, to_loc) #add all the edges   
    
    
    #Draw the graph (optional step)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G,'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
    nx.draw_networkx_nodes(G, pos, nodelist=entrance, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=common_nodes, node_color='r')
    plt.show()
    
def path():
    G = nx.Graph()
    
    G.add_edges_from([(0,1),(1,2),(1,3),(3,4),(3,5),(5,6),(5,7),(5,8),
        (8,9),(8,10),(8,11),(11,12),(11,13)])

    print( nx.shortest_path(G, source=0, target=6))
    nx.draw(G, with_labels=True, node_color='black', edge_color='red', font_size=8, font_color='white')
    plt.show()
    

        

if __name__ == '__main__':
    # draw_graph()
    # draw()
    path()

 
