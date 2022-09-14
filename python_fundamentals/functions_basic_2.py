# #1.Countdown
# countArray = []
# def countdown(num):
#     for x in range(num, -1, -1):
#         countArray.append(x)
#     print(countArray)
# countdown(5)

# #2.Print and Return
def print_and_return(num1,num2):
    print(num1)
    return (num2)
print_and_return(5,3)

#3.First Plus Length
# sum=0
# def first_plus_length(array):
#     sum=array[0] + len(array)
#     print(sum)
# first_plus_length([1,2,3,4,5])

#4.Values Greater than Second 
# def values_greater_than_second(list): 
#     maxlist=[]
#     if(len(list)<2):
#         return False 
#     max=list[1]
#     for x in range(len(list)): 
#         if(list[x]>max): 
#             maxlist.append(list[x]) 
#     return maxlist
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

#5.This Length, That Value
# def length_and_valu(size,value):
#     list=[]
#     for x in range(size):
#         list.append(value)
#     return list
# print(length_and_valu(4,7))
# print(length_and_valu(6,2))