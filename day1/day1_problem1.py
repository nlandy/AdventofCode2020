from collections import defaultdict

with open('input_day1.txt') as f:
    array = [int(line) for line in f]

target = 2020

pair_dict = defaultdict(lambda : -1)
pair = []

for i in range(len(array)):
    if(pair_dict[array[i]] != -1):
        pair = [array[pair_dict[array[i]]], array[i]]
        break
    else:
        pair_dict[target - array[i]] = i

code = pair[0] * pair[1]

print('The code is {}.'.format(code))
