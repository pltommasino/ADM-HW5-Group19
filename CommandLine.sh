#!/bin/bash

# Define the citation graph file
citation_graph_file="citation_graph.txt"

# Question 1: Is there any node that acts as an important "connector" between the different parts of the graph?

# Step 1: Extract the nodes from the second column and count 
node_count=$(awk '{print $2}' "$citation_graph_file" | sort | uniq -c | sort -nr)

# Step 2: Extract the node with the highest degree from the node_count result
read node_highest degree_highest <<< "$(echo "$node_count" | awk 'NR==1 {print $2, $1}')"

# Step 3: Print the result
cat <<EOF
The most important connector node:
Node: $node_highest, Degree: $degree_highest
EOF




# Question 2: How does the degree of citation vary among the graph nodes?

# Step 1: Extract the nodes from the second column and calculate the range of citation degrees
range=$(awk '{print $2}' "$citation_graph_file" | sort -n | uniq -c | awk 'NR==1{min=$1; max=$1} {if($1<min) min=$1; if($1>max) max=$1} END{print min, max}')

# Step 2: Print the result
echo -e "\nRange of Citation Degrees:"
echo "$range"
echo ""






# Question 3: What is the average length of the shortest path among nodes?

# Step 1: Extract unique edges from the citation graph file
unique_edges=$(awk '{print $1, $2}' "$citation_graph_file" | sort -u)

# Step 2: Use Python to calculate average shortest path length for the largest strongly connected component
average_length=$(echo "$unique_edges" | python3 -c "
import networkx as nx
import sys

# Step 3: Read edges from stdin and create a directed graph
G = nx.DiGraph()
for line in sys.stdin:
    # Parse source and target nodes from the input lines
    source, target = map(int, line.split())
    G.add_edge(source, target)

# Step 4: Find the largest strongly connected component in the graph
largest = max(nx.strongly_connected_components(G), key=len)

# Step 5: Create a subgraph with only the largest strongly connected component
largest_comp_g = G.subgraph(largest)

# Step 6: Calculate average shortest path length for the largest component
average_length = nx.average_shortest_path_length(largest_comp_g)
# Print the result with two decimal places
print('{:.2f}'.format(average_length))
")

# Step 7: Check if the average_length is not empty (i.e., calculation successful)
if [ -n "$average_length" ]; then
    # Step 8: Print the calculated average shortest path length
    echo "The Average Shortest Path Length: $average_length"
else
    # Step 9: Handle the case where the calculation failed
    echo "Error: Unable to calculate the average shortest path length."
fi