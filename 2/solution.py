def calculate_score(file_name):
    with open(file_name) as f:
        content = f.read()
        matches_list = content.split('\n')
        score = 0
        temp_score = 0
        for i in matches_list:
            if i[-1] == 'X':
                temp_score += 1
                if i[0] == 'A':
                    temp_score += 3
                if i[0] == 'B':
                    temp_score += 0
                if i[0] == 'C':
                    temp_score += 6
            if i[-1] == 'Y':
                temp_score += 2
                if i[0] == 'A':
                    temp_score += 6
                if i[0] == 'B':
                    temp_score += 3
                if i[0] == 'C':
                    temp_score += 0
            if i[-1] == 'Z':
                temp_score += 3
                if i[0] == 'A':
                    temp_score += 0
                if i[0] == 'B':
                    temp_score += 6
                if i[0] == 'C':
                    temp_score += 3
            score += temp_score
            temp_score = 0
    return score


print(calculate_score('aoc2.txt'))
