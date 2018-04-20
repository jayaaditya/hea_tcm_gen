import csv
from sys import argv

BASE_DIR = '/home/jaya-aditya/repos/hea_tcm_gen/'
f1 = open(BASE_DIR+'results/quinary_non_eq_600.dat','r')
file_dump = map(lambda x: x.strip('\n'),f1.readlines())
f1.close()
heading = ["Mo", "Nb", "Ta", "V", "W", "FCC_L12", "BCC_B2"]
final_csv_out = []
print final_csv_out
for x in range(len(file_dump)/7):
    index = x*7
    temp_list = []
    for out_str in file_dump[index : index + 7]:
        temp_list.append(str(eval(out_str.split('=')[1])))
    final_csv_out.append(temp_list)
final_csv_out.sort(key = lambda x: float(x[6]), reverse = True)
with open(BASE_DIR+'results/quinary_non_eq_results_600.csv', 'w') as f2:
    csv_writer = csv.writer(f2, dialect = 'excel')
    csv_writer.writerow(heading)
    csv_writer.writerows(final_csv_out)
