x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# Call x and y to be displayed
print "I said: %r." % x
print "I also said: '%s'." % y
# Initiate boolean variable hilarious, give value 'false'
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# print joke_evaluation variable (string), call value of hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e