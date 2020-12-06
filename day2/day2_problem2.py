array = []

with open('input_day2.txt') as f:
    for line in f:
        pos1 = int(line.split('-')[0])
        pos2 = int(line.split(' ')[0].split('-')[1])
        letter = line.split(':')[0].split(' ')[1]
        pw = line.split(' ')[2].split('\n')[0]
        array += [(pos1, pos2, letter, pw)]

num_valid = 0

for pw_tup in array:
    pos1, pos2, letter, pw = pw_tup
    in_pos1 = pw[pos1-1] == letter
    in_pos2 = pw[pos2-1] == letter
    if (in_pos1 and not in_pos2) or (not in_pos1 and in_pos2):
        num_valid += 1

print('Number of valid passwords: {}.'.format(num_valid))
