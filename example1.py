'''
example1.py
calculates sum of integers from 1 to 100 and experiments with loops
8/30/2016
'''

value = 0 #initialize our sum to zero

for i in range(1, 101, 1):
    value = value + i
    if (i <= 25 or i>= 75):
        print "The value for i =", i, "is:", value
print "The sum of the first 100 integers is: ", value

#let's try a while loop

value = 0 #re-initialize value to zero
j = 1 #initialize counter value
while (j < 101):
    value+=j
    j+=1
print "The sum of the first 100 integers is: ", value

#prints all odds from 1-50
print
odds = []
for x in range(1, 50, 2):
    odds.append(x)
print odds
