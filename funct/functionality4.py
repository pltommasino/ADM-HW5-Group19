import random
import networkx as nx

def functionality_4(graph, start, target):
    #auxiliar lists that allows us to save the neighbor for the starter node and for the target node
    start_nb = []
    target_nb = []
    #need a copy because later 1 need the original graph in order to bulld the subgraph and computing the numb
    graph_copy = graph.copy()
    while len(graph_copy) > 2: # iterate till there are just 2 nodes
        # pick randomly between the start and the target
        v = random.choice([start, target])
        # the other node to use in the contraction is in the neighborhood of v but cant be neither the start or t.
        w = random.choice(list(graph_copy.neighbors(v)))
        if w == start or w == target:
            continue
        graph_copy = nx.contracted_edge(graph_copy,(v, w))
        #if we are contracting with respect to the start node we will add w to start_nb, otherwise it'11 be adde
        if v == start:
            start_nb.append(w)
        else:
            target_nb.append(w)
    #create the subgraph starting from the original graph and from the arrays containing the neighbors
    subgraph_start = nx.subgraph(graph, start_nb + [start])
    subgraph_target = nx.subgraph(graph, target_nb + [target])
    removed_edges = len(graph.edges) - len(subgraph_start.edges) - len (subgraph_target.edges) 
    
    return removed_edges