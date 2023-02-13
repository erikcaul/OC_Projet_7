import csv

with open('actions_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    actions_list = list(reader)

budget = 500
profit = 0
best_profit = 0
best_solution = 0
best = 0
cost = 0
purchase_list = []

sorted_data = sorted(actions_list, key=lambda x:x['profit'], reverse=True)

for i in range(len(sorted_data)):
    if cost < budget:
        cost = cost + int(sorted_data[i]['price'])
        profit = profit + float(sorted_data[i]['profit'])
        purchase_list.append(sorted_data[i]["name"])
        if cost > budget:
            cost = cost - int(sorted_data[i]['price'])
            profit = profit - float(sorted_data[i]['profit']) 
print("The purchase actions list is : " + str(purchase_list))  
print("The cost of this solution is :" + str(cost))
print("The profit of this solution is :" + str(profit))           