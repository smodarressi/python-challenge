#Dependencies/Modules
import os
import csv

#path to budget open csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")


with open(budget_data_csv, newline='') as budget:
    
    budget_reader = csv.reader(budget, delimiter=',')
    budget_header = next(budget_reader)
    
    month_counter = 0
    month_list = []
    profit_loss_total = 0
    profit_loss_list = []
    for row in budget_reader:
        #make month list
        month_list.append(row[0])
        #number of months
        month_counter += 1
        #sum of profit/loss total
        profit_loss_total = int(row[1]) + profit_loss_total
        profit_loss_list.append(int(row[1]))
    
    #since I want to find the average of each, i will make a list of pairs to evaluate
    pair_of_values = zip(profit_loss_list[:-1], profit_loss_list[1:])
    
    #above created tuple list of averages
    #at each index (x,y) where x is the profit loss list without the last value and y is the same list without the first value 
    
    #list comprehension finding difference with the list of pairs to evaluate
    differences_profit_loss = [((y - x)) for (x, y) in pair_of_values]

    #average change of complete data
    average_change = (sum(differences_profit_loss)/(len(differences_profit_loss)))
    
    #finding max change
    max_difference = max(differences_profit_loss)
    find_max_month_index = differences_profit_loss.index(max_difference)
    
    #i want the month that is largest/smallest
    #since the list of tuples removed the first and last values, I have to add one
    
    #max month
    max_month = month_list[(find_max_month_index + 1)]
    
    #finding min month
    min_difference = min(differences_profit_loss)
    find_min_month_index = differences_profit_loss.index(min_difference)
    min_month = month_list[(find_min_month_index + 1)]

report_to_print =(
'''
  Financial Analysis
  ----------------------------
  Total Months: {}
  Total: ${}
  Average  Change: ${:.2f}
  Greatest Increase in Profits: {} $({})
  Greatest Decrease in Profits: {} $({})
  ```
'''.format(month_counter, profit_loss_total, average_change, max_month, max_difference, min_month, min_difference))
print(report_to_print)

#writes financial_report.txt to same folder as main.py
with open('financial_report.txt', 'w', newline='') as finance_report:
        finance_report.write(report_to_print)


# print(month_counter)
# print(profit_loss_total)
# print(average_change)
# print(max_month)
# print(max_difference)
# print(min_month)
# print(min_difference)
