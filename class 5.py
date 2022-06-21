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
a=[1,24,52,65]
firstindex=a[0]
totalsum=0,sum=0
for i in a:
    if (i > firstindex):
        firstindex = i
print(firstindex)
print("Max",firstindex)
for i in a:
    if (i <firstindex):
        firstindex = i
print(firstindex)
print("Min",firstindex)

for i in a:
    print(i)
    totalsum=i+sum
    print(totalsum)