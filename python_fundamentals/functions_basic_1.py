#1
def a():
    return 5
print(a())      #prints 5

#2
def a():
    return 5
print(a()+a())  #prints 5+5=10

#3
def a():
    return 5
    return 10
print(a())      #prints 5

#4
def a():
    return 5
    print(10)
print(a())      #prints 5

#5
def a():
    print(5)    #prints 5
x = a()
print(x)        #prints 5

#6
def a(b,c):
    print(b+c)  #prints 1+2=3 then prints 2+3=5
print(a(1,2) + a(2,3))

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))               #prints 25

#8
def a():
    b = 100
    print(b)        #prints 100
    if b < 10:
        return 5
    else:
        return 10
        return 7
        print(a())

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))       #prints 7
print(a(5,3))       #prints 14
print(a(2,3) + a(5,3))      #prints 7+14=21

#10
def a(b,c):
    return b+c 
    return 10
print(a(3,5))   #prints 3+5=8

#11
b = 500
print(b)        #first print  =  500
def a():
    b = 300
    print(b)    #3rd print after the call =  300
print(b)        #second =   500
a()             #gets called after second
print(b)        #4th print =   500

#12
b = 500
print(b)        #first print  =  500
def a():
    b = 300
    print(b)     #3rd print after the call =  300
    return b
print(b)        #second  =  500
a()             #gets called after second
print(b)        #4th print =  500 cuz b doesnt get saved

#13
b = 500
print(b)        #first print   = 500
def a():
    b = 300
    print(b)    #3rd print after the call =  300
    return b
print(b)        #second  =  500
b=a()           #returns b as 300
print(b)        #4th print =  300

#14
def a():
    print(1)    #prints 1 first cuz it starts with a
    b()         #b gets called secondly
    print(2)    #prints 2 secondly after b call
def b():        #after b call it comes here
    print(3)    #prints 3 after b call
a()    #gets called first cuz indentation

#15
def a():        #6.comes here after a call
    print(1)    #7.prints 1 after a call
    x = b()     #1.calls b first thing    then x=5 cuz it returned 5 in line 116
    print(x)    #8.prints 5
    return 10   #9.returns 10
def b():        #2.comes here after b call   
    print(3)    #3.prints 3 first thing
    return 5    #4.returns 5
y = a()         #5.calls a after b and returns 10 as y
print(y)        #10.prints 10

