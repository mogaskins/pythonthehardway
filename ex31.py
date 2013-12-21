print "You enter a dark room with two doors.  Do you go through door #1, door #2, or door #3?"


door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Ouch!"
	elif bear == "2":
		print "The bear eats your legs off. Ouch!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
if door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Ouch!"
	else:
		print "The insanity rots your eyes into a pool of much. Ouch!"
		
if door >= "3":
	print "It's very dark in here. What else is in here?"
	print "1. A ghost! Yikes!"
	print "2. A very soft and comfortable bed. Good night moon."
	
	darkness = raw_input("? ")
	if darkness == "1" or darkness =="2":
		print "You are getting very sleepy."
	else:
		print "Lights out princess."
		
