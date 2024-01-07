import random
import networkx as nx

def functionality_4(graph, start, target, N):

    #Subgraph of first N authors
    degrees_for_topN = dict(graph.degree())
    topN_auth_2 = sorted(degrees_for_topN.items(), key=lambda x:x[1], reverse=True)[:N]
    topN_auth = [i[0] for i in topN_auth_2]
    Nauthors_graph = graph.subgraph(topN_auth)

    #We take two random author... if 'start' and 'target' are = 0
    if start==0 and target==0:
        n=2
        subsample = random.sample(list(Nauthors_graph.nodes), n)
        start = subsample[0]
        target = subsample[1]

    #Initialite lists to save neighbors
    neigh_start = []
    neigh_target = []

    #We copy the graph
    graph_copy = Nauthors_graph.copy()

    #Till there are just two nodes...
    while len(graph_copy) > 2:

        #Random choice between start and target
        choice1 = random.choice([start, target])
        #Other node to use in the contraction is in the neighborhood of v...
        choice2 = random.choice(list(graph_copy.neighbors(choice1)))

        #...if 'choice2' is equal to 'start' or 'target' >>> continue
        if choice2 == start or choice2 == target:
            continue

        graph_copy = nx.contracted_edge(graph_copy,(choice1, choice2))

        #...If we are contracting with respect to the start node we will add 'choice2' to 'neigh_start'...
        if choice1 == start:
            neigh_start.append(choice2)
        #... Otherwise it'll be add to 'neigh_target'
        else:
            neigh_target.append(choice2)

    #Create subgraph from original graph and from the arrays containing the neighbors
    start_subgraph = nx.subgraph(Nauthors_graph, neigh_start + [start])
    target_subgraph = nx.subgraph(Nauthors_graph, neigh_target + [target])
    removed_edges = len(Nauthors_graph.edges) - len(start_subgraph.edges) - len (target_subgraph.edges) 
    
    return removed_edges