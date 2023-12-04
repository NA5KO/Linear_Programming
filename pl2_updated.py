#!/usr/bin/env python
# coding: utf-8

# In[6]:


import gurobipy as gp

nb_mois = 4  # champ nombre de mois

cout_stockage = 5  # champ Coût de stockage
salaire_ouvrier = 1500  # champ Salaire d’un ouvrier
cout_heure_supplementaire = 6  # champ Coût d’une heure supplémentaire
frais_recrutement = 1600  #champ  Frais de recrutement d’un ouvrier
frais_licenciement = 1400  #champ  Frais de licenciement d’un ouvrier
cout_matiere_premiere = 5  #champ  Coût de matière première par paire
max_heures_supplementaires = 20  #champ  le maximum des heures supplementaires par ouvrier 
stock_initial = 500  #champ  le stock initial
nombre_initiale_ouvriers = 100  # champ le nombre  d'ouvriers initial
heures_travail_paire=4 #  champs le nombre d'heures par chaussures 
heures_travail_ouvrier=160 #champs le nombre d'heures de travail d'un ouvier par mois 

demande_du_mois = {0: 2000, 1: 1500, 2: 3000, 3: 4000}  # les champs demande de mois i 

model = gp.Model("pl2")

# Ajoutez les variables de décision au modèle
heures_sup = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"heures_sup_{t}") for t in range(nb_mois)}
paires_chaussures = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"paires_chaussures_{t}") for t in range(nb_mois)}
ouvriers_rec = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"ouvriers_rec_{t}") for t in range(nb_mois)}
ouvriers_lic = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"ouvriers_lic_{t}") for t in range(nb_mois)}
ouvriers_dispo = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"ouvriers_dispo_{t}") for t in range(nb_mois)}
stock = {t: model.addVar(vtype=gp.GRB.INTEGER, name=f"stock_{t}") for t in range(nb_mois)}


model.update



# Contraintes
for t in range(nb_mois):
    if t > 0:
        model.addConstr(ouvriers_dispo[t] == ouvriers_dispo[t - 1] + ouvriers_rec[t] - ouvriers_lic[t])
        model.addConstr(stock[t] == stock[t - 1] + paires_chaussures[t - 1] - demande_du_mois[t - 1])
    else:
        model.addConstr(ouvriers_dispo[t] == nombre_initiale_ouvriers + ouvriers_rec[t] - ouvriers_lic[t])
        model.addConstr(stock[t] == stock_initial )

    
    model.addConstr(heures_sup[t] <= max_heures_supplementaires * ouvriers_dispo[t])

   
    model.addConstr(stock[t] + paires_chaussures[t] >= demande_du_mois[t])

    model.addConstr(paires_chaussures[t] <= (1 / heures_travail_paire) * (heures_sup[t] + ouvriers_dispo[t] * heures_travail_ouvrier))



model.addConstrs((stock[t] >= 0 for t in range(nb_mois)))
model.addConstrs((ouvriers_dispo[t] >= 0 for t in range(nb_mois)))
model.addConstrs((ouvriers_rec[t] >= 0 for t in range(nb_mois)))
model.addConstrs((ouvriers_lic[t] >= 0 for t in range(nb_mois)))
model.addConstrs((heures_sup[t] >= 0 for t in range(nb_mois)))

# Fonction objective
model.setObjective(
    gp.quicksum(
        stock[t] * cout_stockage
        + ouvriers_rec[t] * frais_recrutement
        + ouvriers_lic[t] * frais_licenciement
        + heures_sup[t] * cout_heure_supplementaire
        + paires_chaussures[t] * cout_matiere_premiere
        + ouvriers_dispo[t] * salaire_ouvrier
        for t in range(nb_mois)
    ),
    gp.GRB.MINIMIZE
)

# Résoudre le modèle
model.optimize()
# Résoudre le modèle
model.optimize()

# Afficher les résultats
if model.status == gp.GRB.OPTIMAL:
    print("Solution optimale trouvée!")
    

    # Afficher les valeurs des variables de décision
    for t in range(nb_mois):
        
        print(f"   Heures supplémentaires : {heures_sup[t].x}")
        print(f"   Paires de chaussures produites : {paires_chaussures[t].x}")
        print(f"   Ouvriers recrutés : {ouvriers_rec[t].x}")
        print(f"   Ouvriers licenciés : {ouvriers_lic[t].x}")
        print(f"   Ouvriers disponibles : {ouvriers_dispo[t].x}")
        print(f"   Stock : {stock[t].x}")
else:
    print("Le problème n'a pas pu être résolu de manière optimale.")



# In[ ]:





# In[ ]:




