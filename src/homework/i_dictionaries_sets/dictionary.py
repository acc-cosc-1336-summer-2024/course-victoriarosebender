#


def get_p_distance(dna1,dna2):

    count = 0
 
    for i in range(len(dna2)):
        if dna1[i] != dna2[i]:
            count += 1
    
    final = count / len(dna2)
    
    final = float(final)

    return final




def get_p_distance_matrix(matrix1):
    rows = len(matrix1)
    columns = len(matrix1)
   


    

    master_matrix = []
    ##row1.append(get_p_distance(list1,list2) / len(list1))

    for i in range(0,rows):
        row_list = []
        for j in range(0,columns):
            list1 = matrix1[i]
            list2 = matrix1[j]
            new_val = float(get_p_distance(list1,list2)) 
            row_list.append(new_val)
        master_matrix.append(row_list)  
    return master_matrix


def menu():
    print("Homework 6 Menu \n 1-Get p distance matrix \n 2-Exit")
    ##this is the menu

def user_controlled_loop(): 
    choice = 1  
    while( choice != '2'):
        menu()
        choice = input("Enter Menu Option: ")
        run_menu(choice)
        
def run_menu(choice):        
    if (choice == '1'):
        matrix1 = []

        print("Type your matrix line by line.")
        list1 = input("Give a matrix as a string, no commas, apostrophes, or spaces: ")
        list1 = list(list1)
        matrix1.append(list1)
        print("""Type 1 when complete with matrix""")
        exit1 = 0
        while exit1 != '1':
            list2 = input("Give a matrix as a string, no commas, apostrophes, or spaces: ")
            list2 = list(list2)
            matrix1.append(list2)
            exit1 = input("Press 1 when complete. Press ENTER to add another line:")
        
        
        print(get_p_distance_matrix(matrix1))

    elif (choice == '2'):
        print('Exiting')

    else:
        print('Invalid Input')
