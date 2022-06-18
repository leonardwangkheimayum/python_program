# # Task 1
# #Q1.Find the given number is odd or even(if)
# #Q2.Reverse the number(while loop)
# #Q3.Find the given years is leap year.(if)
#
# #Q1 Code:
# # a=int(input("Enter a number"))
# # if(a%2==0):
# #     print("The Number is even")
# # else:
# #     print("The Number is Odd")
# #Q2 code
# a=int(input("Enter a number"))
# reversed=0
# while(a>0):
#         remainder=a%10
#         reversed=reversed*10+remainder
#         a= a//10
#     print("Reverse of the number:",reversed)
# #----------------------------
#q3 code
# n=int(input("Enter number: "))
# reversed=0
# while(n>0):
#     remainder=n%10
#     reversed=reversed*10+remainder
#     n=n//10
# print("Reverse of the number:",reversed)

#q3 CODE
# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")

    #TEST 1
# count=0
# amount=10000
# while(amount<20000):
#     print("amount",amount)
#     amount=amount+amount*0.07
#     count=count+1
# print(count)
# for a in range(10):
#     print(a)
# for a in range(11,20):
#     print(a)
# for a in range(10,20,2):
#     print("a",a)
# for a in range (100,20,-2):
#     print(a)
a="python"
for i in a:
    print(i)
print(a[::-1])