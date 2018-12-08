def get_node_value(data, index):
    children = data[index]
    metadatas = data[index+1]
    index += 2
    if children == 0:
        metadata_sum = 0
        for _ in range(metadatas):
            metadata_sum += data[index]
            index += 1
        return (metadata_sum, index)
    else:
        children_values = []
        for _ in range(children):
            value, index = get_node_value(data, index)
            children_values.append(value)
        
        node_value = 0
        for _ in range(metadatas):
            m = data[index] - 1
            if m >= 0 and m < len(children_values):
                node_value += children_values[m]
            index += 1
        
        return (node_value, index)

data = []
with open('memory-maneuver-input.txt', 'r') as file:
    data = [int(x) for x in file.readline().split(' ')]

print("Root value: {}".format(get_node_value(data, 0)[0]))