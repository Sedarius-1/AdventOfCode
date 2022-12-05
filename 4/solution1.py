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

        pairs_amount = 0
        for i in p_m:
            if i[0][0] <= i[1][0]:
                if i[0][1] >= i[1][1]:
                    pairs_amount += 1
                    continue
            if i[0][0] >= i[1][0]:
                if i[0][1] <= i[1][1]:
                    pairs_amount += 1
                    continue
    return pairs_amount


print(calculate_overlaps('input.txt'))
