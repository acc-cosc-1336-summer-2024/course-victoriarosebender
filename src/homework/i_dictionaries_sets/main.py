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
