#

def get_hamming_distance(dna1,dna2):
    
    count = 0
    
    for i in range( 0,len(dna2)):
        if dna1[i] != dna2[i]:
            count += 1

    return count


def get_dna_complement(dna):
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



