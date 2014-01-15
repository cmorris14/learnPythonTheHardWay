my_name = 'Zed A. Shaw'
my_age = 35.
my_height = 74.0 # inches
my_weight = 180.0 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# %s used for formatting Strings; %d, decimal used for integers; %r can be used to force, no matter what

# Example:
# name = 'marcog'
# number = 42
# print '%s %d' % (name, number)
# prints 'marcog 42'

my_height_cm = my_height * 2.54
my_height_m = my_height_cm / 100
my_weight_kg = my_weight / 2.2

print "Height in centimetres: %d" % my_height_cm
print "Height in meters: %d" % my_height_m
print "Weight in kilograms: %d" % my_weight_kg