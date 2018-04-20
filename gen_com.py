import itertools

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
print_str="""s-co T=1000,n=1,p=1e5
s-co x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.2,x(%s)=0.0,x(%s)=0.0,x(%s)=0.0,x(Al)=None;
c-eq
show x(%s),x(%s),x(%s),x(%s),x(%s)
show np(fcc_a1)
show np(fcc_l12)
show np(bcc_a2)
show np(bcc_b2)
"""
comment = "@@%d\n"
end_str = "set-int\n"
counter = 0
with open('tc_eq_elements.TCM','w') as f1:
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
        f1.write(print_str %(a,b,c,d,e,f,g,h,a,b,c,d,e))
    f1.write(end_str)
