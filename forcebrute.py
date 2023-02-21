import helper


budget = 500


def binary_convertion(possibility):
    binary_chain = format(possibility, "b")
    inversed_chain = ''.join(reversed(binary_chain))
    bit = enumerate(inversed_chain)
    return bit


def values_updated(actions_list, index, cost, profit, purchase_list):
    cost = cost + float(actions_list[index]['price'])
    profit = profit + float(actions_list[index]['netProfit'])
    purchase_list.append(actions_list[index]["name"])
    return {"cost": cost, "profit": profit}


def actions_combination(actions_list, budget):
    nb_possibilities = 2**(len(actions_list)-1) - 1
    best_profit = 0
    best_solution = 0
    best_purchase_list_cost = 0
    best = 0
    best_purchase_list = []
    for possibility in range(nb_possibilities):
        cost = 0
        profit = 0
        best_solution = best_solution + 1
        purchase_list = []
        bit = binary_convertion(possibility)
        for index, value in bit:
            if value == chr(ord('1')):
                if (cost + float(actions_list[index]['price'])) > budget:
                    break
                value_updated = values_updated(actions_list, index, cost,
                                               profit, purchase_list)
                cost = value_updated["cost"]
                profit = value_updated["profit"]
                if profit > best_profit:
                    best_profit = profit
                    best = best_solution
                    best_purchase_list = purchase_list
                    best_purchase_list_cost = cost
    return {"best": best, "best_profit": best_profit,
            "best_purchase_list": best_purchase_list,
            "best_purchase_list_cost": best_purchase_list_cost}


def display_result(best, best_profit, best_purchase_list,
                   best_purchase_list_cost):
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("Best solution is the solution " + str(best))
    print("The best profit = " + str(best_profit))
    print("The best purchase list is : " + str(best_purchase_list))
    print("The cost of the best purchase list is :" +
          str(best_purchase_list_cost))


for chosen_list in ['actions_list.csv', 'dataset1.csv', 'dataset2.csv']:
    data_list = helper.file_reader(chosen_list)
    result = actions_combination(data_list, budget)
    best = result["best"]
    best_profit = result["best_profit"]
    best_purchase_list = result["best_purchase_list"]
    best_purchase_list_cost = result["best_purchase_list_cost"]
    display_result(best, best_profit, best_purchase_list,
                   best_purchase_list_cost)
