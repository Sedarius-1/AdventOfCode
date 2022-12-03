from string import ascii_lowercase, ascii_uppercase
import re


def find_duplicates(file_name):
    with open(file_name) as f:
        content = f.read()
        rucksacks_list = [x.strip().split('\n') for x in re.findall('((?:[^\n]+\n?){1,3})', content)]
        items_list = []
        values = {}
        value_low = 1
        value_up = 27
        letters_low = []
        letters_up = []
        final_value = 0
        ind = 1
        flag = True
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
            for p in i[0]:
                for q in i[1]:
                    for r in i[2]:
                        if p == q == r:
                            item_to_add = p
                        if flag:
                            pass
            items_list.append(item_to_add)
        for z in items_list:
            value = values[z]
            final_value += value
        return final_value


print(find_duplicates('input.txt'))
