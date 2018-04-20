import itertools
from sys import argv

BASE_DIR = '/home/jaya-aditya/repos/hea_tcm_gen/'
init_str = """set-log single_phase,,, 
set-echo
go data
sw tchea1
def-sy
Cr,Mo,Nb,Ta,V,W,Hf,Zr,Al
get
go p_3
adv
out
@&
"""
elements = ['Cr','Mo','Nb','Ta','V','W','Hf','Zr']
print_str="""s-co T=%s,n=1,p=1e5
s-co x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.0,x(%s)=0.0,x(%s)=0.0,x(Al)=None;
c-eq
show x(%s),x(%s),x(%s),x(%s),x(%s)
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
show np(mu_phase)
show np(ni2v)
show np(ni3ti_d024)
show np(sigma)
"""
comment = "@@%d\n"
end_str = "set-int\n"
counter = 0
with open(BASE_DIR+'tcm_files/tc_eq_elements_'+argv[1].strip()+'.tcm','w') as f1:
    f1.write(init_str)
    for x in itertools.combinations(elements,5):
        counter += 1
        a,b,c,d,e = x
        temp = elements[:]
        print temp
        for i in [a,b,c,d,e]:
            temp.remove(i)
        print temp
        f,g,h = temp
        f1.write(comment %(counter))
        f1.write(print_str %(argv[1].strip(),a,b,c,d,e,f,g,h,a,b,c,d,e))
    f1.write(end_str)
