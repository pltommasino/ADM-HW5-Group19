import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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
    print("The name of graph selected is: " + name_graph)

    #Nodes
    print("The number of the nodes in the graph: %i" %len(graph.nodes))

    #Edges
    print("The number of the edges in the graph: %i" %len(graph.edges))
    
    #Density
    density = nx.density(graph)
    print("The Graph Density is: %g" %density)

    #Degree distribution
    degree_sequence = [d for n, d in graph.degree()]
    plt.bar(*np.unique(degree_sequence, return_counts=True))
    plt.title("Degree histogram")
    plt.xlabel("Degree")
    plt.ylabel("Number of Nodes")
    plt.show()

    # Average degree
    avg_degree = np.mean(degree_sequence)
    print("The Average Degree is: %d" %avg_degree)

    # Hubs
    percentile_95 = np.percentile(degree_sequence, 95)
    hubs = [node for node, degree in graph.degree() if degree > percentile_95]
    print("The Hubs are: %ls" %hubs)

    #Graph classification
    if density < 0.5:
        classification_graph = 'Sparse'
    else:
        classification_graph = 'Dense'
    print("The Selected Graph is: %s" %classification_graph)
        

def functionality_2(graph, node_selected, name_graph):
    '''
    Input:
    - The graph
    - A node of the graph (paper/author)
    - The name of the graph
    
    Output:
    - The centrality of the node, calculated based on the following centrality measurements:
        - Betweeness
        - PageRank
        - ClosenessCentrality
        - DegreeCentrality
    '''
    #Name graph
    print("The name of graph selected is: " + name_graph)

    #Betweenness Centrality
    betw = nx.betweenness_centrality(graph)
    print("The Betweenness Centrality of selected node is: %g" %betw[node_selected])
    
    #PageRank Centrality
    pagerank = nx.pagerank(graph)
    print("The PageRank Centrality of selected node is: %g" %pagerank[node_selected])
    
    #Closeness Centrality
    closeness = nx.closeness_centrality(graph)
    print("The Closeness Centrality of selected node is: %g" %closeness[node_selected])
    
    #Degree Centrality
    degree = nx.degree_centrality(graph)
    print("The Degree Centrality of selected node is: %g" %degree[node_selected])
   

def functionality_3(graph_data, sequence_authors, node_first, node_last, N):
    '''
    Input:
    - The graph data
    - A sequence of authors_a = [a_2, ..., a_{n-1}]
    - Initial node a_1
    - End node a_n
    - N: denoting the top N authors whose data should be considered

    Output:
    - The shortest walk of collaborations you need to read to get from author a_1 to author a_n and the papers you need to cross to realize this walk.
    '''