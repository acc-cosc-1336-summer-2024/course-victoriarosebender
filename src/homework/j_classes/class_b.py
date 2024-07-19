#menu here
import class_a

def menu():
    print("Homework 7 Menu \n 1-Roll Die \n 2-Exit")
    ##this is the menu

def user_controlled_loop(): 
    choice = '3' 
    while( choice != '2'):
        menu()
        choice = input("Enter Menu Option: ")
        if choice == '2':
            print("Exiting the program...")
            break
        run_menu(choice)



        
def run_menu(choice):        
        exit1 = '0'
        die = class_a.Die()

        while exit1 != '1':
            die.roll()
            roll = str(die)
            print(roll)
            exit1 = input("Press 1 when complete. Press ENTER to see another roll:")

            
        
        
        


