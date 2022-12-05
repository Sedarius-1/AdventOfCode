def calculate_overlaps(file_name):
    with open(file_name) as f:
        p_m = []
        pair = []
        for line in f.readlines():
            member = line.strip().split(',')
            pair.append((int(member[0].split("-")[0]), int(member[0].split("-")[1])))
            pair.append((int(member[1].split("-")[0]), int(member[1].split("-")[1])))
            p_m.append(pair)
            pair = []
        overlaps_flag = False
        overlaps = 0
        for i in p_m:
            pair1_min = i[0][0]
            pair1_max = i[0][1]
            pair2_min = i[1][0]
            pair2_max = i[1][1]
            for value1 in range(pair1_min, pair1_max+1):
                for value2 in range(pair2_min, pair2_max+1):
                    if value1 == value2:
                        overlaps_flag = True
            if overlaps_flag:
                overlaps += 1
            overlaps_flag = False

    return overlaps


print(calculate_overlaps('input.txt'))
