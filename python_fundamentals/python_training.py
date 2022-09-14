# print("Hello World!")

# name = "Zen"
# print("My name is", name)

# name = "Zen"
# print("My name is " + name)

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# x = "hello world"
# print(x.title())
# # output:
# "Hello World"

# x = 10
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")

# class EmptyClass:
#     pass

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# ninjas.insert(2,'Ahmad')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# def addNumbers(a,b):
#     return a + b

# result = addNumbers(3,5)       #if we leave one empty it will give error cuz b is missing
# print(result)

# def addNumbers(a=0,b=0):       #can also put a = '' to fill in a string
#     return a + b

# result = addNumbers(3)       #if we leave one empty it will print 0 cuz b is 0
# print(result)


# class User:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
#         self.account=BankAccount(int_rate=0.02, balance=0)

#     def greeting(self):
#         print("welcome",self.name)

# class BankAccount:
#     def __init__(self,int_rate,balance):
#         self.int_rate=int_rate
#         self.balance=balance

# malik = User("Malik Mohanna", "malik@axsos")
# malik.account = BankAccount(0.06, 10000)
# print(malik.account.int_rate)

# saad=User("Saad Hroub","saad@axsos")
# saad.name="Saad Hroub"
# saad.age="36"                 ->error
# print(saad)
# print(saad.name)
# print(saad.age)
# print(saad.email)
# print(saad.balance)
# print(saad.account.int_rate)
# nasri=User("Nasri",20,"nasri@axsos.academy",1000000)

# print(saad.name, saad.age)
# saad.age=50
# print(saad.name, saad.age)
# print(nasri.name, nasri)




# saad.greeting()
# nasri.greeting()


string_name = "geeksforgeeks"

# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")

# Code #2
string_name = "GEEKS"

# Iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])