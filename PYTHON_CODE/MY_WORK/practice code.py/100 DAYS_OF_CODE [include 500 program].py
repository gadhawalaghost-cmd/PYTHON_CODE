 
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






#               # DAY 7 #

# CODE 31 / 500 :

# Ek class banao Student naam ki, jisme __init__ method ho jo name aur marks set kare.
# Ek method banao display() jo student ka naam aur marks print kare.
# Class se ek object banao aur display() call karo.

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
       print("name:",self.name)
       print("marks:",self.marks)

    
s1 = student("raza",92)
s1.display()





# CODE 32 / 500 :

# Student class se ek TopperStudent class banao (inherit karke).
# jisme ek extra method ho award() jo "Congratulations, you got a medal!" print kare.
# Object banake dono methods (display() aur award()) call karo.

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
       print("name:",self.name)
       print("marks:",self.marks)

class Topperstudent(Student):

    def award (self,):
        print("congratulations, you got a medal!")

topper = Topperstudent("raza",92)
topper.award()
topper.display()





# CODE 33 / 500 :

# 1 se 10 tak numbers ki ek dictionary banao jisme key = number aur value = uska square ho
# — dictionary comprehension use karke (ek line mein), normal loop nahi.

square = {num: num ** 2 for num in range(1,11)}
print(square)





# CODE 34 / 500 :

# Ek function banao total_sum(*args) jo jitne bhi numbers diye jaayein,
# unka sum return kare (chahe 2 numbers ho ya 10). 
# Function ko alag-alag counts ke numbers se call karke test karo.

def total_sum (*args):

    total = 0
    for num in args:
        total = total + num
    return total
    
print(total_sum(2, 3))
print(total_sum(1, 2, 3, 4, 5))
print(total_sum(10))





# CODE 35 / 500 :

# Ek custom exception class banao NegativeNumberError (jo Exception se inherit kare).
# Ek function banao check_number(num) jo agar number negative ho toh ye custom exception raise kare,
# warna number print kare. 
# try-except use karke isse handle karo.

class negativenumbererror(Exception):
    pass

def check_number(num):
    if num < 0 :
        print("negative numbers are not allowed !!")

    else :
         print(num)

try:

    check_number(-5)

except negativenumbererror as e:
    print("error granted:", e)






#               # DAY 8 #


# CODE 36 / 500 :

# Student class use karo (Day 7 wali).
# 3 students ke objects banao alag-alag marks ke saath. 
# Ek loop likho jo teeno students mein se sabse zyada marks wale student ka naam print kare.

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
       print("name:",self.name)
       print("marks:",self.marks)

    
s1 = student("raza",92)
s2 = student("ayan",88)
s3 = student ("akib",90)

students = [s1 , s2, s3]

topper = students[0]

for student in students :
    if student.marks > student.marks:
        topper = student

print("the top 1 is :",topper.name)





# CODE 37 / 500 :

# Ek function banao student_info(*args, **kwargs) jo args ke andar diye gaye normal values print kare,
# aur kwargs ke andar diye gaye key-value pairs bhi print kare.
# Function ko is tarah call karo: student_info("Raza", 25, city="Himatnagar", course="Python").

def student_info(*args,**kwargs):
    print("args value:")

    for value in args:
        print("-",value)

    print("kwargs values:")
    for key,value in kwargs.items() :
        print("-", key,":",value)

student_info("raza",25, city="himatnager", course="python")





# CODE 38 / 500 :

# Ek function banao factorial(n) jo recursion use karke (loop nahi) kisi number ka factorial nikale.
# (Hint: factorial(5) = 5 * factorial(4), aur factorial(0) = 1.)

def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))





# CODE 39 / 500 :

# Ek function banao jo user se ek number input le aur usse 10 se divide kare.
# try-except-finally use karo — except mein ValueError handle karo,
# aur finally block mein hamesha "Process complete hua" print karo (chahe error aaye ya na aaye).

def devided_by_ten():

    try:
     num = int(input("enter your number:"))
     result = 10 / num
     print("result:",result)

    except ValueError:
     print("only numbers are allowd! ")

    except ZeroDivisionError:
      print("number zero are not allowd!")

    finally:
     print("process done.")

devided_by_ten()





# CODE 40 / 500 :

# User se ek sentence lo.
# Us sentence se: (a) saare vowels (a, e, i, o, u) count karo, 
# (b) sentence ko title case mein convert karo (.title()), 
# (c) check karo sentence mein koi number hai ya nahi (.isdigit() ya digit check karke).

sentence = (input("enter your sentence:"))

vowels = "AEIOUaeiou"
vowels_count = 0

for char in sentence:
    if char in vowels:
        vowels_count =+ 1

title_case = sentence.title()

has_digit = False
for char in sentence:
    if char.isdigit():
        has_digit = True


print("vowels count:",vowels_count)
print("titel:",title_case)
print("numbers in sentence:",has_digit)





#               # DAY 9 #


# CODE 31 / 500 :

# Ek dictionary banao jisme keys students ke naam ho, 
# aur values list ho unke 3 subjects ke marks.
# (jaise {"Raza": [80, 90, 85], "Aman": [70, 75, 60]}).
#  Loop use karke har student ka naam aur unke marks ka average print karo.

std_details = {
    "Raza":[80,90,85],
    "Aman":[70,75,60],
    "riya":[80,93,89]
}

for name, mark_list in std_details.items():
    total = 0
    for marks in mark_list:
        total = total + marks
    average = total / len(mark_list)
    print(name,"average:",average)






# CODE 32 / 500 :

# Ek list banao 5 fruits ki.
# enumerate() use karke print karo har fruit uske index ke saath (jaise "Index 0: Apple").

l1 = ["apple","banana","litchi","kivi","mango"]

for index , fruite in enumerate(l1):
    print("index:",index ,"fruit:",fruite)





# CODE 33 / 500 :

# Do lists banao — ek names ki, 
# ek marks ki (dono same length ki). 
# zip() use karke dono lists ko combine karke print karo (jaise "Raza scored 85").

name = ["raza","ayan"]
marks= [88,88]

for name , marks in zip(name,marks):
    print(name, "your score is:",marks)





# CODE 34 / 500 :

# Ek list banao 1 se 10 tak numbers ki.
# map() use karke har number ka square nikalo (naya list banao), 
# phir filter() use karke us squared list mein se sirf 50 se bada numbers nikalo.

number = list(range(1,11))

square = list(map(lambda x : x**2,number))
print("square is:",square)

filter = list(filter(lambda x : x >50,square))
print("geather then 50:", filter)





# CODE 35 / 500 :

# Ek class banao BankAccount jisme __init__ mein balance set ho (starting 0).
# Do methods banao: deposit(amount) jo balance badhaye,
# aur withdraw(amount) jo balance ghataye (agar balance kam ho toh "Insufficient balance" print kare). 
# Object banake test karo — deposit aur withdraw dono try karo.

class BenkAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("deposit is :", amount)
        print("new balance :",self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient belance!")

        else:
            self.balance = self.balance - amount
            print("withdraw is :",amount)
            print("new belence :",self.balance)

account = BenkAccount()
account.deposit(1000)
account.withdraw(500)
account.withdraw(1000)






#               # DAY 10 #


# CODE 36 / 500 :

# Ek class banao ToDoList jisme __init__ mein ek empty list tasks ho. 
# 3 methods banao: add_task(task) (task list mein add kare), 
# remove_task(task) (task list se hata de), 
# aur show_tasks() (saare tasks print kare). 
# Object banake teeno test karo.

class ToDOList :

    def __init__(self):
        self.task = []
        pass

    def add_task(self,task):
        self.task.append(task)
        print("adding action on task...")
        print(task)

    def remove_task(self,task):
        if task in self.task:
             self.task.remove(task)

        else:
            print("item not in list")
        print("removing task..")
        print(task)

    def show_task(self):
        print("task showing...")
        for task in self.task:
            print("--",task)

my_list = ToDOList ()
my_list.add_task("learning pythone")
my_list.add_task("going to gym")
my_list.add_task("playing sports")

my_list.show_task()

my_list.remove_task("going to gym")

my_list.show_task()





# CODE 37 / 500 :

# Ek dictionary banao product ka naam aur price ke saath.
# (jaise {"name": "Shirt", "price": 499.5}).
# F-string use karke print karo: "Shirt ki price hai ₹499.50" — 
# price 2 decimal places tak honi chahiye (hint: :.2f format specifier).

shope_item = {
    "name" : "shirt",
    "price" : 400.5
}

print(f"{shope_item["name"]} price are : {shope_item["price"]:.2f}")





# CODE 38 / 500 :

# 4 students ki list banao, har student ek dictionary (naam aur marks). 
# sorted() function use karke, key parameter ke saath, 
# list ko marks ke hisaab se descending order mein sort karo.

student = [
    {"name": "raza","marks" : 92},
    {"name": "ayan","marks" : 97},
    {"name": "akib","marks" : 91},
    {"name": "priya","marks" : 90}
]

sorted_student = sorted(student, key=lambda student: student["marks"], reverse = True)
for student in sorted_student:
    print(student["name"],"-",student["marks"])





# CODE 39 / 500 :

# Ek Calculator class banao jisme ek method divide(a, b) ho.
# Agar b zero ho, custom exception raise karo. 
# Agar a ya b string ho (number nahi), TypeError handle karo. 
# try-except se dono cases test karo.


class DivisionByZeroError(Exception):
    pass

class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise DivisionByZeroError("devided by zero are not allowd!")
        result = a / b
        return result

calc = Calculator()


try:
    print(calc.divide(10, 2))
except DivisionByZeroError as e:
    print("Custom Error:", e)
except TypeError:
    print("Sirf numbers hi do, text nahi!")


try:
    print(calc.divide(10, 0))
except DivisionByZeroError as e:
    print("Custom Error:", e)
except TypeError:
    print("Sirf numbers hi do, text nahi!")


try:
    print(calc.divide(10, "abc"))
except DivisionByZeroError as e:
    print("Custom Error:", e)
except TypeError:
    print("Sirf numbers hi do, text nahi!")





# # CODE 40 / 500 : 

# Ek simple "Student Grade System" banao: 
# Dictionary mein 5 students ke naam aur marks ho. 
# Function banao jo (a) sabka average nikale, 
# (b) sabse zyada marks wala student batae, 
# (c) har student ka grade calculate kare (A/B/C/Fail, jaisa Day 4 mein seekha tha).

students = {
    "Raza": 85,
    "Aman": 92,
    "Priya": 45,
    "Karan": 78,
    "Neha": 60
}

def calculate_average(students):
    total = 0
    for marks in students.values():
        total = total + marks
    average = total / len(students)
    return average

def find_topper(students):
    topper_name = ""
    topper_marks = 0
    for name, marks in students.items():
        if marks > topper_marks:
            topper_marks = marks
            topper_name = name
    return topper_name, topper_marks

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# --- Sab kuch use karke dikhana ---

avg = calculate_average(students)
print("Class ka average:", avg)

name, marks = find_topper(students)
print("Topper:", name, "-", marks, "marks")

print("\nHar student ka grade:")
for name, marks in students.items():
    grade = get_grade(marks)
    print(name, "-", marks, "marks -> Grade:", grade)





#               # DAY 11 #

# CODE 41 / 500 :

# BankAccount class use karo (Day 9 wali). 
# Usse SavingsAccount naam ki class banao jo inherit kare, 
# aur __init__ mein ek extra attribute interest_rate add kare (using super().
# __init__() parent ka __init__ call karne ke liye). 
# Ek method banao add_interest() jo balance mein interest amount add kare (balance * interest_rate / 100).

class BenkAccount :

    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance = self.balance - amount

class SAvingAccount(BenkAccount):

    def __init__(self,intrest_rate):
        super().__init__()
        self.intrest_rate = intrest_rate

    def add_interest(self):
        interest_ammount= self.balance * self.intrest_rate / 100 
        self.balence = self.balance + interest_ammount
        print("intrest ammount is :",interest_ammount)
        print("new balence : ", self.balance)

saving = SAvingAccount(5)

saving.deposit(1000)
print("balance after deposit :", saving.balance)

saving.add_interest()





# CODE 42 / 500 :

# Ek list banao 1 se 20 tak numbers ki. 
# Slicing use karke print karo: (a) pehle 5 elements, 
# (b) last 5 elements, 
# (c) har alternate (dusra) number (index 0, 2, 4...).


numbers = list(range(1,21))

five_numbers = numbers[0:5]
last_numbers = numbers[-5:]
alternate_numbers = numbers[0::2]

print("first 5:", five_numbers)
print("Last 5:", last_numbers)
print("Alternate:", alternate_numbers)





# CODE 43 / 500 :

# Ek generator function banao even_numbers(limit).
# jo yield use karke 1 se limit tak ke saare even numbers ek-ek karke generate kare,
# (list return nahi karna, yield use karna hai). Use for loop se call karke print karo.

def even_numbers(limit):
    for num in range(1,limit + 1):
        if num %2 == 0:
            yield num

for num in even_numbers(20):
    print(num)
    





# CODE 44 / 500 :

# Ek dictionary banao jisme ek company ka data ho — company ka naam, 
# aur ek list of dictionaries (employees, har employee ka naam aur salary). 
# Loop use karke: (a) sabhi employees ke naam print karo, 
# (b) total salary (sabka sum) calculate karo.

company_data = {
    "company_name":"google",
    "employes" : [
        {"name":"raza","salary":50000},
        {"name":"ayan","salary":45000},
        {"name":"akib","salary":55000}
        ]
}

print("company name : ",company_data["company_name"])

print("\nall employees : ")
for employes in company_data["employes"]:
    print("-",employes["name"])

total_salary = 0
for employes in company_data["employes"]:
    total_salary = total_salary + employes["salary"]

print("\ntotal salary : ",total_salary)





# CODE 45 /  500 :

# Ek simple decorator function banao timer_info jo kisi bhi function ke call hone se pehle,
# "Function shuru ho raha hai..." aur baad mein "Function complete ho gaya" print kare. 
# Ek simple function (jaise greet()) banao aur usse @timer_info decorator se decorate karo.

def timer_info(func):
    def wrapper ():
        print("function starting...")
        func()
        print("function complited.")
    return wrapper

@timer_info
def greet():
    print("hello, raza!")

greet()





#               # DAY 12 #


# CODE 46 / 500 :

# Ek class banao Rectangle jisme __init__ mein length aur width set ho. 
# Ek @property method banao area jo automatically length × width calculate kare, 
# (bina brackets () ke call ho, jaise rect.area, na ki rect.area()).

class rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width

    @property
    def area (self,):
        return self.length * self.width


rect = rectangle(10,5)
print(rect.area)





# CODE 47 / 500 :

# Do classes banao Flyable (ek method fly() jo "Can fly" print kare) 
# aur Swimmable (ek method swim() jo "Can swim" print kare). 
# Ek class Duck banao jo dono se inherit kare. 
# Object banake dono methods call karo.

class flyable:
    def fly(self):
        print("can fly")

class swimmeble:
    def swim(self):
        print("can swim")

class duck(flyable,swimmeble):
    pass


bird = duck()
bird.fly()
bird.swim()





# CODE 48 / 500 :

# File Handling Advanced — File se data read karke, 
# uske total lines count karo aur total words count karo (poori file ka), 
# with statement use karke (jaise Day 6 mein seekha tha).

with open(r"C:\git_repo\PYTHONE_CODE\PYTHON_CODE\MY_WORK\practice code.py\notes.txt","w") as f :

    f.write("it's Amaizing to learn python\n")
    f.write("my second line\n")
    f.write("my third line\n")

with open(r"C:\git_repo\PYTHONE_CODE\PYTHON_CODE\MY_WORK\practice code.py\notes.txt","r") as f :
    content = f.read()

lines = content.split("\n")
lines = [line for line in lines if line != "" ]

total_line = len(lines)

words = content.split()
total_words = len(words)

print("total lines :",total_line)
print("total words :", total_words)





# CODE 49 / 500 :

# Ek function banao jo try-except ke andar ek error catch kare, 
# phir usi error ko ek custom message ke saath dobara raise kare,
# (raise keyword dobara use karke, except block ke andar).

def zerodivision (num):
    try:
        result =10 / num

    except ZeroDivisionError:
        raise ZeroDivisionError ("you cant calculate with zero!")

try:
    zerodivision(0)

except ZeroDivisionError as e:
    print("error founded... \n",e)





# CODE 50 / 500 :
 
# Ek class banao MathHelper jisme ek @staticmethod ho add(a, b),
# jo dono numbers ka sum return kare — is method ko object banaye bina, 
# seedha MathHelper.add(5, 3) se call karo.


class MathHelper:
    @staticmethod

    def add (a,b):
        return a+b


result = MathHelper.add(5,3)
print(result)





#               # DAY 13 #


# CODE 51 / 500 :

# Student class use karo. 
# Ek @classmethod banao from_string(cls, data_string) jo ek string jaise "Raza,85" ko le kar 
# (comma se split karke) naam aur marks nikale, 
# aur ek naya Student object bana kar return kare. 
# Object ko Student.from_string("Raza,85") se banao.

class student:

    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls,data_string):
        name,marks = data_string.split(",")
        marks = int(marks)
        return cls (name,marks)

s1 = student("raza,93")
print(s1.name)
print(s1.marks)





# CODE 52 / 500 :

# Student class mein ek __str__ method add karo jo object ko print() karte waqt,
# ek proper readable string dikhaye (jaise "Student: Raza, Marks: 85") — 
# normal object print karne se <__main__.Student object at 0x...> jaisa ajeeb output aata hai, 
# __str__ isse fix karta hai.

class student:

    def __init__(self,name,marks,):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"student: {self.name},marks : {self.marks}"

s1 = student("raza", 93)
print(s1)






# CODE 53 / 500 :

# Ek class banao Point jisme x aur y coordinates ho. 
# __add__ method banao jisse do Point objects ko + operator se jod sakein 
# (jaise p1 + p2 se naya Point ban jaye jisme x aur y dono add ho jayein).

class point :
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.x + other.y
        return point(new_x,new_y)

    def __str__(self):
        return f"point {self.x},{self.y}"

p1 = point(5,11)
p2 = point(6,12)

p3 = p1 + p2 

print(p3)





# CODE 53 / 500 :

# Ek class banao CountUpTo jo limit leta ho, 
# aur for loop mein use hone par 1 se limit tak numbers ek-ek karke de 
# (bina yield ke — __iter__ aur __next__ methods use karke).

class CountUpTo:

    def __init__(self,limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__ (self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current = self.current + 1
        return value


counter = CountUpTo(5)

for num in counter:
    print (num)





# CODE 55 / 500 : 

# abc module use karke ek abstract class banao Shape jisme ek abstract method area() ho 
# (jo khud kuch na kare, bas define ho). 
# Do classes banao Circle aur Square jo Shape se inherit karke apna-apna area() implement karein.

from abc import ABC, abstractmethod

class shape (ABC):
    @abstractmethod
    def area (self):
        pass

class circle (shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side* self.side

c1 = circle(5)
s1 = square(4)

print("circle area :" ,c1.area())
print("square are :" ,s1.area())





#               # DAY 14 #

# CODE 56 / 500 :

# Rectangle class use karo (Day 12 wali).
# area ko @property banao jaise pehle. Ab ek naya property length banao jisme ek @length.setter bhi ho 
# — jo check kare ki naya length negative na ho 
# (agar negative diya toh error message print kare, warna update kare).


class Rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width

    @property
    def length (self,):
        return self._length

    @length.setter
    def length (self,value):
        if value < 0:
            print("you coud not take nagative value (-)")

        else:
            self._length = value

    @property
    def area (self):
        return self._length * self.width

rect = Rectangle(10, 5)
print(rect.area)

rect.length = 20
print(rect.area)

rect.length = -5
print(rect.area)





# CODE 57 / 500 :

# Ek class banao FlexibleData jisme __init__(self, *args, **kwargs) ho-
# jo bhi normal values di jayein args mein store ho, 
# jo bhi named values di jayein kwargs mein store ho. 
# Ek method show() banao jo dono print kare.

class FlexibleData:
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def show(self):
        print("args =",self.args)
        print("kwargs =",self.kwargs)

data = FlexibleData("raza",25, city="himatnagar",cource="python")
data.show()





# CODE 58 / 500 :

# Ek class banao StringBuilder jisme text empty string se shuru ho. 
# Methods banao add(word) (text mein word jode) aur upper() (text ko uppercase kare), 
# dono methods self return karein taaki tum builder.add("hello").add(" world").upper() jaise chain kar sako.

class StringBuilder:

    def __init__(self):
       self.text = ""

    def add(self,word):
        self.text = self.text + word
        return self

    def upper(self):
        self.text = self.text.upper ()
        return self

builder = StringBuilder()
result = builder.add("hello").add(" world").upper()

print(result.text)





# CODE 59 / 500 :

# Ek custom class banao FileOpener jo with statement ke saath use ho sake,
# (jaise with FileOpener("notes.txt") as f:),
# __enter__ aur __exit__ methods use karke — bina Python ke built-in open() ke with support ke, 
# apna khud ka banao.

class FileOpener:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File khul gayi")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File band ho gayi")


with FileOpener("notes.txt", "w") as f:
    f.write("Python seekhna maza aa raha hai")

with FileOpener("notes.txt", "r") as f:
    content = f.read()





# CODE 60 / 500 :

# Ek "Library System" banao: Book class (naam, author, available status), 
# aur Library class jisme books ki list ho. 
# Methods: add_book(book), borrow_book(name),
# (agar available ho toh status False karo, warna "Not available" print karo), 
# return_book(name) (status True karo).

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.name, "library mein add ho gayi")

    def borrow_book(self, name):
        for book in self.books:
            if book.name == name:
                if book.available:
                    book.available = False
                    print(name, "issue ho gayi")
                else:
                    print(name, "abhi available nahi hai")
                return
        print(name, "library mein hai hi nahi")

    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                book.available = True
                print(name, "wapas aa gayi")
                return
        print(name, "library mein hai hi nahi")


# --- Test karo ---
library = Library()

b1 = Book("Python Basics", "Raza")
b2 = Book("Data Science", "Aman")

library.add_book(b1)
library.add_book(b2)

library.borrow_book("Python Basics")
library.borrow_book("Python Basics")   # dobara try karo, available nahi hogi

library.return_book("Python Basics")
library.borrow_book("Python Basics")   





#               # DAY 15 #

# CODE 61 / 500 :

# enum module use karke ek Enum class banao Status jisme values ho PENDING, ACTIVE, COMPLETED. 
# Ek function banao check_status(status) jo Enum ke basis pe alag message print kare.

from enum import Enum

class Status (Enum):

    PENDING = 1
    ACTIVE = 2
    COMPLETED = 3

def check_satatus(status):
    if status == status.PENDING:
        print("your work is pending...")

    elif status == status.ACTIVE:
        print("your work is activated...")

    elif status == status.COMPLETED:
        print("your work is complite.")

check_satatus(Status.ACTIVE)





# CODE 62 / 500 :

# Ek class banao StringUtils jisme 3 @staticmethod ho: 
# is_palindrome(text), count_vowels(text), reverse_text(text). 
# Object banaye bina, seedha StringUtils.method_name(...) se test karo.

class StringUtils:

    @staticmethod
    def is_palindrome(text):
        return text == text[ :: -1]

    @staticmethod
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count = count + 1
        return count

    @ staticmethod
    def revers_text(text):
        return text [ :: -1]


print(StringUtils.is_palindrome("madam"))
print(StringUtils.count_vowels("hello world"))
print(StringUtils.revers_text("pythone"))





# CODE 63 / 500 :

# Ek class banao Car jiske andar ek nested class ho Engine (jisme horsepower attribute ho). 
# Car ke __init__ mein ek Engine object banao aur use self.engine mein store karo. 
# Object banake car.engine.horsepower access karo.

class Car:
    class Engine:
        def __init__(self,horsepower):
            self.horsepower = horsepower

    def __init__(self, name,horsepower):
            self.name = name
            self.engine = self.Engine(horsepower)

car = Car("honda city ",120)

print(car.name)
print(car.engine.horsepower)





# CODE 64 / 500 :

# Point class use karo (Day 13 wali). 
# Ek __eq__ method add karo jisse do Point objects ko == se compare kar sako 
# (jaise p1 == p2 check kare ki dono ke x aur y same hain ya nahi).

class point :
    def __init__ (self,x,y):
        self.x = x
        self.y = y


    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    

    def __str__(self):
        return f"point {self.x},{self.y}"

    

p1 = point(5,11)
p2 = point(6,12)
p3 = point(12,13)

print(p1 == p2)
print(p1 == p3)






# CODE 65 / 500 :

# Mini Project 3 
# — Ek "Inventory Management System" banao: 
# Product class (naam, price, quantity). 
# Inventory class jisme products ki list ho. 
# Methods: 
# add_product(), 
# total_value() (sabhi products ki price × quantity ka sum), 
# low_stock(threshold) (jo products threshold se kam quantity ke hain unke naam print kare).

class product:
    def __init__ (self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class inventory:
    def __init__(self):
        self.product = []

    def add_product(self,product):
        self.product.append(product)

    def total_value(self):
        total = 0
        for product in self.product:
            total += product.price * product.quantity
        return total

    def low_stock(self,threshold):
        print(f"products with quantity less then {threshold}:")
        found = False

        for product in self.product:
            if product.quantity < threshold:
                print(product.name)
                found = True

        if not found:
                print("no low stock product found.")


inventory = inventory()


inventory.add_product(product("Laptop", 50000, 5))
inventory.add_product(product("Mouse", 500, 20))
inventory.add_product(product("Keyboard", 1500, 3))
inventory.add_product(product("Monitor", 12000, 2))

print("tottal inventory values : ", inventory.total_value())

inventory.low_stock(5)