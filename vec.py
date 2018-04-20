import csv
import itertools 

elements = ['Cr', 'Hf','Mo','Nb', 'Ta', 'V', 'W', 'Zr']
vec = {
        'Cr': 6,
        'Hf':4,
        'Mo':6,
        'Nb':5,
        'Ta':5,
        'V':5,
        'W':6,
        'Zr':4
        }

comb_list = []
for x in itertools.combinations(elements,5):
    temp = []
    for i in x:
        temp.append(i)
    comb_list.append(temp)
f = open('vec.csv','w')
csv_writer = csv.writer(f)
for x in comb_list:
    vec_val = 0
    for i in x:
        vec_val += 0.2*vec[i]
    csv_writer.writerow(x + [vec_val])
f.close()
