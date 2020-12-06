from collections import defaultdict

with open('input_day1.txt') as f:
    array = [int(line) for line in f]

def twosum(target, array):
    pair_dict = defaultdict(lambda : -1)
    pair = []
    for i in range(len(array)):
        if(pair_dict[array[i]] != -1):
            pair = [array[pair_dict[array[i]]], array[i]]
            break
        else:
            pair_dict[target - array[i]] = i
    return pair

three_sum_target = 2020

for i in range(len(array)):
    two_sum_target = 2020 - array[i]
    pair = twosum(two_sum_target, array[:i] + array[i+1:])
    if pair:
        trio = pair + [array[i]]
        break

code = trio[0] * trio[1] * trio[2]
print('The code is {}.'.format(code))
