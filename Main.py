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

#===================================================================================================================================

def myNameIs(name):
    #print my name
    print(name + " is my name")

myNameIs("Kaleb")

#==================================================================================================================================

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

#====================================================================================================================================================

def madlib(a, b, c, d, e, f, g, h, i, j):
    #create a madlib with multiple spots where a adjective or noun can be added
    print("Star Wars is a " + a + b + " of " + c + " versus evil in a " + d + " far far away. There are " + e + " battles between " 
    + f + g + " in " + h + " space and " + i + " duels with " + j + " called...")

#run the function madlib
madlib("space", " opra", "good", "galaxy", "galactic", "star", " fighters", "deep", "physical", "swords")

#====================================================================================================================================================

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


#create a function with an if statement
def equalsTen(x):
    if x == 10:
        return "x is equal to 10!!!"

    elif x > 10:
        return "x is greater than 10!!!"

    else:
        return "x is less than 10!!!"

print(equalsTen(29))


def favColor(color):
    if color == "green":
        return "your favorite color is green"

    elif color == "Green":
        return "your favorite color is green"

    else:
        return "your favorite color is NOT green"

#=================================================================================================================================================================================================================================================================

#Create a dictionary with ten different words

def defineDict(word):

    #word.upper() also exists, if it were to be used, then all of the 'words' should be in all caps like,
    #if word == "SANS"
    word = word.lower()

    if word == "sans":
        return "A skeleton from the Underground who will dunk on you if he judges your lOVE to be too high. Also the brother of Papyrus and likes to use puns."

    elif word == "papyrus":
        return "NYAHAHA!!!"

    elif word == "gaster":
        return "You have been playing too much Undertale and Deltarune."

    elif word == "spider-man":
        return "Hero of NYC with the powers of a spider. There are two different Spider-Men. Under the masks are Peter Parker and Miles Morales."
    
    elif word == "goku":
        return "A saiyan raised on earth. Has defeated many threats to the Earth and the Universe. Has the power of the Gods and Angels."

    elif word == "dog":
        return "An animal that will love you forever (unlike a certain other one...)"
    
    elif word == "monkey":
        return "MONKE..."

    elif word == "saiyan":
        return "Saiyans are a race that love the thrill of battle. They have the special ability to transform into many forms and obtain Zenkai Boosts. Saiyans have a monkey tail at birth. Only a few remain."

    elif word == "zenkai boost":
        return "A special ability of the Saiyan race. Literally what doesn't kill them makes them stronger, much stronger."

    elif word == "dragon ball":
        return "A dragon ball is a ball that has 1 to 7 stars inside. When all 7 are collected, a dragon will appear that will grant anywhere from 1-3 wishes, depending on the impact of the wish. Dragon Balls are created by a race called Namekians."

    else:
        return "This word in not in this terrible dictionary. Go onto google for a real answer."

print(defineDict("Papyrus"))

#===========================================================================================================================================================================================================================================================

#modulus is very simillar to division
print (99 % 100)

print (12 % 10)

#Absolute Value is NOT |#|
print(abs(-256))

#Define the function evenOrOdd()
def evenOrOdd(x):
    if x % 2 == 0:
        return True

    else:
        return False

print (evenOrOdd(4))

#=============================================================================================================================================================================================================================================================

#'and' is a Boolean Operator
def twoBigNumbers(x, y):
    if x > 10 and y > 10:
        return True

    else:
        return False

#'or' is a Boolean Operator
def atLeastOneBigNumber(x, y):
    if x > 10 or y > 10:
        return True

    else:
        return False

#'not' is a Boolean Operator. could also be written as -- if x > 10 or y <= 10: ...
def OneBigNumber():
    if x > 10 or not y > 10:
        return True

    else:
        return False

# You can have 'and' and 'or' operators in the name statement
def andOrNumbers(x, y, z):
    if x > 10 or not y > 10 and z == 5:
        return True
    
    else:
        return False

#When using () the statement will be read in an order of operations style. 
#If it was ...or not (y > 10 and z == 5)... then 'not' would be used on both y > 10 AND z == 5, 
#instead of just y > 10.
def andOrNumberOp(x, y, z):
    if x > 10 or (not y > 10 and z == 5):
        return True

    else:
        return False 


