'''strings '''
# str="PYTHON"
# print(str)
# print(str[1])
# print(str[4])
# print(str[-2])
'''(PYTHON
Y
O
O
)'''
'''string slicing'''
# str="hello world"
# print(str[2:10])
# print(str[1:-1])
# print(str[:3])
# print(str[::2])
# print(str[1::2])
# print(str[::-1])
'''(llo worl
ello worl
hel
hlowrd
el ol
dlrow olleh)'''
'''(string concatenation)'''
# name1="jhon"
# name2="doe"
# fullname=name1 +""+ name2
# print("fullname:",fullname)
'''(fullname: jhon doe
)'''
'''string length'''
# str="coding is fun!"
# print(len(str))
'''(14)'''
# str1="asdfghjklpoiuyfhhk"
# print(len(str1))
'''(18)'''
'''string methods'''
# str="Hello World!"
# print(str.upper())
# print(str.lower())
# print(str.strip())
# print(str.replace('o','l'))
# print(str.count('l'))
'''(HELLO WORLD!
hello world!
Hello World!
Helll Wlrld!
3
)'''
'''string formating'''
# name="alice"
# age=12
# print(f"Name:{name},Age:{age}",)
# print("Name:",name,",Age:",age,sep="")
'''(Name:alice,Age:12
Name:alice,Age:12)'''
'''escape sequence'''
# print("hello\'s world")
# print("hello\ns world")
# print("hello\bs world")
# print("hello\rs world")
# print("hello\vs world")
# print("hello\fs world")
'''examples'''
# str=input("enter your name:" )
# str1=str.lower()
# a=str1.count('a')
# e=str1.count('e')
# i=str1.count('i')
# o=str1.count('o')
# u=str1.count('u')
# print("number of vowels:",a+e+i+o+u)
'''(enter your name:Hello,World!
number of vowels: 3)'''
'''grade calculator'''
# mat=int(input("marks in maths:"))
# sci=int(input("marks in science:"))
# eng=int(input("marks in english:"))
# total_marks=mat+sci+eng
# avg=total_marks/3
# percentage=(total_marks/300)*100
# grade=""
# if percentage>90:
#     grade="A"
# elif percentage>80 and percentage<=90:
#     grade="B"
# elif percentage>70 and percentage<=80:
#     grade="C"
# else:
#     grade="p"
 
# print("Total Marks:",total_marks,",\nAverage Marks:",avg,",\nGrade:",grade)
'''(marks in maths:85
marks in science:90
marks in english:78
Total Marks: 253 ,
Average Marks: 84.33333333333333 ,
Grade: B)'''
'''palindrome checker'''
# s=input("enter:")
# reverse=s[::-1]
# if reverse==s:
#     print("it is palindrome",)
# else:
#     print("not a palindrom")
'''(enter:radar
it is palindrome)'''
'''largest of the three numbers'''
# lag=(input())
# x,y,z=lag.split(",")
# num1=int(x)
# num2=int(y)
# num3=int(z)
# greater=""
# if num1>num2:
#     if num1>num3:
#         greater=num1
#     else:
#         greater=num3
# elif num2>num1:
#     if num2>num3:
#         greater=num2
#     else:
#         greater=num3
# elif num3>num1:
#     if num3>num2:
#         greater=num3
#     else:
#         greater=num2
# print(greater)
'''(15,8,21
21)'''
'''leap year or not'''
# year=int(input("enter a year:"))
# leap=False

# if year%100 == 0 and year%400 != 0:
#     leap=False
# elif year%4 == 0:
#     leap=True
# else:
#     leap=False
# print(leap)
'''enter a year:2016
true'''
'''Temperature converter'''
# tem=int(input("enter temperature:"))
# units=(input("enter units(k or f or c):")).lower()
# c=32  (f->c=f*(9/5)-32),(k->c=273-k)
# f=c*(9/5)+32
# k=273+c
# if units=="c": 
#     print("Temperature in fahernheit:",f,end="f\n")
#     print("Temperature in kelvin:",k,end="k")
# elif units=="f":
#     print("temperature in celsius:",c)
#     print("Temperatur in kelvin:",k)
# else:
#     print("temperature in celsius:",c)
#     print("Temperature in fahernheit:",f)
'''(enter temperature:32
enter units(k or f or c):c
Temperature in fahernheit: 89.6f
Temperature in kelvin: 305k)'''






