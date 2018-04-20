from sys import argv

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
steps = [5,10,15,20,25,30,35]
com = []
for a in steps:
    for b in steps:
        for c in steps:
            for d in steps:
                for e in steps:
                    if a + b + c + d + e == 100:
                        com.append(map(lambda x: x/100.0,[a,b,c,d,e]))
print_str="""s-co T=%s,n=1,p=1e5
s-co x(Mo)=%.2f,x(Nb)=%.2f,x(Ta)=%.2f,x(V)=%.2f;
c-eq
show x(Mo),x(Nb),x(Ta),x(V),x(W)
show np(fcc_a1)
show np(fcc_l12)
show np(bcc_a2)
show np(bcc_b2)
"""
comment = "@@%d\n"
end_str = "set-int\n"
iterations = len(com)
with open('../tcm_files/final_tc_code_quinary'+argv[1].strip()+'.tcm','w') as f1:
    f1.write(init_str)
    for x in range(iterations):
        a,b,c,d,e = com[x]
        f1.write(comment %(x+1))
        f1.write(print_str %(argv[1].strip(),a,b,c,d))
    f1.write(end_str)
