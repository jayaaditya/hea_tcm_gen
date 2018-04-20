import csv
import re

BASE_DIR = '/home/jaya-aditya/repos/hea_tcm_gen/'
f1 = open(BASE_DIR+'results/eq_calc_quinary.dat','r')
file_dump = map(lambda x: x.strip('\n'),f1.readlines())
f1.close()
heading = [
        'Element1',
        'Element2',
        'Element3',
        'Element4',
        'Element5'
        ]
final_csv_out = []
print final_csv_out
flag = True
for x in range(len(file_dump)/28):
    index = x*28
    temp_list = []
    for out_str in file_dump[index : index + 5]:
        element = out_str.split('(')[1].split(')')[0]
        temp_list.append(element)
    for out_str in file_dump[index + 5 : index + 28]:
        if flag:
            heading.append(out_str.split('(')[1].split(')')[0])
        temp_list.append(str(eval(out_str.split('=')[1])))
    flag = False
    final_csv_out.append(temp_list)
with open(BASE_DIR+'results/eq_results_com.csv', 'w') as f2:
    csv_writer = csv.writer(f2, dialect = 'excel')
    csv_writer.writerow(heading)
    csv_writer.writerows(final_csv_out)
