array = []

with open('input_day2.txt') as f:
    for line in f:
        min = int(line.split('-')[0])
        max = int(line.split(' ')[0].split('-')[1])
        letter = line.split(':')[0].split(' ')[1]
        pw = line.split(' ')[2].split('\n')[0]
        array += [(min, max, letter, pw)]

num_valid = 0

for pw_tup in array:
    min, max, letter, pw = pw_tup
    if min <= pw.count(letter) <= max:
        num_valid += 1

print('Number of valid passwords: {}.'.format(num_valid))
