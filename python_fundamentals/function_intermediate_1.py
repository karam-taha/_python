# import random
# def randInt(min=0, max=100):
#     num = random.random()
#     return num
# print(random.randint(0,100)) 		# should print a random integer between 0 to 100
# print(random.randint(0,50)) 	# should print a random integer between 0 to 50
# print(random.randint(50,100)) 	# should print a random integer between 50 to 100
# print(random.randint(50,500))    # should print a random integer between 50 and 500

import random
def randInt(min=0, max=50):
    num = round(random.random()*max+min)
    return num
print(randInt(50))		# should print a random integer between 0 to 100
print(randInt()) 	# should print a random integer between 0 to 50
print(randInt(50,50)) 	# should print a random integer between 50 to 100
print(randInt(50,450))    # should print a random integer between 50 and 500

