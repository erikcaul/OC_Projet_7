import csv

with open('actions_list.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['name', 'price', 'profit'])
    filewriter.writerow(['action_1', 20, 0.05])
    filewriter.writerow(['action_2', 30, 0.1])
    filewriter.writerow(['action_3', 50, 0.15])
    filewriter.writerow(['action_4', 70, 0.20])
    filewriter.writerow(['action_5', 60, 0.17])
    filewriter.writerow(['action_6', 80, 0.25])
    filewriter.writerow(['action_7', 22, 0.07])
    filewriter.writerow(['action_8', 26, 0.11])
    filewriter.writerow(['action_9', 48, 0.13])
    filewriter.writerow(['action_10', 34, 0.27])
    filewriter.writerow(['action_11', 42, 0.17])
    filewriter.writerow(['action_12', 110, 0.09])
    filewriter.writerow(['action_13', 38, 0.23])
    filewriter.writerow(['action_14', 14, 0.01])
    filewriter.writerow(['action_15', 18, 0.03])
    filewriter.writerow(['action_16', 8, 0.08])
    filewriter.writerow(['action_17', 4, 0.12])
    filewriter.writerow(['action_18', 10, 0.14])
    filewriter.writerow(['action_19', 24, 0.21])
    filewriter.writerow(['action_20', 114, 0.18])


def add_net_profit(data_list):
    for i in range(len(data_list)):
        data_list[i]['netProfit'] = float(data_list[i]['price']) *\
                                    (float(data_list[i]['profit'])/100)
    return data_list


def file_reader(file_path):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        actions_list = list(reader)
        add_net_profit(actions_list)
        return actions_list
