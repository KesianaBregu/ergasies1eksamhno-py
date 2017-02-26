x = raw_input ("Write ( or ), if you want to exit press Enter: ")

a = x.count("(")
b = x.count(")")
length = len(x)

if (length != a + b):
	print "invalid input"
else :
	
	if (x[0] == ')') or (x[-1]== '('):
	    print False
	elif (a == b):
		print True
	else :
		print False