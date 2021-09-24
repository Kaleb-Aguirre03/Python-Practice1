def topFiveMovies():
    #print the title of the list
    print("My Top Five Movies:")

    #pint the 1st movie
    print("1) Home Alone 2")

    #print the 2nd movie
    print("2) Spider-Man: Into the Spider-Verse")

    #print the 3rd movie
    print("3) Dragon Ball Super: Broly")

    #print the 4th movie
    print("4) Dragon Ball Z: Fusion Reborn")

    #Print the 5th movie
    print("5) The Amazing Spider-Man 2")

def topThreeSports():
    #print the title of the list
    print("My Top Three Sports:")

    #print the 1st sport
    print("1) Baseball")

    #print the 2nd sport
    print("2) American Football")

    #print the 3rd sport
    print("3) Basketball")

def namesOfFam():
    #print the title of the list
    print("Names of My Family:")

    #print the name of mom
    print("Mom: Charity")

    #print the name of dad
    print("Dad: Matt")

    #print the name of sis
    print("Sister: Miki")

    #print the name of dog
    print("Dog: Teddy")

def statesIveBeenTo():
    #print title of the list
    print("States That I Have Been To:")

    #print 1st state
    print("Wisconsin")

    #print 2nd state
    print("South Dakota")

    #print 3rd state
    print("Florida")


#run the funtion topFiveMovies WOOOOOO
topFiveMovies()

#run the function topThreeSports
topThreeSports()

#run the function namesOfFam
namesOfFam()

#run the function statesIveBeenTo
statesIveBeenTo()

def myNameIs(name):
    #print my name
    print(name + " is my name")

myNameIs("Kaleb")

def timesTwo(X):
    #print something and multiply by two
    print(X * 2)

#run the function timesTwo
timesTwo(2)

def multTwoNmbrs(x, y):
    #print two numbers and multiply them
    print(x * y)

#run the function multTwoNmbrs
multTwoNmbrs(4, 7)

def plusFive(a):
    #print a number and add 5
    print(a + 5)

def divideByTwo(z):
    #print a number and divide by two
    print(z / 2)

#run the function plusFive
plusFive(3)

#run the function divideByTwo
divideByTwo(16)

def addThreeNmbrs(x, y, z):
    #print three numbers and add them together
    print(x + y + z)

#run the function addThreeNmbrs
addThreeNmbrs(4, 18, 98)



def madlib(a, b, c, d, e, f, g, h, i, j):
    #create a madlib with multiple spots where a adjective or noun can be added
    print("Star Wars is a " + a + b + " of " + c + " versus evil in a " + d + " far far away. There are " + e + " battles between " 
    + f + g + " in " + h + " space and " + i + " duels with " + j + " called...")

#run the function madlib
madlib("space", " opra", "good", "galaxy", "galactic", "star", " fighters", "deep", "physical", "swords")


#create a function with an if statement
def greaterThanTen (x):
    if x > 10:
        return "x is greater than 10"
    
    elif x == 10:
        return "x equals 10"
    
    else:
        return "x is not greater than 10"

#print the function with a number greater than 10
print (greaterThanTen (11))

#print the function with a number less than 10
print (greaterThanTen(9))

#print the function with the number 10
print (greaterThanTen(10))