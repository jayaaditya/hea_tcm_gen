init_str = """set-log single_phase,,, 
set-echo
go data
sw tchea1
def-sy
Cr,Mo,Nb,Ta,V,W
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
                    for f in steps:
                        if a + b + c + d + e + f == 100:
                            com.append(map(lambda x: x/100.0,[a,b,c,d,e,f]))
print_str="""s-co T=1000,n=1,p=1e5
s-co x(Cr)=%.2f,x(Mo)=%.2f,x(Nb)=%.2f,x(Ta)=%.2f,x(V)=%.2f;
c-eq
show x(Cr),x(Mo),x(Nb),x(Ta),x(V),x(W)
show np(fcc_a1)
show np(fcc_l12)
show np(bcc_a2)
show np(bcc_b2)
"""
comment = "@@%d\n"
end_str = "set-int\n"
iterations = len(com)
with open('final_tc_code.TCM','w') as f1:
    f1.write(init_str)
    for x in range(iterations):
        a,b,c,d,e,f = com[x]
        f1.write(comment %(x+1))
        f1.write(print_str %(a,b,c,d,e))
    f1.write(end_str)
