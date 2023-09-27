import csv
from tqdm import tqdm
import itertools


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


def find_best_investment(actions, max_budget):
    """_summary_

    Args:
        actions (Action)
        max_budget (int)

    Returns:
        best_investment list[Action]: list of best actions comination
        best_profit int: amount of best profit
    """
    best_investment = []
    best_profit = 0

    for r in tqdm(range(1, len(actions) + 1)):
        for combination in itertools.combinations(actions, r):
            total_cost = sum(action.cost for action in combination)
            total_profit = sum(action.profit*action.cost for action in combination)

            if total_cost <= max_budget and total_profit > best_profit:
                best_profit = total_profit
                best_investment = list(combination)

    return best_investment, best_profit


def main():
    # initalise variable
    filename = "actions.csv"
    max_budget = 500
    actions = assign_actions(filename)

    # finding best investment and best_profit
    best_investment, best_profit = find_best_investment(actions, max_budget)

    # display best investment and associated profit
    print("Meilleur investissement :")
    for action in best_investment:
        print(f"Action-{action.id} (Coût : {action.cost} €, Bénéfice : {(action.cost * action.profit):.2f} €)")

    print(f"Bénéfice total : {best_profit:.2f} €")


if __name__ == "__main__":
    main()
