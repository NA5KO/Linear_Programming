import gurobipy as gp 
milestones= ["a","b","c","d"]
tasks, duration= gp.multidict({
    ("a","b"): 3,
    ("a","c"): 5,
    ("b","c"): 3,
    ("b","d"): 4,
    ("c","d"): 2, 
})
m= gp.Model("Example3B")
x= m.addVars(milestones, name="x")
m.setObjective(x[milestones[-1]] -x[milestones[0]])
m.addConstrs((x[j] -x[i] >= duration[(i,j)] 
              for(i,j) in tasks), name="constr")
m.optimize()
m.printAttr('X')