import gurobipy as gp
from gurobipy import GRB
from itertools import combinations
import numpy as np

def construct_symmetric_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i+1): # we only need to fill the upper triangle
            while True: # Keep asking for input until the user enters a valid input
                try:
                    response = int(input(f"Est-ce que la région {i+1} est voisine de la région {j+1} ? (1 pour oui, 0 pour non) : "))
                    if response == 1 or response == 0:
                        matrix[i][j] = response
                        break # Exit the loop if the user entered a valid input
                    else:
                        print("Veuillez entrer 1 ou 0.")
                except ValueError:
                    print("Veuillez entrer 1 ou 0.")
    return matrix + matrix.T - np.diag(matrix.diagonal())

def solve_agency_location_problem(num_regions, B, K, D, a, b, c, A, population):
    # Création du modèle
    model = gp.Model("implantation_agences")    
    x = model.addVars(num_regions, vtype=GRB.BINARY, name="x")
    y = model.addVars(num_regions, vtype=GRB.BINARY, name="y")

    # Fonction objective
    Z = sum(a * population[i] + (b * sum(A[i][j] * population[j] for j in range(num_regions) if i != j) + c * y[i] * population[i]) * x[i] for i in range(num_regions))
    model.setObjective(Z, GRB.MAXIMIZE)

    # Contraintes budgétaires
    model.addConstr(K * x.sum() + D * y.sum() <= B, "contrainte_budget")

    # Contraintes de non-ouverture d'agences dans des régions voisines
    for i, j in combinations(range(num_regions), 2):
        if A[i][j] == 1:
            model.addConstr(A[i][j] * (x[i] + x[j]) <= 1, f"contrainte_voisines_{i}_{j}")
    
    # Contraintes d'avoir des clients de toutes les régions
    for i in range(num_regions):
        model.addConstr(sum(A[i][j] * x[j] for j in range(num_regions)) + y[i] >= 1, f"contrainte_clients_{i}")
    
    model.optimize()

    # Récupérer les résultats
    results = {"regions": []}
    for i in range(num_regions):
        region_result = {
            "Region": i + 1,
            "Agence": int(x[i].getAttr('X')),
            "Serveur_DAB": int(y[i].getAttr('X'))
        }
        results["regions"].append(region_result)
    
    results["Objective_value"] = model.objVal

    return results

# Exemple d'utilisation:
num_regions = int(input("Nombre de régions : "))
B = float(input("Budget total (B) : "))
K = float(input("Coût d'ouverture d'une agence (K) : "))
D = float(input("Coût d'installation d'un serveur DAB (D) : "))
a = float(input("Pourcentage de la population de la région pour les agences (a) : "))
b = float(input("Pourcentage de la population des régions voisines pour les agences (b) : "))
c = float(input("Pourcentage de la population de la région pour les serveurs DAB (c) : "))
A = construct_symmetric_matrix(num_regions)
population = []
for i in range(num_regions):
    pop = float(input(f"Population de la région {i+1} : "))
    population.append(pop)

result = solve_agency_location_problem(num_regions, B, K, D, a, b, c, A, population)
print("Solution optimale:")
for region_result in result["regions"]:
    print(f"Région {region_result['Region']}: Agence={region_result['Agence']}, Serveur DAB={region_result['Serveur_DAB']}")
print("Objective value =", result["Objective_value"])
