def get_metadata_sum(data, index):
    children = data[index]
    metadatas = data[index+1]
    index += 2
    metadata_sum = 0
    for _ in range(children):
        mdata_sum, index = get_metadata_sum(data, index)
        metadata_sum += mdata_sum
    for _ in range(metadatas):
        metadata_sum += data[index]
        index += 1
    
    return (metadata_sum, index)

data = []
with open('memory-maneuver-input.txt', 'r') as file:
    data = [int(x) for x in file.readline().split(' ')]

print("Metadata sum: {}".format(get_metadata_sum(data, 0)[0]))