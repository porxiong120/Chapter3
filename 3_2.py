

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

# answer = eval(input("How many gallons does a ten-gallon hat hold? "))

# if (.5 <= answer <= 1):
#     print("Good, ", end="") # Good, it holds about 3/4 of a gallon
# else:
#     print("No, ", end="") # No, it holds about 3/4 of a gallon4

# print("it holds about 3/4 of a gallon.")

# def is_greater_than10():
#     answer = eval(input("How many gallons does a ten-gallon hat hold? "))
#     if answer > 10:
#         return True
#     return False


# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))

# max = first_num

# if second_num > max:
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest number of the three number is " + str(max) + ".")

# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))

# max = first_num

# if second_num > max:
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest number of the three number is " + str(max) + ".")

# numbers = []
# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))
# numbers.append(first_num)
# numbers.append(second_num)
# numbers.append(third_num)
# msg = "The largest number of the three number is " + str(max(numbers)) + "."
# print(msg)


# color = input("Enter a color (BLUE or RED): ")
# mode = input("Enter a mode (STEACY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()

# results = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else:
#         result = "Cloud Due."
# else: 
#     if mode == "STEADY":
#         result = "Rain Ahead."
#     else: 
#         result = "Snow Ahead."
# print("The weather forecast is", result)

# color = input("Enter a color (BLUE or RED): ").upper()
# mode = input("Enter a mode (STEACY or FLASHING): ").upper()

# results = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else: # mode is FLASHING
#         result = "Cloud Due."
# else: # color is RED
#     if mode == "STEADY":
#         result = "Rain Ahead."
#     else: # mode is FLASHING
#         result = "Snow Ahead."
# print("The weather forecast is", result)


# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even."
# else:
#     if costs < revenue: 
#         profit = revenue -costs 
#         result = "Profit is ${0:,.2f}.".format(profit)
#     else: 
#         loss = costs - revenue 
#         result = "Loss is ${0:,.2f}.".format(loss)
# print(result)


# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even."
# else:
#     profit = revenue -costs 
#     result = "is ${0:,.2f}.".format(profit)
#     if profit < 0:
#         result = "Loss " + result
#     else:
#         result = "Profit" + result
# print(result)


# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even."
# else:
#     profit = revenue -costs 
#     result = "is ${0:,.2f}.".format(profit)
#     if profit < 0:
#         print("Loss " + result)
#     print("Profit" + result)


# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     print("Break even.")
#     result = "is ${0:,.2f}.".format(revenue - costs)
#     if (crevenue - costs) < 0:
#         print("Loss " + result)
#     print("Profit" + result)


# num1 = eval(input("Enter first number: "))
# num2 = eval(input("Enter second number: "))

# if num1 > num2:
#     print("The larger value is", str(num1) + ".")
# elif num2 > num1:
#     print("The larger value is", str(num2) + ".")
# else: 
#     print("The two values are equal.")


# gpa = eval(input("Enter your gpa: "))

# if gpa >= 3.9:
#     honors = " summa cum laude."
# elif gpa >= 3.6:
#     honors = " magna cum laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."

# print("You graduated" + honors)


# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     else: 
#         print("The first entry was not a proper number.")
# else: 
#     print("The second entry was not a proper number.")


# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.") 
#     print("The first entry was not a proper number.")
# print("The second entry was not a proper number.")


# if 7: 
#     print("A nonzero number is true.")
# else: 
#     print("The number zero is false.")
# if []: 
#     print("A nonempty list is true.")
# else: 
#     print("An empty list is false.")
# if ["spam"]: 
#     print("A nonempty list is true.")
# else: 
#     print("The empty list is false.")

# if 0: 
#     print("this will not run.")
# if 7: 
#     print("this will run.")
# if []: 
#     print("this will run.")
# if [1, 2, 99]: 
#     print("this will run.")
# if True: 
#     print("this will run.")
# if False: 
#     print("this will not run.")

cart = []

if cart:
    empty():
    