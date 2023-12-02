from gurobipy import *
eg1=Model("eg1")
x1=eg1.addVar(lb=0, vtype= GRB.CONTINUOUS, name="x1") 
x2=eg1.addVar(lb=0, vtype= GRB.CONTINUOUS, name="x2")
eg1.setObjective(700*x1+900*x2, GRB.MAXIMIZE)
eg1.addConstr(3*x1+5*x2<=3600,"Bois")
eg1.addConstr(x1+2*x2<=1600,"Main d'oeuvre")
eg1.addConstr(50*x1+20*x2<=48000,"Machine")
eg1.optimize()
for var in eg1.getVars():
    print(var.varName, '=', var.x)
print("Objective value =", eg1.objVal)