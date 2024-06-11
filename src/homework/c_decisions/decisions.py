ratio = 0

def get_options_ratio(options, total):
    ratio = options / total

    return ratio

def get_faculty_rating(ratio):

    if (ratio <= 1 and ratio >= .9):

        return 'Excellent'
    elif(ratio < .9 and ratio >= .8):
        return 'Very Good'
    
    elif (ratio < 0.8 and ratio >= 0.7):
        return 'Good'
    
    elif (ratio < 0.7 and ratio >= 0.6):
        return 'Needs Improvement'
    
    else:
        return 'Unacceptable'
#