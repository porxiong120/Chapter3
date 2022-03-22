

# grade = 90
# condition = grade >=90
# # condition = 90 >=90 # substitute 4 grade
# # if 90 >=90: # substitute 4 condition
# if not condition:
#     # execute when true 
#     print("Your grade is A")
# else:
#     # execute when false 
#     print("Your grade is not A")

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))

#num1 = input("Enter the first number: ")
#num2 = input("Enter the second number: ")
# print("1", num1, "2", num2)
# if num1 > num2: # works, but not logical
# print(isinstance(num1, int))
# print(isinstance(num1, str)) # false if we put 2 numbers
#print("1", isinstance(num1, str))
#print("2", isinstance(num1, str))
#if isinstance(num1,str) or isinstance(num2, str):
#    print("Data type not allowed! Please specify a numeric value.")
#else:
#    num1 = eval(num1)
#    num2 = eval(num2)
#    if num1 > num2:
#        largerVal = num1
#    else:
#        largerVal = num2
#
#    print("The larger value is " + str(largerVal))
# if num1 > num2:
#     largerVal = num1
# else:
#     largerVal = num2

# print("The larger value is " + str(largerVal))

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# try:
#     print("1", isinstance(num1, str))
#     print("2", isinstance(num1, str))
#     if isinstance(num1,str) or isinstance(num2, str):
#         print("Data type not allowed! Please specify a numeric value.")
#     else:
#         if num1 > num2:
#             largerVal = num1
#         else:
#             largerVal = num2

#     print("The larger value is " + str(largerVal))
# except:
#     print("Data not allowed!")

answer = eval(input("How many gallons does a ten-gallon hat hold? "))

if (.5 <= answer <= 1):
    print("Good, ", end="") # Good, it holds about 3/4 of a gallon
else:
    print("No, ", end="") # No, it holds about 3/4 of a gallon4

print("it holds about 3/4 of a gallon.")

def is_greater_than10():
    answer = eval(input("How many gallons does a ten-gallon hat hold? "))
    if answer > 10:
        return True
    return False