# #1.Basic
for x in range(0,151,1):
    print(x)

# #2.Multiples of Five
for x in range(5,1001,5):
    print(x)

# #3.Counting, the Dojo Way
for x in range(1,101,1):
    if x%10== 0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)

#4.Whoa, That Sucker's Huge
sum = 0
for y in range(0,500000):
    if y % 2 != 0:
        sum += y
print(sum)

#5.Countdown by fours
for x in range (2018,0,-4):
    print(x)

#6.Flexible Counter
lowNum=0
highNum=9
mult=3
for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)