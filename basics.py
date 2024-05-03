nums = [4, 2, 90, 33, 5]
print(nums)

print('first element of nums:', nums[0])
print('first element of nums:', nums[-5])
print('last element of nums:', nums[4])
print('last element of nums:', nums[-1])
print('third element of nums:', nums[2])

print("********* 'U' Updating the elements ***************")
countries = ['italy', 'spain', 'japan', 'uk', 'usa']
countries[2] = 'china'
print("After the change:", countries)
countries.append("Uzbekistan")
print("after the append", countries)
countries.insert(0, 'France')
print("after inserting the value to the beginning of the list", countries)















print('******** 'U' Updating the elements ************')
countries = ['italy', 'france', 'usa', 'china', 'russia']
print(countries)
countries[1]='uzbekistan'
print('after the change:', countries)
countries.insert(0, 'UK')
print('after inserting to the beginning of the list:', countries)
countries.append('Belgium')
print('after appending to the end of the list:', countries)
del countries[3]
print(countries)
countries.pop()
print(countries)


guests = ['Marina', 'Nigora', 'Dilya', 'Adkham', 'Shokir']
for i in guests:
    print(f'We are inviting you, dear {guest} to our dinner celebration.')
print(f"{guests[1]}, we are inviting you to dinner")
print(f"{guests[0]}, we are inviting you to dinner")
print(f"{guests[2]}, we are inviting you to dinner")
print(f"{guests[3]}, we are inviting you to dinner")
print(f"{guests[4]}, we are inviting you to dinner")


print(f"Unfortunately, {guests[4]} cannot make it to dinner,")
guests[4] = 'Trevor'
print(f"but we are excited to have {guests[4]} instead.")
guests.append('Eddie')
(print(f"{guests[5]}, we are inviting you to dinner"))
print(guests)
del guests[2]
print(guests)





cars = ['toyota', 'ferrari', 'lexus', 'ford', 'bmw']
print(cars)
cars.sort()
print(f"Cars in ascending order: {cars}")
cars.sort(reverse=True)
print(f"Cars in descending order: {cars}")

guests = ['Marina', 'Nigora', 'Dilya', 'Adkham', 'Shokir']
print(f"{guests[1]}, we are inviting you to dinner")
print(f"{guests[0]}, we are inviting you to dinner")
print(f"{guests[2]}, we are inviting you to dinner")
print(f"{guests[3]}, we are inviting you to dinner")
print(f"{guests[4]}, we are inviting you to dinner")




cars = ['toyota', 'lexus', 'ford', 'bmw', 'ferrari']
for i in cars:
    print(f"I like my {i}")





guests = ['sophia', 'annie', 'benjamin', 'prince', 'khalid', 'ansar']
for guest in guests:
    print(f"Hello my lovely {guest}. I cannot wait to meet you!")
    print(len(guests))


print("**** range (100, 121, 2")
for i in range(100, 121, 2):
    print(f'number in this iteration: {i}')

nums=list(range(100, 121, 2))
for num in nums:
    print (num**2)

print("***************")
for num in range(10):
    print(num)


print("************")
for i in range (10):
    print(f"*********** outer loop: {i} *******")
    for j in range(5):
        print(f"inner loop: {j} ")

print("++++++++++++++++++++++++")

for num1 in range(1,11):
    for num2 in range(1,11):
        print(f"{num2} * {num1} = {num2 * num1}", end='\t\t\t\t')
    print()



players = ['charles', 'marina', 'florence', 'steve', 'eli']
for i in range(len(players)):
    print({i})
    print(f"you are still invited {players[0]}")
    del players[-1]
    print(f"you are still invited: {players}")

print(f'\new{players}')

print("**************")
def hello():
    print(f"Hello, World Function!")
hello()

print('1-19: odd numbers')
for i in range(1,20,2):
    print(i)

print('new line:')
cubes = []
for val in range (1,11):
    cube = val ** 3
    cubes.append(cube)
    print(cube)
print(cubes)


print("My favorite pizzas")
pizzas = ['Pepperoni', "Chicken", "Quattro Formaggi", "Pesto"]
my_favorite_pizzas = pizzas[:]
pizzas.append("Buffalo")
my_favorite_pizzas.append("Fancy")
print("My favorite pizzas are:")
for pizza in pizzas:
    print("-" + pizza)
print("My friend's favorite pizza's are:")
for pizza in my_favorite_pizzas:
    print("-" + pizza)

countries = ['usa', 'uk', 'canada', 'france', 'uzbekistan']
for country in countries:
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())

countries = ['usa', 'uk', 'canada', 'france', 'uzbekistan']
if countries==[]:
    print('List is not empty')
else:
    print('list is empty')


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

msg='hello'
print(msg)
print(int(100/3))

print("result:", 5**3)

num1 = 20
num2 = 2
print('modulo:', num1 % num2)

print(9//2)

print('25' + '30')

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

numbers = []
students = ['Alex', 'Ali', 'Anna', 'Elvin']

print(students[1])
print(f'Second student in the list: {students[1]}')
print(students[-2].upper())

students.append('Stella')
print(students)
students.insert(2, 'mansur')
print(students)
students.insert(3, 'nigora')
print(students)

del students[-1]
print(students)
students.pop(-2)
print(students)

students = ['ali', 'ali', 'dima', 'vlad', 'jim']
students.remove('ali')
print(students)
print("******************")
students = ['ali', 'ali', 'dima', 'vlad', 'jim']
students.remove('vlad')
print(students)




print(25*25)