import networkx as nx

def functionality_5(graph, paper1, paper2, N):
    
    #Subgraph of first N authors
    degrees = dict(graph.degree())
    N_authors = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:N]
    N_authors_id = [el[0] for el in N_authors]
    subgraph = graph.subgraph(N_authors_id)

    #From subgraph extract edge betweenness centrality
    G_dict = nx.edge_betweenness_centrality(subgraph)
    edge = ()

    #Extract the edge lenght with the highest edge betweenness centrality score
    for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse=True):
        edge = key
        break
    number_of_edges = len(edge)

    # Find the number of connected components
    conn_comp = nx.connected_components(subgraph)
    conn_comp_count = nx.number_connected_components(subgraph)

    # Continue removing edges until the graph is divided into multiple connected components
    while conn_comp_count == 1:

        #From subgraph.copy() extract edge betweenness centrality
        G_dict = nx.edge_betweenness_centrality(subgraph.copy())
        edge = ()

        # Extract the edge with the highest edge betweenness centrality score
        for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse=True):
            edge = key
            break

        graph.remove_edge(edge[0], edge[1])
        conn_comp = nx.connected_components(subgraph.copy())
        conn_comp_count = nx.number_connected_components(subgraph.copy())

    #Find the nodes forming the communities
    communities = []

    for i in conn_comp:
        communities.append(list(i))

    for community in communities:
        if paper1 in community and paper2 in community:
            same_c = True
            break
        else:
            same_c = False
    
    return number_of_edges, communities, same_c
