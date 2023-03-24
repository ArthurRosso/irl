import ruamel.yaml
import copy

# read the yaml file
with open('test1.yaml', 'r') as f:
    input = ruamel.yaml.round_trip_load(f)

# nodes to delete
modes = [['B', 'C'], ['A']]
count = 0

for nodes_to_delete in modes:
    data = copy.deepcopy(input)
    # remove the specified nodes
    for node in nodes_to_delete:
        del data['nodes'][node]

    for node in nodes_to_delete:
        for key in ['accessTo', 'deps']:
            for item in data['nodes'].values():
                if node in [x[0] for x in item[key]]:
                    item[key] = [x for x in item[key] if x[0] != node]

    # write the modified yaml file back to disk
    fname = "mode"+str(count)+".yaml"
    count += 1
    with open(fname, 'w') as f:
        ruamel.yaml.round_trip_dump(data, f, default_flow_style=True)
