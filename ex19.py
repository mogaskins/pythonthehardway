# this is the line where you define the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Defines the %d variable cheese count
	print "You have %d chesses!" % cheese_count
	# Defines the %d variable boxes of crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#these two lines will print out at the end
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
#signifies using the function and setting variables below	
print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

#calls function and uses = to fix the variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# sets the cesse and crackers variable for the last two functions
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# uses math in parenthesis to set variable
print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6)

#uses previous amount of variable and adds to the amount with math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

