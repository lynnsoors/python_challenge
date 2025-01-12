#import modules
import os
import csv

#Path to data file
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#open csv, set reader
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read and print header
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    
    #set variables
    month_count = 0
    net_profit_loss = 0
    current_month = 0
    previous_month = 0
    #equation current month value - previous month value
    monthly_change = 0 
    #empty list for months and to hold monthly_change
    months = []
    monthly_profit_loss = []

    #begin pulling data from rows after header
    for row in csv_reader:
        #add to month count
        month_count += 1
        #set current month
        current_month = (int(row[1]))
        #add to net profit/loss variable
        net_profit_loss += current_month

        #set conditions
        #set the previous month value to first month
        if month_count == 1:
                previous_month = current_month
        
        else:
            #equation to add value to monthly change
            monthly_change = current_month - previous_month
            #add month name to list
            months.append(row[0])
            #add monthly change to list
            monthly_profit_loss.append(monthly_change)
            #set variable for next loop
            previous_month = current_month

    #calculate average change
    average_change = (sum(monthly_profit_loss))/ (month_count - 1)

    #print to terminal
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Average Change: {(round(average_change,2))}")
    print(f"Greatest Increase: ${(max(monthly_profit_loss))}")
    print(f"Greatest Decrease: ${(min(monthly_profit_loss))}")

    #print to text file
    #set variable for output file
    output_file = os.path.join('..', 'PyBank', 'Analysis', 'final_analysis.txt')

#open output file and add reporting
with open(output_file, "w") as outfile:
    writer = csv.writer(outfile)

    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total Months: {month_count}")
    outfile.write("\n")
    outfile.write(f"Average Change: {(round(average_change,2))}")
    outfile.write("\n")
    outfile.write(f"Greatest Increase: ${(max(monthly_profit_loss))}")
    outfile.write("\n")
    outfile.write(f"Greatest Decrease: ${(min(monthly_profit_loss))}")