import csv

with open('actions_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    actions_list = list(reader)

with open('dataset1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dataset1 = list(reader)

with open('dataset2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dataset2 = list(reader)

budget = 500


def sort_data(data_list):
    sorted_data = sorted(data_list, key=lambda x: x['profit'], reverse=True)
    return sorted_data


def optimized_algo(sorted_data):
    purchase_list = []
    profit = 0.0
    cost = 0.0
    for i in range(len(sorted_data)):
        if float(sorted_data[i]["price"]) <= 0.0:
            continue
        if (cost + float(sorted_data[i]['price'])) <= budget:
            cost = cost + float(sorted_data[i]['price'])
            profit = profit + float(sorted_data[i]['profit'])
            purchase_list.append(sorted_data[i])
    return {"cost": cost, "profit": profit, "purchase_list": purchase_list}


def display_optimized_result(cost, profit, purchase_list):
    print("The purchase actions list is : " + str(purchase_list))
    print("The cost of this solution is :" + str(cost))
    print("The profit of this solution is :" + str(profit))


# optimized alog with actions_list data
sorted_actions_list = sort_data(actions_list)
result_actions_list = optimized_algo(sorted_actions_list)
display_optimized_result(result_actions_list["cost"],
                         result_actions_list["profit"],
                         result_actions_list["purchase_list"])


# optimized alog with dataset1
sorted_dataset1 = sort_data(dataset1)
result_dataset1 = optimized_algo(sorted_dataset1)
display_optimized_result(result_dataset1["cost"], result_dataset1["profit"],
                         result_dataset1["purchase_list"])

# optimized alog with dataset2
sorted_dataset2 = sort_data(dataset2)
result_dataset2 = optimized_algo(sorted_dataset2)
display_optimized_result(result_dataset2["cost"], result_dataset2["profit"],
                         result_dataset2["purchase_list"])
