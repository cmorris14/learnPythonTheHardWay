tabby_cat = "\tI'm %r in." % "tabbed" # %r puts '' around. %s does not
persian_cat = "I'm split\non a line."
backslash_cat = "I'm %s \\ cat." % "\\ a"

fat_cat = '''
I'll do a list:
\t* Cat %s
\t* Fishies
\t* Catnip\n\t* Grass
''' % "food"

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat