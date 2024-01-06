import random

# Dijkstra's algorithm
def NextNode(dist, visited, nodes):
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
    for i in nodes:
        if (not visited[nodes.index(i)]) and (dist[nodes.index(i)] < min):
            next_node = i
            min = dist[nodes.index(i)]
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

    '''
    list_nodes_adjacent = []
    for j in range(len(graph)):
        if graph[node][j] != float('inf'):
            list_nodes_adjacent.append([j, graph[node][j]])
    return list_nodes_adjacent
    '''

    list_nodes_adjacent = []

    auth = [i for i in graph[node]]
    weight_auth = [graph[node][i]['weight'] for i in auth]
    nod_adj = list(zip(auth, weight_auth))

    for j in range(len(nod_adj)):
        if weight_auth[j] != float('inf'):
            list_nodes_adjacent.append(nod_adj[j])
    return list_nodes_adjacent

def Dijkstra(graph, node_start, node_plusone):
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
    nodes = []
    ###---
    predecessor = []  # Inizializza tutti i predecessori a -1
    ###---

    for i in range(n):
        dist.append(float('inf'))
        visited.append(False)
        nodes.append(list(graph.nodes)[i])
        ###---
        predecessor.append([])
        ###---

    dist[nodes.index(node_start)] = 0

    for i in range(n - 1):
        next = NextNode(dist, visited, nodes)
        visited[nodes.index(next)] = True
        V = getAdjacents(graph, next)
        for [z, w] in V:
            d = dist[nodes.index(next)] + w
            if dist[nodes.index(z)] > d:
                dist[nodes.index(z)] = d
                predecessor[nodes.index(z)].append(next)
    
    return dist[nodes.index(node_plusone)], node_plusone
    

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
    topN_auth = [i[0] for i in topN_auth_2]
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
        print('The first node is: %s' %node_first)

    if node_last==0:
        #Select the last...
        node_last = sequence_authors[-1]
        #... and delete it from sequence authors
        sequence_authors.remove(node_last)
        print('The last node is: %s' %node_last)
        print('The authors sequence is: %ls' %sequence_authors)

    # final path
    shortest_walk = []

    #First node have 0 distance from itself
    shortest_walk.append((0,node_first))

    # shortest path between starting node and first node in the sequence
    dist1, predecessor1 = Dijkstra(Nauthors_graph, node_first, sequence_authors[0])
    # add to total path (without repeating starting node)
    shortest_walk.append((dist1, predecessor1))

    # for each node in the sequence
    # find shortest path between that node and the following node in the sequence
    for p in range((len(sequence_authors)-1)):
      dist_s, predecessor_s = Dijkstra(Nauthors_graph, sequence_authors[p], sequence_authors[p+1])
      # add path to total_path
      shortest_walk.append((dist_s, predecessor_s))

    # shortest path between last node in the sequence and ending node
    dist_last, predecessor_last = Dijkstra(Nauthors_graph, sequence_authors[-1], node_last)
    shortest_walk.append((dist_last, predecessor_last))

    weight = [i[0] for i in shortest_walk]

    if float('inf') in weight:
        return 'It is not possible to calculate a path'
    else:
        return shortest_walk