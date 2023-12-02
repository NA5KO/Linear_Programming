import gurobipy as gp
numTasks= 4
m= gp.Model("Example")
x= m.addVars(numTasks, obj=[-1,0,0,1], 
            vtype=gp.GRB.CONTINUOUS)
m.addConstr(x[1] -x[0] >= 3)
m.addConstr(x[2] -x[0] >= 5)
m.addConstr(x[2] -x[1] >= 3)
m.addConstr(x[3] -x[1] >= 4)
m.addConstr(x[3] -x[2] >= 2)
m.optimize()
m.printAttr('X')
