import helper

budget = 500


def sort_data(data_list):
    sorted_data = sorted(data_list, key=lambda x: x['netProfit'], reverse=True)  # n log(n)
    return sorted_data


def optimized_algo(sorted_data):  # n log(n)
    purchase_list = []
    profit = 0.0
    cost = 0.0
    for i in range(len(sorted_data)):
        if float(sorted_data[i]["price"]) <= 0.0:
            continue
        if (cost + float(sorted_data[i]['price'])) <= budget:
            cost = cost + float(sorted_data[i]['price'])
            profit = profit + float(sorted_data[i]['netProfit'])
            purchase_list.append(sorted_data[i])
    return {"cost": cost, "profit": profit, "purchase_list": purchase_list}


def display_optimized_result(cost, profit, purchase_list):
    print("The purchase actions list is : " + str(purchase_list))
    print("The cost of this solution is :" + str(cost))
    print("The profit of this solution is :" + str(profit))


for chosen_list in ['actions_list.csv', 'dataset1.csv', 'dataset2.csv']:
    data_list = helper.file_reader(chosen_list)
    sorted_actions_list = sort_data(data_list)
    result_actions_list = optimized_algo(sorted_actions_list)
    display_optimized_result(result_actions_list["cost"],
                             result_actions_list["profit"],
                             result_actions_list["purchase_list"])
