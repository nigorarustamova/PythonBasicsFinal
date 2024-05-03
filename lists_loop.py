# Looping

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
     print(magician.title())
print("******this is repeatable line*******")

nums = [3, 5, 1, 8]
#print list of square of these numbers
squares = [] #mutable: can be changed
coordinates = (10, 30) #tuple: immutable: you can not change
for num in nums:
     print('calculating the square:', num)
     #print(i**2)
     squares.append(num**2)
print(squares)

cars = ['tesla', 'mercedes', 'toyota']
for car in cars:
     print(f'I love my {car.title()}!')
print("end of the dream *******")

pizzas = ['quattro formagi', 'pesto', 'margherita', 'buffalo']
for pizza in pizzas:
     print(f'I like {pizza} pizza.')
print("I love having kebabs for lunch from Greece restaurant.")


for value in range(1,5): #generate numbers starting from 1 up to 5 (not including 5), incrementing by 1
     print(value)

for num in range(10): #starting from 0 up to 10, incrementing by 1
     print(num)

for num in range (5, 30, 3): #starting from 5 up to 30, increementing by 3
     print(num, end='\t')


print('\nodd numbers:', end='\t')
for num in range (11, 20, 2):
     print(num, end='\t')

squares =[]
for num in range(10,20,2):
     print(num**2, end='\t')
     squares.append(num**2)
print('squares of even numbers from 10 to 20:', squares)



print('find min and max from the given unsorted list without using min or max functions:')
nums = [4, -22, 2005, 105, 55]
nums.sort()
print(f"min: {nums[0]} and max: {nums[-1]}")

squares = [value*2 for value in range(1,11)]
print(squares)

# H/W: 4-3--4-8
# 4-3 Counting to twenty:
for num in range(1,21):
     print(num)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
     if car == 'bmw':
          print("This is the real beast:", car.upper())
     else:
          print(car.title())


nums = [3, 6, 1, 10, 6]
for num in nums:
     if num == 6:
          print("I got the number:", num)
     else:
          print('next', num)


rivers = {'dnepr': 'ukraine', 'mississippi': 'usa', 'amazon': 'brasil', 'volga': 'russia'}
for river, country in rivers.items():
     print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
     print(f"The name of the river is: {river.title()}")

for country in rivers.values():
     print(f"The name of the country is: {country.title()}")


for num in nums:
     if num < 6:
          print('I got the number:', num)
     else:
          print('next')

age = 25
if age < 4:
     print('You can have a free ice cream! Yay!')
elif age < 16:
     print('Congratulations! You get 50% off on admission')
else:
     print(f"You need to pay full price. Sucks to be an adult, doesn't it?")

age = 3

if age < 4:
     print('Your ticket price is $4')


# h/w: build if logic:
# print fizz  when number is dividable by 3
#print buzz when number is dividable by 5
#print fizzbuzz when number is dividable by 15

num = 3
if num % 3 == int:
     print('fizz')
elif num % 5 == int:
     print('buzz')
elif num % 15 == int:
     print('fizzbuzz')
else:
     print('not dividable')


nums = [3, 11, 5, 2, 33, 3, 5, 111, 5, 22]
cnt = 0
for num in nums:
     if num == 5:
          cnt = cnt + 1
       #   cnt +=1       #in python, it means increment by one
       #   cnt -=1       #in python, it means decrease by one
print(f'total number os 5s: {cnt}')


# Homework: 8.3 - 8.5

#Functions: blocks of code designed to do one specific job
#parameter: a piece of information the function needs to do its job
#argument: a piece of information that's passed from a function to call to a function

def ahmet():
     """Display a simple personal message""" #dockstring
     print("Nice guy!")

ahmet()

#8.3 - 8.5
def make_shirt(size, message):
     "Make a shirt with a message"
     print(f"I need a size {size.upper()} T-shirt that says {message}")

make_shirt('L', "I love Python." )
make_shirt('m', 'I am a pro coder.')

def make_shirt():
     print(f'I need a size L shirt that displays the message: I love Python')

make_shirt()

def describe_city(city, country):
     print(f'{city.title()} is in {country.upper()}.')

describe_city('London', 'UK')
describe_city('New York', 'USA')
describe_city('quebec', 'canada')


def add(x,y):
     c = x+y
     return c


result = add(5,10)
print(result)

def hello(name, age, country=''):









