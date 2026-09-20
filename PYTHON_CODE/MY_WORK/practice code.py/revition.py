# a= int(input("first number:"))
# b= int(input("second number:"))
# c= int(input("third number:" ))
# d= int(input("fourth number:" ))

# if (a >= b and a >=c and a>=d):
#     print("first number is greatest:")

# elif (b >=c and b>=d):
#     print("second number is greatest:")

# elif (c >=d):
#     print("third number is greatest:")

# else:
#     print("fourth number is greatest:")

def total_sum (*args):

    total = 0
    for num in args:
        total = total + num
    return total
    
# print(total_sum(2, 3))
print(total_sum(1, 2, 3, 4, 5))
# print(total_sum(10))