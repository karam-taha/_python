# #1.Biggie Size 
# def biggie_size(list):
#     for x in range(len(list)):
#         if list[x]>0:
#             list[x]="big"
#     print (list)
# biggie_size([-1, 3, 5, -5])

#2.Count Positives
# def count_positives(list):
#     Counter=0
#     for x in range(len(list)):
#         if list[x]>0:
#             Counter+=1
#     list[len(list)-1] = Counter
#     print(list)
# count_positives([-1,1,1,1])

#3.Sum Total
# def sum_total(list):
#     sum=0
#     for x in range(len(list)):
#         sum+=list[x]
#     print(sum)
# sum_total([1,2,3,4]) 

#4.Average
# def average(list):
#     sum=0
#     for x in range(len(list)):
#         sum+=list[x]
#         avg=sum/len(list)
#     print(avg)
# average([1,2,3,4])

#5.Length
# def length(list):
#     print(len(list))
# length([37,2,1,-9])

#6.Minimum 
# def minimum(list):
#     min=list[0]
#     for x in range(len(list)):
#         if min>(list[x]):
#             min=list[x]
#     print(min)
# minimum([37,2,1,-9])

#7.Maximum 
# def maximum(list):
#     max=list[0]
#     for x in range(len(list)):
#         if max<(list[x]):
#             max=list[x]
#     print(max)
# maximum([37,2,1,-9])

# #8.Ultimate Analysis 
# def ultimate_analysis(list):
#     sum=0
#     min=list[0]
#     max=list[0]
#     for x in range(len(list)):
#         if max<(list[x]):
#             max=list[x]
#         if min>(list[x]):
#             min=list[x]
#         sum+=list[x]
#         avg=sum/len(list)
#     thisdict={'sumTotal':sum,'average':avg,'minimum':min,'maximum':max,'length':len(list)}
#     print (thisdict)
# ultimate_analysis([37,2,1,-9,2,7,1,20])

#9.Reverse List
# def reverse_list(list):
#     x=0
#     y=len(list)-1
#     while(x<y):
#         list[x],list[y]=list[y],list[x]
#         x+=1
#         y-=1
#     print (list)
# reverse_list([37,2,1,-9])


#if i have to return instead of printing (list) whats the correct way to do that