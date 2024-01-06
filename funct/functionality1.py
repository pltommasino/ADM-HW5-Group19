import networkx as nx
import numpy as np

def functionality_1(graph, name_graph):
    '''
    Input:
    - The graph
    - The name of the graph

    Output:
    - The number of the nodes in the graph
    - The number of the edges in the graph
    - The graph density
    - The graph degree distribution
    - The average degree of the graph
    - The graph hubs (hubs are nodes having degrees more extensive than the 95th percentile of the degree distribution)
    - Whether the graph is dense or sparse
    '''

    #Name graph
    #print("The name of graph selected is: " + name_graph)

    #Nodes
    len_nodes = len(graph.nodes)
    #print("The number of the nodes in the graph: %i" %len_nodes)

    #Edges
    len_edges = len(graph.edges)
    #print("The number of the edges in the graph: %i" %len_edges)
    
    #Density
    density = nx.density(graph)
    #print("The Graph Density is: %g" %density)

    #Degree distribution
    degree_sequence = [d for n, d in graph.degree()]
    # plt.bar(*np.unique(degree_sequence, return_counts=True))
    # plt.title("Degree histogram")
    # plt.xlabel("Degree")
    # plt.ylabel("Number of Nodes")
    # plt.show()

    # Average degree
    avg_degree = np.mean(degree_sequence)
    #print("The Average Degree is: %d" %avg_degree)

    # Hubs
    percentile_95 = np.percentile(degree_sequence, 95)
    hubs = [node for node, degree in graph.degree() if degree > percentile_95]
    #print("The Hubs are: %ls" %hubs)

    #Graph classification
    if density < 0.5:
        classification_graph = 'Sparse'
    else:
        classification_graph = 'Dense'
    #print("The Selected Graph is: %s" %classification_graph)

    return len_nodes, len_edges, density, degree_sequence, avg_degree, hubs, classification_graph