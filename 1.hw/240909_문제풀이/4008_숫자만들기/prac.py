import itertools

opers = ['+', '+', '-', '/']
nums = [3, 5, 3, 7, 9]

permu_operators = list(set(list(itertools.permutations(opers))))
print(permu_operators)

permu_nums = list(set(list(itertools.permutations(nums))))
print(permu_nums)



mn, mx = float('int'), float('-int')

for permu_o in permu_operators:
    for permu_n in permu_nums:
