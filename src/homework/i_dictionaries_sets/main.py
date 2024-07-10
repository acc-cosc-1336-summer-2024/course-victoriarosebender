#

def get_p_distance(dna1,dna2):
    dna1= dna1.upper()
    dna2 = dna2.upper()
    count = 0
    
    for i in range( 0,len(dna2)):
        if dna1[i] != dna2[i]:
            count += 1

    return count 




def get_p_distance_matrix(matrix1):
    rows = len(matrix1)
    columns = len(matrix1)
    master_matrix = []
    ##row1.append(get_p_distance(list1,list2) / len(list1))

    for i in range(1,rows):
        row_list = []
        for j in range(1,columns):
            new_val = get_p_distance(matrix1[(i+1)]*matrix1[(j+1)]) / rows
            row_list.append(new_val)
        master_matrix.append(row_list)  
    print(master_matrix)

    
get_p_distance_matrix([['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']])