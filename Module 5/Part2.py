# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased
# each month. The points are awarded as follows:
#
#    If a customer purchases 0 books, they earn 0 points.
#    If a customer purchases 2 books, they earn 5 points.
#    If a customer purchases 4 books, they earn 15 points.
#    If a customer purchases 6 books, they earn 30 points.
#    If a customer purchases 8 or more books, they earn 60 points.
#  
# Write a program that asks the user to enter the number of books that they have purchased this month and then display
# the number of points awarded.

# Define variables
num_points = 0
points = {
    '0': 0,
    '2': 5,
    '4': 15,
    '6': 30,
    '8': 60}

# Reverse sort the dictionary
reverse_sorted_points = {}
for key in sorted(points, key=points.get, reverse = True):
    reverse_sorted_points[key] = points[key]

# Get number of books
num_books = int(input('Enter number of books:\n'))

# Traverse through reverse sorted dictiony, break upon match
index = 0
for value in reverse_sorted_points:
    if num_books >= int(value):
        num_points = reverse_sorted_points[value]
        break
    index += 1

print('You earned {} points!'.format(num_points))
    
 
 