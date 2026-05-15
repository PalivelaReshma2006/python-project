'''(loops)'''
'''Types'''
'''while loop'''
# candies=10
# while candies>0:
#     print("gives to friend")
#     candies-=1
# print(candies)
'''(gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
0)'''
'''for loop'''
# candies=10
# for i  in range(0,candies):
#     print("gives to friend")
# print(candies)
'''(gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
gives to friend
10)'''
'''for loop for sequence'''
message="hello world!"
# for i in message:
#     print(i)
'''(h
e
l
l
o
 
w
o
r
l
d
!
)'''
# length=len(message)
# for i in range(length):
#     print(i)
# print("total lenght:",length)
'''(0
1
2
3
4
5
6
7
8
9
10
11
total lenght: 12)'''
'''Nested loops'''
# for i in range(1,6):
#     for j in  range(1,11):
#         # print(i*j=(i*j))
#         print(f"{i}*{j}={i*j}")
'''(1*1=1
1*2=2
1*3=3
1*4=4
1*5=5
1*6=6
1*7=7
1*8=8
1*9=9
1*10=10
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30
4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36
4*10=40
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50)'''
'''break statement'''
# candies=10
# for  i in range(candies):
#     print("give to a friend!")
#     if  candies-i==5:
#         print("only five candies left,save it")
#         break
# print(candies)
'''
give to a friend!
give to a friend!
give to a friend!
give to a friend!
give to a friend!
give to a friend!
only five candies left,save it
10'''
# candies=10
# for  i in range(candies):
#     print("give to a friend!")
#     if  candies-i==5:
#         print("only five candies left,skip it")
#         continue
# print("giving a candy")
'''(give to a friend!
give to a friend!
give to a friend!
give to a friend!
give to a friend!
give to a friend!
only five candies left,save it
give to a friend!
give to a friend!
give to a friend!
give to a friend!
giveing a candy)'''
'''examples'''
# N=int(input("enter:"))
# i=1
# while i<=N:
#     print(i)
#     i+=1#i=i+i
# for i in range(1,N+1):
#     print(i)
'''(enter:5
1
2
3
4
5)'''
# N=int(input("enter:"))
# i=1
# sum=0
# while i<=N:
#     sum=i+sum
#     i+=1
# print("sum of N:",sum)
'''(enter:5
sum of N: 15)'''
'''n=10 print even numbers'''
# N=int(input("enter:"))
# i=1
# while i<=N:
# #     if i%2==0:
#     if not (i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
n=int(input("enter:"))
for i in range(1,n+1):
    if (i%2==0):
        print(i)
'''(enter:10
2
4
6
8
10)'''
'''n=10 print odd numbers'''
# n=int(input("enter:"))
# i=1
# while i<=n:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1
# n=int(input("enter:"))
# for i in range(1,n+1):
#     if not(i%2==0):
#         print(i)


'''(enter:10
1
3
5
7
9)'''
''' mulitiplication table of a number'''
# n=int(input("enter:"))
# for i in range(n,n+1):
#     print("mutiplication of 3:")
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
# i=1
# while i<=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1
# print("mutiplication of 3:")
# for i in range(1,11):
    
#     print(f"{n}*{i}={n*i}")
'''(enter:3
mutiplication of 3:
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30)'''
'''calculate the factorial of the number'''
# n=int(input("enter:"))
# factorial=1
# while n>0:
#     factorial=factorial*n
#     n-=1
# print("factorial of 5:",factorial)
'''(enter:5
 factorial: 120)'''