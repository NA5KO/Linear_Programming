from gurobipy import *
produits = range(2) # les deux produits
ressources = range(3) # les ressources
prix = [700,900]
ressources_consommations = [[3,5],[1,2],[50,20]]
ressources_disponibilité = [3600,1600,48000]
eg1_de=Model("eg1_decoupage")
x=[]
for i in produits:
  x.append(eg1_de.addVar(lb=0, vtype = GRB.CONTINUOUS, name='x'+str(i)))
eg1_de.setObjective(quicksum(prix[i]*x[i] for i in produits), GRB.MAXIMIZE)
#ajoutez des contraintes et nommez-les.
eg1_de.addConstrs((quicksum(ressources_consommations[j][i]*x[i] for i in 
                            <=ressources_disponibilité[j] for j in ressources ),"limitations des containtres "))
eg1_de.optimize()
for var in eg1_de.getVars():
  print(var.varName, '=', var.x)
  print("Objective value =", eg1_de.objVal)