import decisions

# Get input from the user
options_input = input("Enter the value for options: ")
total_input = input("Enter the value for total: ")


 #convert inputs
options = float(options_input)
total = float(total_input)


ratio = decisions.get_options_ratio(options, total)

rating = decisions.get_faculty_rating(ratio)

print(rating)