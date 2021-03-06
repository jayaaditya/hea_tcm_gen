import itertools
import json
import csv

radius = {
        'Cr':128,
        'Hf':225,
        'Nb':146,
        'Ta':146,
        'Mo':139,
        'W':139,
        'V':143,
        'Zr':230
        }

def calc_delta_h(combinations, delta_h):
    total_h = []
    for x in combinations:
        ans = 0
        for i in itertools.combinations(x,2):
            a,b = i
            ans += 4*delta_h[a][b]*0.2*0.2
        total_h.append(ans)
    return total_h

def calc_delta(combinations, radius):
    delta_vals = []
    for x in combinations:
        avg_radius = sum(map(lambda a: 0.2*radius[a], x))
        delta = 0
        for i in x:
            delta += 0.2*(1 - radius[i]/avg_radius)**2
        delta_vals.append(100*(delta**0.5))
    return delta_vals

delta_h = {}
with open('./delta_h.json', 'r') as f:
    delta_h = json.load(f)

elements = ['Cr', 'Hf','Mo','Nb', 'Ta', 'V', 'W', 'Zr']
final_set = []
for x in itertools.combinations(elements, 5):
    temp = []
    for i in x:
        temp.append(i)
    final_set.append(temp)

delta_vals = calc_delta(final_set, radius)
h_vals = calc_delta_h(final_set, delta_h)
hvals = map(str, h_vals)
delta_vals = map(str, delta_vals)
output = []
for x in range(len(final_set)):
    output.append(final_set[x] + [hvals[x]] + [delta_vals[x]])
required_output = []
for x in output:
    if float(x[5]) >= -15 and float(x[5]) <= 5 and float(x[6]) <= 6.6:
        required_output.append(x)
with open('min_delta_out.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(required_output)
with open('delta_h.csv','w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(output)
