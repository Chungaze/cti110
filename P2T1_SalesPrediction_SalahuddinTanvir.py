# This program will ask a user to enter the projected amount of total sales,
# and then display the profit that will be made from that amount
# 2-17-2020
# CTI-110 P2T1 - Sales Prediction
# 

# Get user input: projected total sales
total_sales = float(input('Enter the projected sales: ')
                     )

# Calculate 'profit' as 23% of total sales
profit = total_sales * 0.23

# Display results of the calculation
print('The profit is $', format(profit, ',.2f'))
