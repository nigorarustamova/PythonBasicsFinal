

rivers = {'nile': 'egypt',
          'amudaryo': 'uzbekistan',
          'firat': 'turkey',
          'kongo': 'kongo',
          'volga': 'russia',
          'mtkyari': 'georgia'
          }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print('*******The list of rivers we have in the list: ***********')
for river in rivers:
    print(river.title())

print('*******The list of countries we have in the list: ***********')
for country in rivers.values():
    print(country.title())

#6.6 Homework, read Chapter 6 and 7

nums = [3, 6, 1, 10, 6]
for num in nums:
    if num > 6:
        print('I got the number:', num)
    else:
        print('next')


age = 5



if age < 4:
    print('KID: Your ticket price is $4.')
elif age < 16:
    print('TEEN: Your ticket price is $10.')
elif age > 65:
    print('SENIOR: Your ticket price is $12.')
else:
    print('REGULAR: Your ticket price is $16')

print('\n****************')
age = 0
if age < 0:
    print('invalid entry')
elif age > 150:
    print('invalid entry')
elif age < 10:
    print('Your ticket price(kids): $4')
elif age < 18:
    print('Your ticket price (teens): $10')
else:
    print('Your ticket price(regular: $15')

meals = ['plov', 'chuchvara', 'khonim', 'samsa', 'kebab']
drinks = ['coke', 'chai', 'water', 'coffee', 'juice']

for meal in meals:
    for drink in drinks:
        print(f'You can have {meal.title()} with {drink}.')
    print('----------------------------')

for i in range(1,11):
    for j in range (1, 11):
        print(f'{i} * {j} = {i*j}', end='\t\t')
        print( )

for i in range(0):
    num_str = input('enter the number:')
    num = int(num_str)
    if num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 15 == 0:
        print('fizzbuzz')
    else:
        print('not dividable')

student1 = {'name': 'john', 'city': 'brooklyn'}
student2 = {}

print(student1['name'].title())
print(student1['city'].title())

print('Update or assign a new value, adding new key-value pair:')
student1['city'] = 'manhattan'
print('updated city:', student1['city'].title())

student1['country'] = 'USA'
print(student1)

student1['classes'] = ['sql', 'linux', 'python']
print(student1)
student1.update({'city': 'brooklyn'})
print(student1)

student1['grades']=[8,9,10]
print(student1)

for i in range(1,100):
    if i % 5 == 0:
        continue
    print(i)


nums = [3, 11, 5, 2, 33, 3, 5, 111, 5, 22]
#go through the numbers and count the 5s in this list
#loop through

cnt = 0
for num in nums:
    if num == 5:
        cnt = cnt + 1
print(f'total number of 5s: {cnt}')

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}
favorite_languages['nigora'] = 'sql'
favorite_languages['adam'] = 'linux'
print(f'Favorite languages poll should be taken by:')
print(favorite_languages.keys())

for name in favorite_languages.keys():
    print(f'{name.title()}, thank you for taking the poll')

cities = {
    'New York': {'population': '9 mln',
                 'country': 'USA',
                 'fact': 'Big Apple'},
    'London': {'population': '6mln',
               'country': 'UK',
               'fact': 'rainy'},
    'Dubai': {'population': '3.4 mln',
              'country': 'UAE',
              'fact': 'expensive'},
    'Rome': {'population': '3 mln',
             'country': 'Italy',
             'fact': 'historical'}
}

print(f'New York has 9 million population and located in the USA, fun fact: "Big Apple"')
print('---------------------------------------------')
for city, info in cities.items():
    print(f'{city.title()} has {info['population']} population and located in {info['country'].upper()}, fun fact: {info['fact'].title()}')

#h-w: 8.1, 8.2

def greet_user(username):
    """Display a simple greeting!"""
    print(f'Hello, {username.title()}! It is so good to see you here.')

greet_user('nigora')

def display_message():
    "Display a simple message"
    print(f'In this chapter, we are learning about defining functions. I wonder if every student is struggling to grasp it as much as I am.')

display_message()

def favorite_book(title):
    """Display a user's favorite book title."""
    print(f'One of my favorite books is {title.title()}.')

favorite_book("A man's search for meaning")

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'Prince')
describe_pet('cat', 'Molly')

print