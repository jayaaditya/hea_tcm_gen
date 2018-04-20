import itertools
import json

delta_h = {}
elements = ['Cr', 'Hf','Mo','Nb', 'Ta', 'V', 'W', 'Zr']
for x in elements:
    delta_h[x] = {}
for x in range(8):
    for i in range(x+1,8):
        print elements[x], elements[i]
        delta_h[elements[x]][elements[i]] = int(raw_input())

with open('delta_h.json', 'w') as f:
    json_str = json.dumps(delta_h)
    f.write(json_str)

"""
final_set = []
combinations = itertools.combinations(elements, 5)
for x in combinations:
    temp = []
    for i in x:
        temp.append(i)
    final_set.append(temp)
print final_set
"""
