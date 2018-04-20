import ternary
import csv
from matplotlib import pyplot

scale = 20
data = {}
with open('results_new.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for x in csv_reader:
        try:
            Cr_V = float(x[0]) + float(x[4])
            Mo_Nb = float(x[1]) + float(x[2])
            Ta_W = float(x[3]) + float(x[5])
            data[(Cr_V*scale,Mo_Nb*scale,Ta_W*scale)] = float(x[7])*100
            print Cr_V, Mo_Nb, Ta_W
        except:
            print "blah"
            pass
figure, tax = ternary.figure(scale=scale)
tax.gridlines(color="black", multiple=scale/20)
fontsize = 14
tax.heatmap(data, style = 'h', cmap = None, scientific = True)
tax.set_title("Pseudo Ternary Diagram", fontsize=20)
tax.left_axis_label("Mo + Nb", fontsize=fontsize)
tax.right_axis_label("Ta + W", fontsize=fontsize)
tax.bottom_axis_label("Cr + V", fontsize=fontsize)
tax.boundary()
tax.ticks(multiple = scale/20)
tax.show()
