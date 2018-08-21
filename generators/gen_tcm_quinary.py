from sys import argv
#argv contains the temperature at which it has to run
BASE_DIR='/home/jaya-aditya/repos/hea_tcm_gen/'
# these are the list parameters to be set before performing single point calculations
init_str = """set-log single_phase,,, 
set-echo
go data
sw tchea1
def-sy
Mo,Nb,Ta,V,W
get
go p_3
adv
out
@&
"""
# five nested loops find combinations such that a+b+c+d+e = 100
# range of a,b,c,d,e is from 5 to 35
steps = [5,10,15,20,25,30,35]
#com will contain the valid compositions of elements 
com = []
for a in steps:
    for b in steps:
        for c in steps:
            for d in steps:
                for e in steps:
                    if a + b + c + d + e == 100:
                        com.append(map(lambda x: x/100.0,[a,b,c,d,e])) # converts percentages to fractions 
#print_str contains the thermocalc commands to perform single point calculations for 
#placeholders i.e 0.2f% will be substituted by values 
print_str="""s-co T=%s,n=1,p=1e5
s-co x(Mo)=%.2f,x(Nb)=%.2f,x(Ta)=%.2f,x(V)=%.2f;
c-eq
show x(Mo),x(Nb),x(Ta),x(V),x(W)
show np(fcc_l12)
show np(bcc_b2)
"""
#show np(fcc_l12) and np(bcc_b2) prints amount of bcc and fcc phase in thermocalc
#comment in thermocalc macro to denote the iteration being run, its optional and not essential to run the code
comment = "@@%d\n"
end_str = "set-int\n"
iterations = len(com)
# writing macro, for example if 400 is passed as temperature, the output file will be stored as
# final_tc_code_400.tcm in tcm_files folder
with open(BASE_DIR+'tcm_files/final_tc_code_quinary_'+argv[1].strip()+'.tcm','w') as f1:
    f1.write(init_str)
    for x in range(iterations):
        a,b,c,d,e = com[x]
        f1.write(comment %(x+1))
        f1.write(print_str %(argv[1].strip(),a,b,c,d)) #substituting valid combinations 
    f1.write(end_str)
