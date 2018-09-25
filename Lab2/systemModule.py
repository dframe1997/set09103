import sys

print "The first argument in the sys.argv variable is the name of the program. In this case: "
print sys.argv[0]

def plural():
	if len(sys.argv)-1 > 1: return "s" 
	else: return ""

if len(sys.argv) > 1:
	print "You added " + str(len(sys.argv)-1) + " arguement" + plural() + "."
else:
	print "Try to add an arguement!" 

