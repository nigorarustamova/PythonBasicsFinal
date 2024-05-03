#ASK AKMAL AKA REGARDING THIS CODE!!!!!!!!!!!!!!!!!!!

# for i in range(3):
wish_to_continue = 'yes'
while wish_to_continue.lower() == 'yes':
    print('Welcome to our Ice Cream Shop!')
    print('You have a choice of 3 toppings:')
    topping1 = input('Please enter your first choice:')
    topping2 = input('Please enter your second choice: ')
    topping3 = input('Please enter your third choice: ')

    print(f'You have entered {topping1}, {topping2} and {topping3}.')

    available_toppings = ['chocolate', 'vanilla', 'strawberry', 'caramel']
    requested_toppings = [topping1, topping2, topping3]

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f'Adding {requested_topping}...')
        else:
    print(f"Sorry, we don't have the {requested_topping}.")

    wish_to_continue = input('Do you wish to continue? enter yes/no: ')



