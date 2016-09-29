'''
example2.py
another for loop
8/30/2016
'''

#create a tuple
Majors = ('Francis', 'Alvaro', 'Peter', 'Andrew', 'Joan of Arc', 'Philip')
counter = 1
for name in Majors:
    print "Hello student number " + str(counter) + ", " + name + '.'
    counter+=1
print "Thank you for being such great students."