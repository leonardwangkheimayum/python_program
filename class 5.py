# a=[1,2,4]#list mutable
# a.append(45)
# print(a)
# b=[7,9,10]
# a.extend(b)
# print(a)
# a.insert(-1,95)#indexing
# print(a)
# print(a[4:6])#slicing
# print(a[4:])#slicing
# print(a[:4])
# del a[-1]
# print(a)
# del a[4:7]
# print(a)
# a.remove(45)#value
# print(a)
# a.pop(2)#index
# print(a)
#find max and min length and sum without using inbuilt function of list
# a=[1,24,52,65]
# firstindex=a[0]
# totalsum=0
# sum=0
# for i in a:
#     if (i > firstindex):
#         firstindex = i
# print(firstindex)
# print("Max",firstindex)
# for i in a:
#     if (i <firstindex):
#         firstindex = i
# print(firstindex)
# print("Min",firstindex)
#
# for i in a:
#     totalsum=i+totalsum
#
# print(totalsum)

# #Q1 Create a=[123,232,123,123] for your task is to find the last index of 123 and how many occurence of 123.
# a=[123,232,123,123 ,"lion","rabbit","lion"] #a=[]
# x="rabbit"
# count=0
# print(a[-1])
# for ele in a:
#     if(ele==x):
#         count=count+1
# print("{}has occured {}".format(x,count))
# # create a=[123,"","","",] remove the occurence of double quote or white space
# a=[123,"","",""]
# while("" in a):
#     a.remove("")
# print(a)
# ABC input output wil be ZYX
# a=[]
# for i in range(65,91):
#     a.append(chr(i))
# print(a)
# # T=input("enter the word")
# T="ABCD"
# for i in T:
#     if(i in a):
#         b=a.index(i)
#         print(a[25-b],end="")
#
# #Python123 seperate word and number
# a="Python123"
# word=""
# number=""
# for i in a:
#     if(i.isdigit):
#         number=number+i
#     else:
#         word=word+i
# print(word)
# print(number)
# a=["a","b","c"] a should be replace with b and b=c ,c=c.

# a=2
# for i in range(1,11,1):
#     product=2*i
#     print(product)
#
#Dictionary
a={"name":"Pillu","Age":23,"Blood Group":"A"}
a["Address"]="Uripok"
print(a)
a["name"]="Leonard"
print(a)
del a["name"]
print(a)
a.pop("Age")
print(a)
a.popitem()
print(a)
print(a.keys())
print(a.values())
print(a.items())