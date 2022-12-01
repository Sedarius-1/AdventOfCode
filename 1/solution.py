def read_file(txtfile):
    with open(txtfile) as f:
        elves_list = []
        content = f.read()
        calories_list = content.split('\n')
        yemp_string = []
        sums_list = []
        calories = 0
        max_1 = 0
        max_2 = 0
        max_3 = 0
        for i in calories_list:
            # print(i+'\n')
            if len(i) > 0:
                yemp_string.append(i)
            else:
                elves_list.append(yemp_string)
                yemp_string = []
        for i in elves_list:
            # print(i)
            for p in range(0, len(i)):
                calories += int(i[p])
            sums_list.append(calories)
            calories = 0
        for i in sums_list:
            if i > max_3:
                max_3 = i
            if max_3 > max_2:
                max_3 = max_2
                max_2 = i
                if max_2 > max_1:
                    max_2 = max_1
                    max_1 = i

    return max_1 + max_2 + max_3


print(read_file('aoc1.txt'))
