# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program
# should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve
# times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After
# all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per
# month for the entire period.

# Initialize Variables
years = 0
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
month = ''
rainfall_per_month = []
num_months = 0
total_rainfall = 0

# Ask for number of years from the user
years = int(input('Enter number of years: '))

# Cycle through years and months and prompt user for rainfall
for year in range(years):
    for month in months:
        rainfall_per_month.append(int(input('Year {}.  Enter rainfall in decimal inches that occured in {}: '.format(year + 1,month))))
        total_rainfall = total_rainfall + rainfall_per_month[num_months]
        num_months += 1

# Display results
print('Number of months: {}'.format(num_months))
print('Total rainfall: {} inches'.format(total_rainfall))
print('Average rainfall per month: {:.2f} inches'.format(total_rainfall / num_months))