from string import ascii_lowercase, ascii_uppercase


def find_duplicates(file_name):
    with open(file_name) as f:
        content = f.read()
        rucksacks_list = content.split('\n')
        temp_list = []
        half_rucksacks_list = []
        items_list = []
        values = {}
        flag = True
        value_low = 1
        value_up = 27
        letters_low = []
        letters_up = []
        final_value = 0
        ind = 1
        for i in ascii_lowercase:
            letters_low.append(i)
        for i in ascii_uppercase:
            letters_up.append(i)
        for i in range(0, 26):
            values.update({letters_low[i]: value_low})
            values.update({letters_up[i]: value_up})
            value_low += 1
            value_up += 1
        for i in rucksacks_list:
            index = int(len(i) / 2)
            temp_string = i[0:index]
            temp_list.append(temp_string)
            index = int(len(i) / 2)
            temp_string = i[index:]
            temp_list.append(temp_string)
            half_rucksacks_list.append(temp_list)
            for r in temp_list[0]:
                for p in temp_list[1]:
                    if p == r:
                        for q in items_list:
                            if q == p and len(items_list) == ind:
                                flag = False
                        if flag:
                            items_list.append(p)
            temp_list = []
            ind += 1
            flag = True
        for z in items_list:
            value = values[z]
            final_value += value
        print(len(items_list))
        return final_value


print(find_duplicates('input.txt'))