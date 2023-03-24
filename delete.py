import ruamel.yaml
import copy

# read the yaml file
with open('test1.yaml', 'r') as f:
    input = ruamel.yaml.round_trip_load(f)

# nodes to delete
modes = [['B', 'C'], ['A']]
count = 0

for nodes_to_delete in modes:
    # copy the data to don't loose the information of the original file
    data = copy.deepcopy(input)

    # remove the specified nodes
    for node in nodes_to_delete:
        del data['nodes'][node]

    # loops over each node in the nodes_to_delete list
    for node in nodes_to_delete:
        # loops over the keys 'accessTo' and 'deps'
        for key in ['accessTo', 'deps']:
            # loops over each value in the 'nodes' dictionary in the data variable
            for item in data['nodes'].values():
                # checks if the node we are currently iterating over is in the first element of any of the lists in the item[key] list
                if node in [x[0] for x in item[key]]:
                    # if the condition in the previous line is true, this line removes the entire list that contains the node from the item[key] list
                    item[key] = [x for x in item[key] if x[0] != node]

    # write the modified yaml file to a new yaml file
    fname = "mode"+str(count)+".yaml"
    count += 1
    with open(fname, 'w') as f:
        ruamel.yaml.round_trip_dump(data, f, default_flow_style=True)
