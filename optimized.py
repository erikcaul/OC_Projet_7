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
purchase_list = []

def sort_data(data_list):
    sorted_data = sorted(data_list, key=lambda x:x['profit'], reverse=True)
    return sorted_data

def optimized_algo(sorted_data):
    profit = 0
    cost = 0
    for i in range(len(sorted_data)):
        if cost < budget:
            cost = cost + float(sorted_data[i]['price'])
            profit = profit + float(sorted_data[i]['profit'])
            purchase_list.append(sorted_data[i]["name"])
            if cost > budget:
                cost = cost - float(sorted_data[i]['price'])
                profit = profit - float(sorted_data[i]['profit'])
    return {"cost":cost, "profit":profit} 

def display_optimized_result(cost, profit):
    """ print("The purchase actions list is : " + str(purchase_list))   """
    print("The cost of this solution is :" + str(cost))
    print("The profit of this solution is :" + str(profit))           
    
sorted_actions_list = sort_data(actions_list)
result_actions_list = optimized_algo(sorted_actions_list)
display_optimized_result(result_actions_list["cost"], result_actions_list["profit"])

sorted_dataset1 = sort_data(dataset1)
result_dataset1 = optimized_algo(sorted_dataset1)
display_optimized_result(result_dataset1["cost"], result_dataset1["profit"])

sorted_dataset2 = sort_data(dataset2)
result_dataset2 = optimized_algo(sorted_dataset2)
display_optimized_result(result_dataset2["cost"], result_dataset2["profit"])

