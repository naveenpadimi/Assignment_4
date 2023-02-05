# Write a Python program to square the elements of a list using map() function.



# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]



def square(num):
    return num**2

numbers = list(map(int,input("Enter a list of numbers separated by commas:").split(",")))

print("The Entered list : ",numbers)

squared_numbers = list(map(square ,numbers))

print("The Squared Numbers : ",squared_numbers)