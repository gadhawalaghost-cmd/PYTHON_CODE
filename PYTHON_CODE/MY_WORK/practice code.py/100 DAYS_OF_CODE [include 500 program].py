 
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




               # DAY 2 #


# CODE 6 / 500 :

# while loop use karke 1 se 10 tak numbers print karo.
# (for loop nahi, while use karna hai).


count = 1

while count <= 10:
    print (count)
    count += 1





# CODE 7 / 500 :

# Ek list banao jisme 5 fruits ke naam ho.
#  Phir usse: (a) pehla fruit print karo,
#  (b) last fruit print karo, 
#  (c) list ki length print karo.


fruits = ["apple","banana","mango","kivi","litchi"]

print (fruits)
print(fruits[4])
print(len(fruits))





# CODE 8 / 500 :

# Ek string lo (apna naam),
# aur ye print karo: (a) uppercase mein, (b) lowercase mein, (c) reverse karke.

str1 = "raza"
print(str1.upper())
print(str1.lower())
print(str1[ ::-1])





# code 9 / 500 :

# Ek function banao greet(name) jo "Hello,<name>! Welcome to Python" print kare.
# Function ko 3 different names ke saath call karo.


def greet(name,):
    print("hello",name,"! welcome to python")

greet("raza")
greet("ayan")
greet("akib")





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





              # DAY 3 #


# CODE 11 / 500 :

# Ek list banao 1 se 10 tak numbers ki.
# Us list se: (a) sirf even numbers print karo, (b) sabka sum nikalo, (c) sabse bada number nikalo.
# (bina max() use kiye, loop se).

l1 = [1,2,3,4,5,6,7,8,9,10]
count = 0
biggest = l1 [0]

for count in l1 :
     count += 1
     if count %2 == 0:
        print (count)

for num in l1 :
    count = count + num
print (count)

for num in l1 :
    if num >= biggest:
        biggest = num
print ("largest value:",num)





# CODE 12 / 500 :

# Ek dictionary banao jisme 3 students ke naam (key) aur unke marks (value) ho.
# Phir: (a) ek student ka naam print karke uske marks nikalo, 
# (b) sabhi keys print karo, 
# (c) sabhi values print karo.

dic = {"raza":86,
       "ayan":88,
       "akib":92}

print(dic.get("raza"))
print(dic.keys())
print(dic.values())





# CODE 13 / 500 :

# User se unka naam aur age input lo,
# aur f-string use karke print karo:
# "Mera naam <naam> hai aur meri age <age> saal hai."

name = str(input("enter your name:"))
age = int(input("enter your age"))

print(f"Mera naam {name} hai aur meri age {age} saal hai.")





# CODE 14 / 500 :

# Ek function banao square(num) jo number ka square return kare (print nahi).
# Function ko call karke result ko ek variable mein store karo, phir print karo.

def square(num):
    return num ** 2

square(5)
num = square(5)
print(num)





# # CODE 15 / 500 :

# User se ek number lo aur uski multiplication table 1 se 10 tak print karo.
# (loop use karke).

num = int(input("enter your number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)





#               # DAY 4 #


# CODE 16 / 500 :

# Nested Loops — for loop ke andar for loop use karke ye pattern print karo:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()





# code 17 / 500 :

# 1 se 20 tak ke numbers ki list banao jisme sirf even numbers ho
# lekin normal loop nahi, list comprehension use karke (ek line mein).
    
even_number = [i for i in range (1,21) if i %2 == 0]
print(even_number)




# code 18 / 500 :

# Ek tuple banao jisme 5 cities ke naam ho.
# Phir: (a) 3rd city print karo, 
# (b) check karo ki "Mumbai" tuple mein hai ya nahi (in keyword use karke), 
# (c) tuple ki length print karo.

cities = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore")
print(cities[2])
print ("Mumbai" in cities)
print(len(cities))





# CODE 19 / 500 :

# Ek function banao calculate(a, b, operation)
# jo operation ke hisaab se (jaise "add", "subtract", "multiply", "divide") result return kare.
# Function ko alag-alag operations ke saath call karke test karo.

num1 = int(input(" enter firs number:"))
sum = (input("enter operation + , - , * , / , %: "))
num2 = int(input(" enter second number:"))

if sum == "+" :
    print(num1 + num2)

if sum == "-" :
    print(num1 - num2)

if sum == "*" :
    print(num1 * num2)

if sum == "/" :
    print(num1 / num2)

if sum == "%" :
    print(num1 % num2)






# CODE 20 / 500 :

# User se ek sentence input lo,
# aur count karo usme kitne words hain (hint: .split() method use hoga).

sentence = input("enter a sentence: ")
words = sentence.split()
count = len(words)
print("Number of words in the sentence:", count)





              # DAY 5 #


# CODE 21 / 500 :

# Ek dictionary banao jisme 5 items aur unki prices ho 
# (jaise {"shirt": 500, "jeans": 1200, ...}).
# Phir: (a) total sum of all prices nikalo, 
# (b) sabse mehenga item aur uski price print karo, 
# (c) ek naya item dictionary mein add karo.

items = {"shirt": 500, "jeans": 1200, "shoes": 2000, "hat": 300, "gloves": 200}

print("tottal sum of price", sum(items.values()))
print("most expensive item:", max(items, key=items.get), "with price:" ,max(items.values()))
items["socks"] = 100
print("Updated dictionary:", items)





# CODE 22 / 500 :

# User se ek word lo aur check karo ki wo palindrome hai ya nahi,
# (jaise "madam", "nan" — jo aage se ulta padho toh same rahe).

word = input("enter a word:")
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")





# CODE 23 / 500 :

# 3 students ki list banao, jisme har student ek dictionary ho 
# (naam aur marks ke saath). Phir loop use karke har student ka naam aur marks print karo.

l1 = [ {"name": "raza", "marks": 86},
       {"name": "ayan", "marks": 88},
        {"name": "akib", "marks": 92}
        ]

for student in l1 :
    print("name:", student["name"], "marks:", student["marks"])





# CODE 24 / 500 :

# User se ek number input lo aur usse 100 se divide karke result print karo.
# Agar user 0 input kare (jisse divide by zero error aayega), 
# toh try-except use karke ek proper error message print karo, program crash na ho.

num = int (input("enter your number:"))
num1 = num / 100
 
if num == 0:
    print("Error: Cannot divide by zero.")

else:
    print(num1)





# CODE 25 / 500 :

# Ek function banao power(base, exponent=2) jo base ki exponent power calculate kare.
# Agar exponent na diya jaaye, toh default square (power 2) calculate ho.
# Function ko dono tareeke se call karke test karo (with aur without exponent).

def power(base, exponent = 2):
    result = base ** exponent

    print (f"base={base} exponent={exponent} your answer is:", result )

power(5,)






              # DAY 6 #

# CODE 26 / 500 :

# Do sets banao: set1 = {1, 2, 3, 4, 5} aur set2 = {4, 5, 6, 7, 8}. 
# Phir print karo: (a) dono ka union, 
# (b) dono ka intersection (common elements),
# (c) set1 mein jo set2 mein nahi hai wo (difference).

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1 | set2
intersection = set1 & set2
different = set1 - set2

print(union)
print(intersection)
print(different)





# CODE 27 /500 :

# Ek lambda function banao jo do numbers ka sum nikale
# (normal def function nahi, lambda use karna hai).
#  Use call karke test karo.

sum = lambda a,b : a + b
print(sum(3,5))





# CODE 28 / 500:

# Ek list banao 5 random numbers ki (bina order ke, jaise [45, 12, 67, 3, 89]).
# Use sorted() function se ascending order mein sort karo,
# aur phir descending order mein bhi sort karo.

numbers = [45, 12, 67, 3, 89]

ascending_order = sorted(numbers)
descending_order = sorted(numbers, reverse=True)

print("Ascending:", ascending_order)
print("Descending:", descending_order)





# CODE 29 / 500 :
 
# User se do numbers input lo aur unhe divide karo.
# try-except use karke do alag errors handle karo:
# (a) agar user number ki jagah text daale (ValueError),
# (b) agar divide by zero ho (ZeroDivisionError).
#  Dono ke liye alag-alag error message print karo.

try :
    num1 = (int(input("enter your first number:")))
    num2 = (int(input("enter your second number:")))
    result = num1 / num2
    print("sum =:",result)

except ValueError:
    print("please enter only numbers!")
except ZeroDivisionError:
    print("devision by zero is not valid!")





# CODE 30 / 500 :

# Ek text file banao notes.txt naam ki,
# usme "Python seekhna maza aa raha hai" likho (write mode se).
# Phir usi file ko wapas read karke content print karo.

f1= open("notes.txt","w")
data = f1.write("pythone seehna maza aa raha hai")
print(data)


f2 = open("notes.txt","r")
r = f2.read()
print(r)

f1.close
f2.close
