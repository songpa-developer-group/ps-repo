from collections import defaultdict


a = [100,4,200,1,3,2]

a = set(input)
parent_map = defaultdict(int)
for i in a:
    parent_map[i] = parent_map[i-1]+1

print(max(parent_map.values()))