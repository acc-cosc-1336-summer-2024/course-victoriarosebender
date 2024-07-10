#

def get_p_distance(dna1,dna2):

    count = 0
    
    for i in range( 0,len(dna2)):
        if dna1[i] != dna2[i]:
            count += 1
    count = int(count)
    return count 




def get_p_distance_matrix(matrix1):
    rows = len(matrix1)
    columns = len(matrix1)
    length = len(matrix1[0])

    print(length)

    

    master_matrix = []
    ##row1.append(get_p_distance(list1,list2) / len(list1))

    for i in range(0,rows):
        row_list = []
        for j in range(0,columns):
            list1 = matrix1[i]
            list2 = matrix1[j]
            new_val = int(get_p_distance(list1,list2)) / length
            row_list.append(new_val)
        master_matrix.append(row_list)  
    return master_matrix

    
