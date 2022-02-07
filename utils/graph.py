import networkx as nx
from matplotlib import pyplot as plt


def draw_path() -> None:
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
    




if __name__ == '__main__':
    draw_path()

 
