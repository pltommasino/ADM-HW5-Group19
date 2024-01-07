import networkx as nx
import random

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
    if node_selected == 0:
        node_selected = random.sample(list(graph.nodes), 1)[0]

    #Betweenness Centrality
    betw2 = nx.betweenness_centrality(graph)
    betw = betw2[node_selected]
    #print("The Betweenness Centrality of selected node is: %g" %betw[node_selected])
    
    #PageRank Centrality
    pagerank2 = nx.pagerank(graph)
    pagerank = pagerank2[node_selected]
    #print("The PageRank Centrality of selected node is: %g" %pagerank[node_selected])
    
    #Closeness Centrality
    closeness2 = nx.closeness_centrality(graph)
    closeness = closeness2[node_selected]
    #print("The Closeness Centrality of selected node is: %g" %closeness[node_selected])
    
    #Degree Centrality
    degree2 = nx.degree_centrality(graph)
    degree = degree2[node_selected]
    #print("The Degree Centrality of selected node is: %g" %degree[node_selected])

    return betw, pagerank, closeness, degree