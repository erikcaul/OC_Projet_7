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


""" for action in actions_list:
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
 """
# fonctions recursives
def action_combinations(actions_list):
    best_profit = 0
    best_solution = 0
    best = 0
    for action_number in range(len(actions_list)):
        cost = 0
        profit = 0
        best_solution = best_solution + 1
        purchase_list = []
        cost = cost + int(actions_list[action_number]['price'])
        profit = profit + float(actions_list[action_number]['profit'])
        purchase_list.append(actions_list[action_number]["name"])
        if profit > best_profit:
            best_profit = profit
            best = best_solution
        i = action_number + 1
        for action_number in range(i, len(actions_list[i:])):
            if cost < budget:
                cost = cost + int(actions_list[action_number]['price'])
                profit = profit + float(actions_list[action_number]['profit'])
                purchase_list.append(actions_list[action_number]["name"])
                if cost > budget:
                    cost = cost - int(actions_list[action_number]['price'])
                    profit = profit - float(actions_list[action_number]['profit']) 
                if profit > best_profit:
                    best_profit = profit
                    best = best_solution
        actions_rest_list = actions_list.pop(action_number)
        if len(actions_rest_list) == 0:
            return 0
        else:
            action_combinations(actions_rest_list)
        """ i = action_number + 1
        for action_number in range(i, len(actions_rest_list[i:])):
            if cost < budget:
                cost = cost + int(actions_list[action_number]['price'])
                profit = profit + float(actions_list[action_number]['profit'])
                purchase_list.append(actions_list[action_number]["name"])
                if cost > budget:
                    cost = cost - int(actions_list[action_number]['price'])
                    profit = profit - float(actions_list[action_number]['profit']) 
                if profit > best_profit:
                    best_profit = profit
                    best = best_solution """
        print("The purchase actions list is : " + str(purchase_list))  
        print("The profit of the solution " + str(best_solution) + " is :" + str(profit))
        print("The cost of this solution is :" + str(cost))             
    print("Best solution is the solution " + str(best) + " = " + str(best_profit))
            
        
action_combinations(actions_list)       

# Pour une action donnée, je dois faire une liste de toutes les possibilités d'achats avec budget < 500
    # une liste du numéro action à max
    # une liste pour chaque autres possibilités
         #     
# répéter pour toutes les actions  
# ------------
# utiliser la forme binaire (0,1) : chaque élément ne peut prendre que 2 valeurs : une liste avec chaque élément, s'il est à 0 je l'utilise pas si à 1 je l'utilise
# liste de 4 éléments : comme si j'avais un nombre avec une représentation à 4 bit
# ex: 15 = 1111
# avec 4 éléments = un max de 15 combinaisons
# je prend le nombre d'éléments dans la liste
# for (2^nombre) - 1 : nombre de possibilités que j'ai au total = boucle ---> for i in range(2^20):
    # convertir en chaine binaire (un chiffre en sa représentation binaire) ---> convertir i en  chaine_binaire
    # for bit in chaine_binaire -(str)-: boucle
        # if bit -(chr)- == chr(ord('1')): 
            # prends les valeurs
        # enumerate bit in chaine_binaire: (lire la doc)
        # if bit == chr("1"):
        # index variable pour prendre index de la bonne action
     
# type chr, utiliser l'objet char pour la comparaison
# string une liste objet char
# doit être comparé à un autre char


# essayer toutes les possibilit/s et essayer la meilleure
# essayer avec action 1 et toutes les autres et calculer le benefice (jusqu'a 500)
# voir celui qui donne le max de benefice
# voir modele algo sur internet
# calculer le b/n/fice et le cout pour chaque combinaison
# garder le meilleur gain pour un budget <= 500