import csv
from pulp import *


class Action:
    """_summary_
    defines an action
    """
    def __init__(self, id, cost, profit):
        self.id = id
        self.cost = cost
        self.profit = profit


def assign_actions(filename):
    """_summary_
    load all actions from a csv file

    Returns:
        list[Action] : list of Class action
    """
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            action = Action(int(row[0]), int(row[1]), float(row[2])/100)
            data.append(action)
    return data


def main():
    filename = "actions.csv"
    budget = 500
    actions = assign_actions(filename)

    # Crée un problème de programmation linéaire
    prob = LpProblem("Investment", LpMaximize)

    # Crée une variable binaire pour chaque action (0 pour non achetée, 1 pour achetée)
    action_vars = LpVariable.dicts("Action", [action.id for action in actions], 0, 1, LpInteger)

    # La fonction objective est de maximiser le profit total
    prob += lpSum([action.profit * action.cost * action_vars[action.id] for action in actions])

    # Contrainte : le coût total des actions achetées ne doit pas dépasser le budget
    prob += lpSum([action.cost * action_vars[action.id] for action in actions]) <= budget

    # Résoud le problème
    prob.solve()

    # Affiche le statut de la résolution
    print("Statut de la résolution:", LpStatus[prob.status])

    # Affiche les actions achetées et leur quantité
    for action in actions:
        if action_vars[action.id].value() == 1:
            print(f"Acheter {action.id}: {action_vars[action.id].value()} unité")

    # Affiche le profit total
    print("Profit total:", value(prob.objective))


if __name__ == "__main__":
    main()
