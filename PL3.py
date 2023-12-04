from gurobipy import *
m= Model(name = "PL3")
x1=m.addVar (name="x1")
x2=m.addVar (name="x2")
x3=m.addVar (name="x3")
x4=m.addVar (name="x4")
x5=m.addVar (name="x5")
x6=m.addVar (name="x6")
x7=m.addVar (name="x7")
obj_func=x1+x2+x3+x4+x5+x6+x7
m.setObjective(obj_func, GRB.MINIMIZE)
C1=m.addConstr(x1+x4+x5+x6+x7 >=17 )#replace 17 with nb_emp donné in all constraints
C2=m.addConstr(x1+x2+x5+x6+x7 >=13 )
C3=m.addConstr(x1+x2+x3+x6+x7 >=15 )
C4=m.addConstr(x1+x2+x3+x4+x7 >=19 )
C5=m.addConstr(x1+x2+x3+x4+x5 >=14 )
C6=m.addConstr(x2+x3+x4+x5+x6 >=16 )
C7=m.addConstr(x3+x4+x5+x6+x7 >=11 )
#controle de saisie sur les x >=0
m.optimize()
#m.write("PL3.txt")
print('La valeur optimale est : %f' % m.objVal)
for v in m.getVars() :
    print('%s: %g' % (v.varName, v.x))