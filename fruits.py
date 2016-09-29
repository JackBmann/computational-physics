'''
fruits.py
experiments with lists and sub-list commands
9/1/16
'''
fruit = ["cherry", "blackberry", "peach", "blueberry", "apricot"]
#fruit = []
#for x in range(5):
#    f = raw_input("Enter a " + str(x+1) + "th fruit: ")
#    fruit.append(f);
print fruit[0] #prints the first fruit the user has entered
print fruit[0:3] #prints the first three fruits in the list
print fruit[3:] #prints the fruits after the first 3 fruits in the list
print fruit[0:5:2] #prints every other fruit in the list for the first 5 fruits in the list starting with the first fruit
print fruit[:] #prints all of the fruits in the list
print len(fruit) #prints the number of fruits in the list