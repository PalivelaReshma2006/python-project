# num=5+2.0
# print(num)
# num=int(num)

# print(type(num))

# message=42
# message=str(message)
# print(message)

# print(type(message))

'''ascii values'''
# char_a='A'
# ascii_a=ord(char_a)
# print(ascii_a)


# ascii_a=chr(a)
# print(ascii_a)
'''input'''

''' string indexing'''
#str="RESHMASAIPRIYA"
#print(str)
#print(str[10])
#print(str[-10])
''' string slicing'''
#str="RESHMASAIPRIYA"
#print(str)
#print(str[5:10])
#print(str[-10:-3])


''' string slicing step in'''
# str="RESHMASAIPRIYA"
# print(str)
# print(str[1::2])
# print(str[-11::-2])

'''leaf year or not'''
#year=int(input("given a year:"))
#if year%100==0 and year%400!=0:
#    print("it is a leaf year")
#elif year%4==0:
#    print("it is a leaf year")
#else:
#  print("it is not leaf year")


#   print("it is not leaf year")

# n=int(input("given a num:"))
# for i in range(1,n+1):
#     print(i)
    
# # i=1
# while i<=n:
#     print(i)
#     i+=1

# n=int(input("given a num:"))
# i=1
# while i<=n:
#     if (i%2==0):
#         print(i)
#     i+=1

# n=int(input("given a num:"))
# i=1
# while i<=n:
#     if  not(i%2==0):
#        print(i)
#     i+=1

'''odd numbers'''
# n=int(input("given a num:"))
# i=1
# while i<=n:
#     if (i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
#  '''even by using continue'''


# n=int(input("given a num:"))
# i=1
# while i<=n:
#     if not(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# n=int(input("given a num:"))
# i=1
# while i<=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1
''' 3 multiplication'''
# n=int(input("given a num:"))
# for i in range(1,10):
    # print(f"{n}*{i}={n*i}")
    

'''escape sequence'''
# s="hello\"s world"
# print(s)

# s="hello\"s\n world"
# print(s)

# n=int(input("given a num:"))
# factorial=1
# while n>0:
#     factorial*=n
#     n-=1
# print(factorial)


# l=[10,20,30,40,50]
# sum=0
# for i in l:
#     sum=+i
# print(sum)

l=[15,2,7,25,10]
# l.sort()
# print(l[0],l[-1])

max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print(max,min)
