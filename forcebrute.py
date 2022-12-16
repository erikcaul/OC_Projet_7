import csv

with open('actions_list.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['name','price','profit'])
    filewriter.writerow(['action_1',20,0.05])
    filewriter.writerow(['action_2',30,0.1])
    filewriter.writerow(['action_3',50,0.15])
    filewriter.writerow(['action_4',70,0.20])
    filewriter.writerow(['action_5',60,0.17])
    filewriter.writerow(['action_6',80,0.25])
    filewriter.writerow(['action_7',22,0.07])
    filewriter.writerow(['action_8',26,0.11])
    filewriter.writerow(['action_9',48,0.13])
    filewriter.writerow(['action_10',34,0.27])
    filewriter.writerow(['action_11',42,0.17])
    filewriter.writerow(['action_12',110,0.09])
    filewriter.writerow(['action_13',38,0.23])
    filewriter.writerow(['action_14',14,0.01])
    filewriter.writerow(['action_15',18,0.03])
    filewriter.writerow(['action_16',8,0.08])
    filewriter.writerow(['action_17',4,0.12])
    filewriter.writerow(['action_18',10,0.14])
    filewriter.writerow(['action_19',24,0.21])
    filewriter.writerow(['action_20',114,0.18])

with open('actions_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    actions_list = list(reader)


budget = 500
best_profit = 0
best_solution = 0
best = 0

for action in actions_list:
    cost = 0
    profit = 0
    best_solution += 1
    print(action["name"])
    purchase_list = []
    for i in range(len(actions_list)):
        if action["name"] != actions_list[i]["name"]:
            if cost < budget:
                cost = cost + int(actions_list[i]['price'])
                profit = profit + float(actions_list[i]['profit'])
                purchase_list.append(actions_list[i]["name"])
                if cost > budget:
                    cost = cost - int(actions_list[i]['price'])
                    profit = profit - float(actions_list[i]['profit']) 
                if profit > best_profit:
                    best_profit = profit
                    best = best_solution
    print("The purchase actions list is : " + str(purchase_list))  
    print("The profit of the solution " + str(best_solution) + " is :" + str(profit))
    print("The cost of this solution is :" + str(cost))             
print("Best solution is the solution " + str(best) + " = " + str(best_profit))


# essayer toutes les possibilit/s et essayer la meilleure
# essayer avec action 1 et toutes les autres et calculer le benefice (jusqu'a 500)
# voir celui qui donne le max de benefice
# voir modele algo sur internet
# calculer le b/n/fice et le cout pour chaque combinaison
# garder le meilleur gain pour un budget <= 500