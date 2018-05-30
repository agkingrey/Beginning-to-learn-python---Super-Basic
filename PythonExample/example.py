#welcome to my python project. Here I'll do some basic
#programming logic. I'll try to throw in some basic if statements, and maybe a loop.
amountOfNumbers = int(input("Enter How many numbers you would like to enter:"))
counter = int(1)
runningTotal = float(0)

while amountOfNumbers >= counter:
    number = float(input("Enter number %d: " % counter))
    counter += 1
    runningTotal += number
    
print("The sum of the numbers is: %d" % runningTotal )

average = runningTotal/amountOfNumbers
print("The average of the numbers is: %d " % average)

doneState = input("Did you forget any numbers? yes or no.")

if doneState.lower() == 'yes':
    newAmountOfNumbers = int(input("Enter How many extra numbers you would like to enter:"))  
    newAmountOfNumbers += amountOfNumbers
    while newAmountOfNumbers >= counter:
        number = float(input("Enter number %d:" % counter))
        counter += 1
        runningTotal += number

print("The sum of the numbers is: %d" % runningTotal )

newAverage = runningTotal/newAmountOfNumbers
print("The average of the numbers is: %d " % newAverage)