#write code function here


def get_factorial(num):
    
    result = 1
    for i in range(1,num+1):
        result *= i

    return result

def sum_odd_numbers(num):

    val = 1
    sum = 0

    while val <= num:
    
        sum = sum + val
    
        val += 2

    return sum

def menu():
    print("Homework 3 Menu \n 1-Factorial \n 2-Sum odd numbers \n 3-Exit")


def user_controlled_loop(): 
    choice = 1  
    while( choice != '3'):
        menu()
        choice = input("Enter Menu Option: ")
        run_menu(choice)
        
def run_menu(choice):        
    if (choice == '1'):
        option_1()
    elif (choice == '2'):
        option_2()
    elif (choice == '3'):
        print('Exiting')

    else:
        print('Invalid Input')
        




def option_1(num):
        num = input("Give a number:")
        num = int(num)
        if num > 0 and num < 10:
            print(get_factorial(num))
        
  
def option_2():
        num = input("Give a number:")
        num = int(num)
        if num > 0 and num < 100:
            print(sum_odd_numbers(num))
    




