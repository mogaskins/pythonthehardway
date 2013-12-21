from sys import argv

# need to give the computer a user name to run. 
# example: python ex14.py Monique

# script, user_name, housemate = argv

blahblah = argv[0]
user_name = argv[1]
housemate = argv[2]

#the prompt is what shows up while the computer 
#waits for an answer. I changed it to 'well??? '
# '>' is blank
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, blahblah)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Do you live with %s" % housemate
response = raw_input(prompt)
print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
And you live with %s."
""" % (likes, lives, computer, housemate)
