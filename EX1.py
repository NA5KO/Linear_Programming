import gurobipy as gp
from gurobipy import GRB

# Demander à l'utilisateur de saisir le nombre de cultures
nombre_cultures = int(input("Entrez le nombre de cultures : "))

# Liste pour stocker les noms des cultures
cultures = []
for i in range(nombre_cultures):
    nom_culture = input(f"Entrez le nom de la culture {i+1}: ")
    cultures.append(nom_culture)

# Demander à l'utilisateur de saisir la limite pour la contrainte Superficie Totale
superficie_totale_limit = float(input("Entrez la limite pour la contrainte Superficie Totale: "))

# Créer un dictionnaire pour mapper les noms des cultures à leurs indices
indices_cultures = {culture: i for i, culture in enumerate(cultures)}

# Demander à l'utilisateur de saisir les valeurs pour R
R = [float(input(f"Entrez la valeur pour R[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour P
P = [float(input(f"Entrez la valeur pour P[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour MO
MO = [float(input(f"Entrez la valeur pour MO[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour T
T = [float(input(f"Entrez la valeur pour T[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour E
E = [float(input(f"Entrez la valeur pour E[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour S
S = [float(input(f"Entrez la valeur pour S[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir les valeurs pour F
F = [float(input(f"Entrez la valeur pour F[{culture}]: ")) for culture in cultures]

# Demander à l'utilisateur de saisir la valeur pour CM
CM = float(input("Entrez la valeur pour CM: "))

# Demander à l'utilisateur de saisir la valeur pour CE
CE = float(input("Entrez la valeur pour CE: "))

# Demander à l'utilisateur de saisir les valeurs pour les contraintes
temps_machine_limit = float(input("Entrez la limite pour la contrainte Temps Machine: "))
main_oeuvre_limit = float(input("Entrez la limite pour la contrainte Main d'oeuvre: "))
eau_limit = float(input("Entrez la limite pour la contrainte Eau: "))

model = gp.Model("Exercice 1")

x = []
for culture in cultures:
    x.append(model.addVar(lb=0, vtype=GRB.CONTINUOUS, name=f'x_{culture}'))

fct = 0
for i, culture in enumerate(cultures):
    fct += x[i] * ((R[i] * P[i]) - (MO[i] * S[i] + CM * T[i] + CE * E[i]) - F[i])

ST = 0
for i, culture in enumerate(cultures):
    ST += x[i] * T[i]

SMO = 0
for i, culture in enumerate(cultures):
    SMO += x[i] * MO[i]

SE = 0
for i, culture in enumerate(cultures):
    SE += x[i] * E[i]

Nombrehectares= 0
for i, culture in enumerate(cultures):
    Nombrehectares += x[i] 

model.setObjective(fct, GRB.MAXIMIZE)
model.addConstr(ST <= temps_machine_limit, "Temps Machine")
model.addConstr(SMO <= main_oeuvre_limit, "Main d'oeuvre")
model.addConstr(SE <= eau_limit, "Eau")
model.addConstr(Nombrehectares <= superficie_totale_limit , "Superficie du terrain ")
model.optimize()

for var in model.getVars():
    print(var.varName, '=', var.x)

print("Objective value =", model.objVal)
