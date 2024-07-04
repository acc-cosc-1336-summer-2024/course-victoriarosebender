#

def get_hamming_distance(dna1,dna2):
    dna1= dna1.upper()
    dna2 = dna2.upper()
    count = 0
    
    for i in range( 0,len(dna2)):
        if dna1[i] != dna2[i]:
            count += 1

    return count


def get_dna_complement(dna):
    dna = dna.upper()
    finish_string = ''
    for i in dna:
        if i == 'A':
            finish_string += 'T'
        elif i == 'T':
            finish_string += 'A'

        elif i == "C":
            finish_string += 'G'

        elif i == "G":
            finish_string += 'C'

    finish_string = ''.join(sorted(finish_string))

    return finish_string



def menu():
    print("Homework 5 Menu \n 1-Hamming Distance \n 2-Dna Complement \n 3-Exit")
    ##this is the menu

def user_controlled_loop(): 
    choice = 1  
    while( choice != '3'):
        menu()
        choice = input("Enter Menu Option: ")
        run_menu(choice)
        
def run_menu(choice):        
    if (choice == '1'):
        string1 = input("Give a string: ")
        string2 = input("Give another string: ")
        print(get_hamming_distance(string1,string2))
    elif (choice == '2'):
        string1 = input("Give a string: ")
        print(get_dna_complement(string1))
    elif (choice == '3'):
        print('Exiting')

    else:
        print('Invalid Input')



