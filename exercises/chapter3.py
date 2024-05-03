# exercises 3.3

cars = ['mercedes', 'toyota', 'mazda', 'bmw']
print(f'The best car is {cars[0].title()}.')
print(f'The best car is {cars[1].title()}.')
print(f'The best car is {cars[2].title()}.')
print(f'The best car is {cars[3].upper()}.')


print(25*25)

cars = ['ferrari', 'maybach', 'bmw', 'tesla', 'mercedes']
nums = [3, 5, 6, 77, 4, 5, 2, -34]

print(sorted(cars))
print(cars)
print(len(cars))

#homework: 3.8; 3.9; 3.10
cities = ['Sugarland', 'Bryn Mawr', 'Punxsutawney', 'Appleton', 'Honolulu']
print(cities)
print(sorted(cities))
sorted_cities = sorted(cities, reverse=True)
print(sorted_cities)
print(cities)
cities.reverse()
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

#3.9
guests = ['Marina', 'Nigora', 'Dilya', 'Sam', 'Blake']
print(f"{guests[1]}, we are inviting you to dinner")
print(f"{guests[0]}, we are inviting you to dinner")
print(f"{guests[2]}, we are inviting you to dinner")
print(f"{guests[3]}, we are inviting you to dinner")
print(len(guests))

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())
    print(f"Dear {magician.title()}, I invite you to our dinner party.")



