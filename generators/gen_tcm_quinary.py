from sys import argv

BASE_DIR='/home/jaya-aditya/repos/hea_tcm_gen/'
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
show np(fcc_l12)
show np(bcc_b2)
show np(liquid)
show np(almo)
show np(alpha_b19)
show np(alti3_do19)
show np(alti_l10)
show np(bct_d022)
show np(c14_laves)
show np(c15_laves)
show np(c36_laves)
show np(cbcc_a12)
show np(cfc2_fenbzr)
show np(co3vv)
show np(cr3si_a15)
show np(crni2_op6)
show np(cub_a13)
show np(d019_hcp)
show np(hcp_a3)
show np(mosi2_c11b)
show np(mu_phase)
show np(ni2v)
show np(ni3ti_d024)
show np(sigma)
"""
comment = "@@%d\n"
end_str = "set-int\n"
iterations = len(com)
with open(BASE_DIR+'tcm_files/final_tc_code_quinary_'+argv[1].strip()+'.tcm','w') as f1:
    f1.write(init_str)
    for x in range(iterations):
        a,b,c,d,e = com[x]
        f1.write(comment %(x+1))
        f1.write(print_str %(argv[1].strip(),a,b,c,d))
    f1.write(end_str)
