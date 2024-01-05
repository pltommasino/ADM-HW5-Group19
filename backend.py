import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

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
    #print("The name of graph selected is: " + name_graph)

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



# Dijkstra's algorithm
def NextNode(dist, visited):
    '''
    ---
    Found the next node to operate on
    ---

    Input:
    - dist: list of distances
    - visited: list of all nodes if the node is visited (=True), not visited (=False)
    Output:
    - next_node: next node to operate on
    '''

    min = float('inf')
    next_node = -1
    for i in range(len(dist)):
        if (not visited[i]) and (dist[i] < min):
            next_node = i
            min = dist[i]
    return next_node

def getAdjacents(graph, node):
    '''
    ---
    Found the list of nodes adjacent to the node selected
    ---

    Input:
    - graph: graph
    - node: node of graph
    Output:
    - list_nodes_adjacent: list of nodes adjacent to the node
    '''

    list_nodes_adjacent = []
    for j in range(len(graph)):
        if graph[node][j] != float('inf'):
            list_nodes_adjacent.append([j, graph[node][j]])
    return list_nodes_adjacent

def Dijkstra(graph, node_start):
    '''
    Input:
    - graph
    - node_start: start node to calculate minimum distances
    - authors_sequence: list of authors to consider
    Output:
    - dist: list of distances
    '''

    n = len(graph)

    dist = []
    visited = []

    for i in range(n):
        dist.append(float('inf'))
        visited.append(False)

    dist[node_start] = 0

    for i in range(n - 1):
        next = NextNode(dist, visited)
        visited[next] = True
        V = getAdjacents(graph, next)
        for [z, w] in V:
            d = dist[next] + w
            if dist[z] > d:
                dist[z] = d

    return dist

def functionality_3(graph, sequence_authors, node_first, node_last, N):
    '''
    Input:
    - graph: The graph data
    - sequence_authors: A sequence of authors_a = [a_2, ..., a_{n-1}] (put 0 for a sample)
    - node_first: Initial node a_1 (put 0 for a take the first in the sample)
    - node_last: End node a_n (put 0 for a take the last in the sample)
    - N: denoting the top N authors whose data should be considered

    Output:
    - shortest_walk: The shortest walk of collaborations you need to read to get from author a_1 to author a_n
    - papers: The papers you need to cross to realize this walk.
    '''

    #Create a sub-graph from N (the top N authors with the highest degree)
    degrees_for_topN = dict(graph.degree())
    topN_auth_2 = sorted(degrees_for_topN.items(), key=lambda x:x[1], reverse=True)[:N]
    topN_auth = [i[0] for i in topN_auth_2] #taken
    Nauthors_graph = graph.subgraph(topN_auth)

    if sequence_authors==0:
        #Extract all the nodes a take a sample from this
        n = 10
        all_authors = list(Nauthors_graph.nodes)
        sequence_authors = random.sample(all_authors, n)
    
    if node_first==0:
        #Select the first...
        node_first = sequence_authors[0]
        #... and delete it from sequence authors
        sequence_authors.remove(node_first)

    if node_last==0:
        #Select the last...
        node_last = sequence_authors[-1]
        #... and delete it from sequence authors
        sequence_authors.remove(node_last)

    # final path
    shortest_walk = [].append(node_first)

    # shortest path between starting node and first node in the sequence
    path = dijkstra(Nauthors_graph, node_first, sequence_authors[0])[0]
    # add to total path (without repeating starting node)
    shortest_walk.extend(path[1:])

    # for each node in the sequence
    # find shortest path between that node and the following node in the sequence
    for p in range((len(sequence_authors)-1)):
      path = dijkstra(Nauthors_graph, sequence_authors[p], sequence_authors[p+1])[0] 
      # add path to total_path
      shortest_walk.extend(path[1:])

    # shortest path between last node in the sequence and ending node
    path = dijkstra(Nauthors_graph, sequence_authors[-1], node_last)[0]
    shortest_walk.extend(path[1:])



    return shortest_walk


    #return shortest_walk, papers