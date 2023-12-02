import gurobipy as gp
from gurobipy import GRB
m= gp.Model()
x= m.addVar(vtype=gp.GRB.BINARY, name="x")
y= m.addVar(vtype=gp.GRB.BINARY, name="y")
z= m.addVar(vtype=gp.GRB.BINARY, name="z")
m.setObjective(x+ y+ 2*z, gp.GRB.MAXIMIZE)
c1= m.addConstr(x+ 2*y+ 3*z<= 4)
c2= m.addConstr(x+ y>= 1)
m.optimize()
