import csv

f1 = open('./final_HEA_results.dat','r')
file_dump = map(lambda x: x.strip('\n'),f1.readlines())
f1.close()
heading = ["Cr" , "Mo", "Nb", "Ta", "V", "W", "FCC_L12", "BCC_B2"]
final_csv_out = []
print final_csv_out
for x in range(len(file_dump)/8):
    index = x*8
    temp_list = []
    for out_str in file_dump[index : index + 8]:
        temp_list.append(str(eval(out_str.split('=')[1])))
    final_csv_out.append(temp_list)
with open('results_raw.csv', 'wb') as f2:
    csv_writer = csv.writer(f2, dialect = 'excel')
    csv_writer.writerow(heading)
    csv_writer.writerows(final_csv_out)
