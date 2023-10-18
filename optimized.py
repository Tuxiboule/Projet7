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
            if float(row[1]) > 0: # Check if value is positive
                action = Action(row[0], float(row[1]), float(row[2])/100)
                data.append(action)
    return data


def main():
    filename = "dataset2.csv"
    budget = 500
    actions = assign_actions(filename)

    # Create a linear programming problem
    prob = LpProblem("Investment", LpMaximize)

    # Create a binary variable for each action (0 for not purchased, 1 for purchased)
    action_vars = LpVariable.dicts("Action", [action.id for action in actions], 0, 1, LpInteger)

    # The objective function is to maximize the total profit
    prob += lpSum([action.profit * action.cost * action_vars[action.id] for action in actions])

    # Constraint: the total cost of purchased actions must not exceed the budget
    prob += lpSum([action.cost * action_vars[action.id] for action in actions]) <= budget

    # Resolve problem
    prob.solve()

    # Display the resolution status
    print("Statut de la résolution:", LpStatus[prob.status])

    # Display the purchased actions and their quantity
    for action in actions:
        if action_vars[action.id].value() == 1:
            print(f"Acheter {action.id}: {action_vars[action.id].value()} unité")

    # Display the total profit
    print("Profit total:", value(prob.objective))


if __name__ == "__main__":
    main()
