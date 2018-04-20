import csv
import re

f1 = open('./eq_calc_quinary.dat','r')
file_dump = map(lambda x: x.strip('\n'),f1.readlines())
f1.close()
final_csv_out = []
print final_csv_out
for x in range(len(file_dump)/7):
    index = x*7
    temp_list = []
    for out_str in file_dump[index : index + 5]:
        element = out_str.split('(')[1].split(')')[0]
        temp_list.append(element)
    for out_str in file_dump[index + 5 : index + 7]:
        temp_list.append(str(eval(out_str.split('=')[1])))
    final_csv_out.append(temp_list)
with open('eq_results_com.csv', 'w') as f2:
    csv_writer = csv.writer(f2, dialect = 'excel')
    csv_writer.writerows(final_csv_out)
