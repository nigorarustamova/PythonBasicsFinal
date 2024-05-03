# define functions as steps to login

def enter_username(username):
    print("******* Login Page ****************")
    uname = input('Enter your username: ')
    print(f"You entered {uname}")

def enter_password():
    pword = input('Enter your password: ')
    print(f"You entered ********{pword[-2:]}")

def click_logi ():
    print("Login was clicked")