import yaml

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for neighbor in graph[node]['accessTo']:
        neighbor_node = neighbor[0]
        if neighbor_node not in visited:
            dfs(graph, neighbor_node, visited)


with open('mia_result.yaml') as file:
    data = yaml.safe_load(file) # Load the YAML file safely

nodes = data['nodes'] # Retrieve the 'nodes' key from the dictionary

# Find the root node
# you can find it by iterating over all the nodes in the JSON file and looking for the one that has no dependencies (i.e., the root node)
root_node = None
for node_name, node_data in nodes.items():
    if not node_data['deps']:
        root_node = node_name
        break

dfs(nodes, root_node)