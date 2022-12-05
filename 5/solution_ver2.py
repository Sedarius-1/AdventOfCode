import collections


def move_crates(file_name):
    crates = [collections.deque(['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']),
              collections.deque(['M', 'Q', 'H']),
              collections.deque(['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']),
              collections.deque(['Z', 'T', 'F', 'Q', 'M', 'W', 'G']),
              collections.deque(['M', 'T', 'H', 'P']),
              collections.deque(['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']),
              collections.deque(['M', 'N', 'B', 'F', 'V', 'R']),
              collections.deque(['P', 'L', 'H', 'M', 'R', 'G', 'S']),
              collections.deque(['P', 'D', 'B', 'C', 'N'])]
    top_crates = []
    with open(file_name) as f:
        instructions = []
        instructions_numbers_groupped = []
        for line in f.readlines():
            instructions.append(line.strip().split(" "))
        for i in instructions:
            instructions_numbers_groupped.append([int(i[1]), int(i[3]) - 1, int(i[5]) - 1])
        for i in instructions_numbers_groupped:

            for p in range(0, i[0]):

                crates[i[2]].append(crates[i[1]][-1])
                crates[i[1]].pop()
        for crate in crates:
            top_crates.append(crate[-1])
    return ''.join(top_crates)


print(move_crates('input.txt'))
