''' input statements'''
# name=input()
# print("enter your name:",name)
''' string input'''
# name=input("enter your name:")
# print("enter your name:",name)
'''int input()'''
# num=input()

# num1=(int(num))
# print(type(num1))
# print(num1)
# num=int(input("enter:"))
# print(type(num))
'''float input()'''
# num=float(input("enter:"))
# print(type(num))
'''example'''
# name=input("enter your name:")
# age=input("enter your age:")
# print("hello,"+name +"!you are",age,"years old")
'''Error handling'''
# num=int(input("enter a value:"))
# print(num)
# name=input()
# print("enter your name:",name)
# print(type(name))
'''output statements'''
# a=input("enter a value:")
# b=input("enter b value:")
# print(a,b)
# a=input("enter a value:")
# b=input("enter b value:")
# print(a,b, a,b,sep=",",end="!")
# name=input("enter u name:")
# print("Hello",name,sep=", ",end="!")
'''examples'''
# a=int(input( " enter a number:"))
# print("you entered:",a,sep="")
# a=float(input( " enter pi:"))
# print("value of pi:",a,sep="")
'''(enter pi:3.14
value of pi:3.14)'''
# a=int(input( " enter a number:"))
# b=int(input( " enter b number:"))
# c=int(input( " enter c number:"))
# num=a+b+c
# print("sum of inputs:",num,sep="")
'''output(enter a number:10
 enter b number:20
 enter c number:30
sum of inputs:60)'''
# a=(input("enter:"))
# x,y,z=a.split(" ")
# sum=int(x)+int(y)+int(z)
# print("sum of inputs:",sum,sep="")
'''(enter:10 20 30
sum of inputs:60)'''
# inp=input("enter name and age:")
# name,age=inp.split(",")
# print("Name:",name,",Age:",age,sep="")
'''(enter name and age:jhon,25
Name:jhon,Age:25)'''
# a =int(input("enter:"))
# print("countdown:5 4 3 2 1", end=" Blast off!")
'''(enter:5
countdown:5 4 3 2 1 Blast off!)'''
# a=(input("enter:"))
# b,c=a.split(",")
# sum=int(b)+int(c)
# print("addition:",sum ,sep="")
'''(enter:10,5
addition:15)'''
# a=(input("enter:"))
# x,y=(input("enter:")).split(",")
# a=int(x)
# b=int(y)
# print("addition:",b+a,"subtraction:",b-a)
'''(enter:10,5
addition: 15 subtraction: -5)'''
# x,y=(input("enter:")).split(",")
# a=int(x)
# b=int(y)
# print("10>5:",a>b,",10<5:",a<b ,sep="")
'''(enter:10,5
10>5:True,10<5:False)'''
'''formating output using f-string'''
# x,y=input("enter name and age:").split(",")
# print(f"Name:{x},Age:{y} years")
'''enter name and age:alice,5
Name:alice,Age:5 years'''
# a,b=input("enter:").split(",")
# print("true and false:",a and b,",true or false:",a or b, ",not true:",b,sep="")
'''(enter:true,false
true and false:false,true or false:true,not true:false)'''
# a,b,c=input("enter:").split(",")
# print("you entered:",c,sep="")
'''(enter:Yes,YES,yEs
you entered:Yes)'''
