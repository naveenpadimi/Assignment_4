# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.



# sample input: 10

# sample output: 35

add_25 = lambda x: x + 25

number = int(input("Enter a number: "))
result = add_25(number)
print("Result after adding 25:", result)