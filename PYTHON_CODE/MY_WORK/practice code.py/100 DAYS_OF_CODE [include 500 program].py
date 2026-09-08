 
                # [DAY 1] #

# CODE 1 / 500:

# Ek program likho jo apna 
# naam, age, aur city teen alag print statements mein show kare.

name = "raza"
age = 17
city = "gujrat,himatnager"

print(name)
print(age)
print(city)




# CODE 2 / 500 :

# 4 variables banao 
# (name → string, age → int, height → float, is_student → boolean).
# aur unka type() print karo.

name = str("raza")
age = int(17)
hight = float(175.2)
is_student = bool()

print(type(name))
print(type(age))
print(type(hight))
print(type(is_student))




# CODE 3 / 500 :

# User se do numbers input lo aur unka.
# addition, subtraction, multiplication, aur division print karo.

num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)




# CODE 4 / 500 :

# User se ek number lo aur check karo ki wo,
# even hai ya odd (if-else use karke).

num= int(input("enter your number:"))

if num %2 == 0 :
    print(num,":your number is even")

else:
    print (num,":your number is odd")




# CODE 5 / 500 :

# for loop use karke 1 se 20 tak ke numbers print karo.

for i in range(1,21):
    print(i)