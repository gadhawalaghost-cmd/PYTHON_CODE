 
#                 # [DAY 1] #

# # CODE 1 / 500:

# # Ek program likho jo apna 
# # naam, age, aur city teen alag print statements mein show kare.

# name = "raza"
# age = 17
# city = "gujrat,himatnager"

# print(name)
# print(age)
# print(city)




# # CODE 2 / 500 :

# # 4 variables banao 
# # (name → string, age → int, height → float, is_student → boolean).
# # aur unka type() print karo.

# name = str("raza")
# age = int(17)
# hight = float(175.2)
# is_student = bool()

# print(type(name))
# print(type(age))
# print(type(hight))
# print(type(is_student))




# # CODE 3 / 500 :

# # User se do numbers input lo aur unka.
# # addition, subtraction, multiplication, aur division print karo.

# num1=int(input("enter your first number:"))
# num2=int(input("enter your second number:"))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)




# # CODE 4 / 500 :

# # User se ek number lo aur check karo ki wo,
# # even hai ya odd (if-else use karke).

# num= int(input("enter your number:"))

# if num %2 == 0 :
#     print(num,":your number is even")

# else:
#     print (num,":your number is odd")




# # CODE 5 / 500 :

# # for loop use karke 1 se 20 tak ke numbers print karo.

# for i in range(1,21):
#     print(i)




#                # DAY 2 #


# # CODE 6 / 500 :
# # while loop use karke 1 se 10 tak numbers print karo.
# # (for loop nahi, while use karna hai).


# count = 1

# while count <= 10:
#     print (count)
#     count += 1




# # CODE 7 / 500 :
# # Ek list banao jisme 5 fruits ke naam ho.
# #  Phir usse: (a) pehla fruit print karo,
# #  (b) last fruit print karo, 
# #  (c) list ki length print karo.


# fruits = ["apple","banana","mango","kivi","litchi"]

# print (fruits)
# print(fruits[4])
# print(len(fruits))




# # CODE 8 / 500 :
# # Ek string lo (apna naam),
# # aur ye print karo: (a) uppercase mein, (b) lowercase mein, (c) reverse karke.

# str1 = "raza"
# print(str1.upper())
# print(str1.lower())
# print(str1[ ::-1])




# # code 9 / 500 :
# # Ek function banao greet(name) jo "Hello,<name>! Welcome to Python" print kare.
# # Function ko 3 different names ke saath call karo.

# def greet(name,):
#     print("hello",name,"! welcome to python")

# greet("raza")
# greet("ayan")
# greet("akib")




# CODE 10 / 500 :
# User se marks (0-100) input lo aur grade print karo:
# 90+ → "A"
# 75-89 → "B"
# 50-74 → "C"
# 50 se kam → "Fail"



marks = int(input("enter your marks out of 100:"))

if marks >= 90:
    print("GRADE A")

elif marks >= 75:
    print("GRADE B")

elif marks >= 50:
    print("GRADE C")

elif marks <= 50:
    print("SORRY YOU HAVE NOT CLEAR THIS EXAM, YOUR FAIL!")