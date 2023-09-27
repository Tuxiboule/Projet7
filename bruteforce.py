import csv
from tqdm import tqdm


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
    n = len(actions)
    best_investment = []
    best_profit = 0

    for i in tqdm(range(1, 2**n)):
        current_budget = max_budget
        current_investment = []
        current_profit = 0

        for j in range(n):
            if (i >> j) & 1:
                action = actions[j]
                if action.cost <= current_budget:
                    current_investment.append(action)
                    current_budget -= action.cost
                    current_profit += action.cost * action.profit

        if current_profit > best_profit:
            best_profit = current_profit
            best_investment = current_investment

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
