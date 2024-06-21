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
    choice = input("Homework 3 Menu \n 1-Factorial \n 2-Sum odd numbers \n 3-Exit")

def choice == 1:
        num = input("Give a number:")
        num = int(num)
        if num > 0 and num < 10:
            get_factorial(num)
        else:
            num = input("Give a number:")
            num = int(num)
            
            
        print("Exit?")

    elif choice == 2:
        num = input("Give a number:")
        num = float(num)
        print("Exit?")

    elif choice == 3:
        print("Continue?")
        print("Exit?")

    




