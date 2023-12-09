#!/usr/bin/env python
# coding: utf-8

# In[4]:


import gurobipy as gp
from gurobipy import GRB

#  a partir de l'interface les champs zones sont regroupés dans une liste
zones = [1, 2, 3,4,5]

# a partir de l'interface les sites qui entourent chaque zone sont regroupés dans une liste
sites = [
    ['A','B'],
    ['A', 'E','F'],
    ['B', 'D'],['C','E','G'],['G','F']
]
 

# a partir de l'interface les champs antennes necessaires sont regroupés dans une liste 
antennas_required = [1, 1, 1,2,1]


# Création d'un dictionnaire des sites uniques 
unique_sites = set(site for sublist in sites for site in sublist)

# Création du modèle
model = gp.Model("CoverageProblem")

# Variables de décision pour chaque site
x = {}
for site in unique_sites:
    x[site] = model.addVar(vtype=GRB.BINARY, name=f"x_{site}")

# Fonction objectif
model.setObjective(gp.quicksum(x[site] for site in unique_sites), sense=GRB.MINIMIZE)

# Contraintes pour chaque zone
for i, zone in enumerate(zones):
    # Contrainte pour chaque zone : la somme des variables binaires des sites entourant la zone doit être supérieure ou égale au nombre d'antennes requis
    model.addConstr(gp.quicksum(x[site] for site in sites[i]) >= antennas_required[i], f"antenna_constraint_{i}")

# Résolution
model.optimize()

# Affichage des résultats
if model.status == GRB.OPTIMAL:
    print("Solution optimale:")
    for site in unique_sites:
        print(f"Site {site}: Antenne = {int(x[site].x)}")
else:
    print("Aucune solution optimale trouvée.")


# In[ ]:




