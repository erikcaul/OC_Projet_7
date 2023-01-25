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
best_purchase_list_cost = 0
best = 0
best_purchase_list = []
nb_possibilities = 2**20 - 1

for i in range(nb_possibilities):
    cost = 0
    profit = 0
    best_solution = best_solution + 1
    purchase_list = []
    binary_chain = format(i, "b")
    inversed_chain = ''.join(reversed(binary_chain))
    # print(chaine_binaire)
    # print(chaine_inversee)
    bit = enumerate(inversed_chain)
    # print(bit)
    for index, value in bit:
        if value == chr(ord('1')) and (cost + int(actions_list[index]['price'])) < budget:
            # print(f"valeur = {valeur} / index = {index}")
            cost = cost + int(actions_list[index]['price'])
            profit = profit + float(actions_list[index]['profit'])
            purchase_list.append(actions_list[index]["name"])
            if profit > best_profit:
                best_profit = profit
                best = best_solution
                best_purchase_list = purchase_list
                best_purchase_list_cost = cost
        """ else:
            print(f"valeur = {valeur} / index = {index}") """
    # print("The purchase actions list is : " + str(purchase_list))  
    # print("The profit of the solution " + str(best_solution) + " is :" + str(profit))
    # print("The cost of this solution is :" + str(cost))             
print("----------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")
print("Best solution is the solution " + str(best))
print("The best profit = " + str(best_profit))
print("The best purchase list is : " + str(best_purchase_list))
print("The cost of the best purchase list is :" + str(best_purchase_list_cost))        
