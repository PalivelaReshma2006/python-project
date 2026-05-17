'''dictionary'''
# dict={1:"a",2:"b"}
# dict[3]="c"
# # dict[1]="c" {1: 'c', 2: 'b', 3: 'c'}
# d=dict[2]
# print(d)
# print(dict[1])
# print(dict)
# '''methods'''
# print(dict.get(1))
# # print(dict.pop(1))
# print(dict)
# print(dict.items())
# print(dict.values())
# print(dict.keys())
'''(b
a
{1: 'a', 2: 'b', 3: 'c'})'''
'''loops in dictionary'''
# dict={1:"a",2:"b"}
# for  i in dict.values():
#     print(i)
# for  i,j in dict.items():
#     print(i,j)
# for  i in dict.keys():
#     print(i)
'''(a
b
1 a
2 b
1
2)'''
'''examples'''
'''find the sum of all elements in a given list of numbers'''
# l=[10,20,30,40,50]
# sum=0
# for i in range(0,5):
#     sum=sum+l[i]
# # for i in l:
# #     sum=sum+i
# print("sum:",sum)
# 
# l=[10,20,30,40,50]
# sum=0
# i=1
# length=len(l)
# while i<length:
#     sum=sum+l[i]
#     i+=1
# # for i in l:
# #     sum=sum+i
# print("sum:",sum)
'''(sum: 150)'''
'''find the maximum and minimum values in a list of numbers'''
# l=[15,2,7,25,10]
# maxi=l[0]
# mini=l[0]
# for i in l:
#     if i>maxi:
#         maxi=i
#     if i<mini:
#         mini=i
# print(l)
# l.sort()
# print(l[-1],l[0])
'''(25 2)'''
'''remove duplicate elements from a list to create a new  list with unique elements'''
'''[10,20,30,20,40,10,50]'''
# inp=input().split(",")
# l=[int(item)for item in inp]
# newl=[]
# for i in l:
#     if i in newl:
#         continue
#     else:
#         newl.append(i)
# print(newl)
# inp=input().split(",")
# l=[int(a)for a in inp]
# s=set(l)
# newl=list[s]
# print(newl)
'''([10, 20, 30, 40, 50])'''
'''list[{40, 10, 50, 20, 30}]'''
'''count the number of occurrences of a specific element in a list'''
# inp=input().split(",")
# l=(int(item)for item in inp)
# l=(int(item)for item in input().split(","))
# n=int(input())
# count=0
# for i in l:
#     if i==n:
#         count+=1
# print(count)
# c=l.count(n)
# print(c)

'''(1,2,3,2,1,4,2,5
2
3)'''
'''given two stes ,find their intersection (common elements ) and union (all unique elements combined) '''
# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s_1=s1.intersection(s2)
# s_2=s1.union(s2)
# print("intersection:",s_1)
# print("union:",s_2)
'''(intersection: {4, 5}
union: {1, 2, 3, 4, 5, 6, 7, 8})'''
''' create dictionaries,access values,update values,and iterate through key -value pairs'''
# mydict={"name":"jhon", 
#         "age":30,
#         "city":"New york"}
# mydict["age"]=31
# for i,j in mydict.items():
#     print(i,j)
# mydict={}
# name=input("enter name:")
# age=int(input("enter age:"))
# city=input("enter city:")
# mydict["name"]=name
# mydict["age"]=age
# mydict["city"]=city
# '''update'''
# mydict["age"]=20
# print(mydict)
'''(enter name:jhon
enter age:19
enter city:chennai
{'name': 'jhon', 'age': 20, 'city': 'chennai'})'''
'''list concatenation'''
l1=[1,2,3]
l2=[4,5,6,]
com=l1+l2
print(com)
'''[1, 2, 3, 4, 5, 6]'''