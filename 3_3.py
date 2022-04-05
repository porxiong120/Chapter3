
# this is a infinite loop 
#i = 0 # iterator / incrementor
#while True:   
 #   i = i + 1
  #  print("Hello World!" + str(i))


# from urllib import response


#num = 0 # iterator / incrementor 
#while num <= 5: 
#    print("Hello World! " + str(num))
#    num += 1 # i = i + 1

#print("This program displays a famous movie quotation.")
#responses = ('1', '2', '3')
#response = '0'
# loop will cotinue if it is satisfy
#while response not in responses: # false condition
#    response = input("Enter 1, 2, or, 3: ")
#    if response =='1':
#        print("Plastics.")
#    elif response == '2':
#        print("Rosebud.")
#    elif response == '3':
#        print("That's all folks.")


# count = 0 
# total = 0

# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number: ")) #5
# min = num 
# max = num 
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num 
#     if num > max:
#         max = num 
#     num = eval(input("Enter a nonnegative number: "))

# if count > 0:
#     print("Minimum:", min)
#     print("Maximum:", max)
#     print("Average:", total / count)
# else:
#     print("No nonnegative numbers were entered.")



# count = 0 
# total = 0
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number: ")) #5
# min = num 
# max = num 
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num 
#     if num > max:
#         max = num 
#     num = eval(input("Enter a nonnegative number: "))
# if count > 0:
#     print("Min:", str(min))
#     print("Max:", str(max))
#     print("Average:", str(total / count))
# else:
#     print("No nonnegative numbers were entered.")


# count = 0 
# numbers = []
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number: ")) #5
# numbers.append(num)
# while num != -1:
#     count += 1
#     num = eval(input("Enter a nonnegative number: "))
# if count > 0:
#     print("Min:", str(min))
#     print("Max:", str(max))
#     print("Average:", str(total / count))
# else:
#     print("No nonnegative numbers were entered.")

# # (examples)

# list1 = [300, 1, 2, 3, 60]
# list1.sort() # [1, 2, 3, 60, 300]

# list1[0] # 1 - lowest number in the list
# list1[-1] # 300 - largest number in the lsit

# # example 4 

# list1 = []
# print ("(Enter -1 to terminate entering numbers.)")


# example 5 

# number_of_years = 0
# balance = eval(input("Enter initial deposit: "))
# while balance < 1000000:
#     balance += .04 * balance
#     number_of_years += 1
# print("In", number_of_years, "years you will have a million dollars.")


# i = 0
# balance = eval(input("Enter initial deposit: "))
# while balance < 1000000:
#     balance += .04* balance # balance = (balance * .04)
#     i += 1
# print("In ", str(i), " years you will have a million dollars.")


# i = 0
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 1000000:
#     balance += .04* balance # balance = (balance * .04)
#     i += 1
# print("In ", str(i), " years you will have a million dollars.")


# i = 0
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 1000000:
#     break
#     balance += .04* balance # balance = (balance * .04)
#     i += 1
# print("In ", str(i), " years you will have a million dollars.")

list1 = []
while True:
    num = eval(input("Enter a nonnegative nubmer: "))
    if num == -1:
        break 
    list1.append(num)

print(list1)