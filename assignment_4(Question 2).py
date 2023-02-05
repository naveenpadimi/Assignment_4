# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


def triple(num):
        return num * 3

numbers = list(map(int, input("Enter a list of numbers separated by comma: ").split(",")))

print("The Entered list : ",numbers)

tripled_numbers = list(map(triple, numbers))

print("The tripled List : ",tripled_numbers)  








