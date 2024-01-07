import networkx as nx

def functionality_5(graph, p1, p2):

    #We need a copy
    graph_copy = graph.to_undirected()

    if nx.number_connected_components(graph_copy) > 1:
        print("The graph is not full connected!")
        return 0, [], False
    
    #Calculate the initial number of edges
    num_edges_start = graph_copy.number_of_edges()

    #Calculate betweenness centrality for each edge
    edge_betweenness = nx.edge_betweenness_centrality(graph_copy)

    # Sort edges by betweenness centrality in descending order
    sorted_edges = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse=True)

    #Remove edges until the graph has more than one connected component 
    while nx.number_connected_components(graph_copy) ==1:
        edge_to_remove = sorted_edges.pop(0)[0]
        graph_copy.remove_edge(*edge_to_remove)
    
    #Find connected components as communities
    communities = list(nx.connected_components(graph_copy))

    # Check if Paper_1 and Paper_2 belong to the same community
    same_community = any({p1,p2} <= community for community in communities)

    #Calculate the minimum number of edges removed
    num_edges_end = graph_copy.number_of_edges()

    diff = num_edges_start-num_edges_end

    # Calculate the minimum number of edges removed
    return num_edges_start-num_edges_end, diff, communities, same_community, graph_copy