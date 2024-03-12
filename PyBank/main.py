import os
import csv

budget_data = os.path.join("budget_data.csv")

total_months = 0
total_p1 = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_p1 += int(first_row [1])
    value = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_months += 1

        total_p1 = total_p1 + int(row[1])

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    average_change = sum(profits)/len(profits)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"total: ${total_p1}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

analysis_file = open("analysis.txt", "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {total_months}")
line4 = str(f"total: ${total_p1}")
line5 = str(f"Average Change: ${average_change}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

analysis_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))


    

