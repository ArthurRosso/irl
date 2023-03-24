import yaml

def all_paths(dag):
    # Find the suitable source and destination vertices
    sources = [v for v in dag if not any(v in edges for edges in dag.values())]
    destinations = [v for v in dag if not dag[v]]
    if len(sources) != 1 or len(destinations) != 1:
        raise ValueError("DAG must have exactly one source and one destination vertex.")
    s, d = sources[0], destinations[0]

    # Find all paths from the source to the destination
    def find_paths_helper(curr, path, paths):
        if curr == d:
            paths.append(path + [curr])
            return
        for neighbor in dag[curr]:
            find_paths_helper(neighbor, path + [curr], paths)

    paths = []
    find_paths_helper(s, [], paths)
    return paths

dag = {
    'f0': ['f1', 'C'],
    'f1': ['A', 'B'],
    'A': ['j0'],
    'B': ['j0'],
    'j0': ['j1'],
    'C': ['j1'],
    'j1': []
}


# with open('input_example.yaml') as file:
#     data = yaml.safe_load(file) # Load the YAML file safely

# # Retrieve the 'nodes' key from the dictionary
# nodes = [node for node in data['nodes'].values()]

# # Initialize the DAG dictionary
# dag = {node['traceName']: [] for node in nodes}

# # Extract the edges from the YAML data
# for node in nodes:
#     for dest_node, _ in node['accessTo']:
#         dag[node['traceName']] += [dest_node]

# # Print the resulting DAG
# print(dag)

paths = all_paths(dag)
print("All paths in the DAG:")
for path in paths:
    print(path)