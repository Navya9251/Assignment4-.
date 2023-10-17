#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

number = lambda x : x + 25
n = int(input("Enter any number of your choice"))
print(number(n)) 

#Write a Python program to triple all numbers of a given list of integers. Use Python map.

nums = [1, 2, 3, 4, 5, 6, 7]
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums)
print("\nTriple of said list numbers: ")
print(list(result))

#Write a Python program to square the elements of a list using map() function.

def square_num(n):
    return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))