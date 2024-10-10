#task 1
num1 = int(input("Enter a number, please."))
num2 = int(input("Enter another number, please."))
num3 = int(input("Enter your final number, please."))

# answer using if statements
if num1 >= num2 and num1 >= num3:
    greatest_num = num1
elif num2 >= num1 and num2 >= num3:
    greatest_num = num2 
else:
    greatest_num = num3

# simple answer using built in max function
# greatest_num = max(num1, num2, num3)    

print(f"The greatest number is {greatest_num}")


#task 2
num1 = int(input("Enter a number, please."))
num2 = int(input("Enter another number, please."))
num3 = int(input("Enter your final number, please."))

lowest_num = min(num1, num2, num3)    

print(f"The lowest number is {lowest_num}")