init_str = """set-log single_phase,,, 
set-echo
go data
sw tchea3
def-sy
Co,Cu,Ti,Ni,Fe
get
go p_3
adv
out
@&
"""

print_str="""s-co T=%d,n=1,p=1e5
s-co x(Co)=0.2,x(Cu)=0.2,x(Ti)=0.2,x(Ni)=0.2,x(Fe)=0.2;
c-eq
show x(Co),x(Cu),x(Ti),x(Ni),x(Fe)
show np(c14_laves)
show np(c15_laves)
show np(hcp_zn)
show np(ni3ti_d024)
show np(fcc_l12)
show np(liquid)
"""
with open('macro_test.tcm','w') as f:
    f.write(init_str)
    for x in range(500,501):
        f.write(print_str % x)

