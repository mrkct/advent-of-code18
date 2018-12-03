def is_similar(string1, string2):
    diff_chars = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff_chars = diff_chars + 1
            if diff_chars > 1:
                return False
    return True

with open('inventory-managment-input.txt', 'r') as file:
    similars = []
    for line in file:
        for sim_list in similars:
            if is_similar(line, sim_list[0]):
                sim_list.append(line)
        else:
            similars.append([line])
    
    for sim_list in similars:
        if len(sim_list) > 1:
            string1 = sim_list[0]
            string2 = sim_list[1]
            for i in range(len(string1)):
                if string1[i] == string2[i]:
                    print(string1[i], end='')
