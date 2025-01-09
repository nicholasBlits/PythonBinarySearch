"""
    File Name: index.py
    File Version: 1.0.7
    Author: Nicholas S. Blits

    Description: This program asks the user to enter 11 Integers, sorts those values in ascending order, then asks the user for a number to find the index of. 
"""

# Start of index.py

# A method that asks users to populate a Python List by entering Integer values
# The values entered by the user are casted to the Integer type and then added to a List
def populateList():

    # Creating a List (which is initially empty) to store user input
    userInputs = []

    # Creating a counter variable and initially setting it equal to 1.
    i = 1


    while i < 12: # A while loop to repeatedly prompt the user to enter a number
        # Storing user input in a variable called enteredNumber, to then add to the userInputs List
        enteredNumber = int(input(f"Enter number {i}: ")) # The prompt uses the current value of i to tell the user what number in the list they are currently entering
        # The user's input is cast as an Integer type, so the userInputs List tracks numbers
        userInputs.append(enteredNumber) # Appending the number as entered (and rounded to an Integer in the case of floats [ex. 1.2 will be stored as 1 in the List])
        i += 1 # Incrementing the counter variable by 1

    return userInputs # Return the List after it has been populated to contain 11 numbers.
    # The return statement returns the populated List, which is then stored in a variable found in the main() method of this program.

# A method that calculates the average of two values
# Method parameters: Two Integers, one for the lowest index value being checked at some point p in the code's runtime, and another for the highest index at that same point 
def calculateMiddleIndex(lowBound, highBound):
    # Do the math to calculate an average [(a + b) / n , where n is a non-zero positive number], saving the result into the midpoint variable
    midpoint = float((lowBound + highBound) / 2)
    # Casting the calculated index value to the Integer type and returning it.
    return int(midpoint)

# All above commented in full

# A method that searches a List of numbers
# Method parameters: A List of numbers entered by the user and a Integer of which number the user wishes to locate in the List
def searchList(valuesList, desiredValue):
    
    # Setting initial values for the lowest and highest index values of the List
    # The lowest valid index is 0 by default, and the highest index is the length of the List minus 1, as length is a count of the number of items in a List
    lowestIndex = 0
    highestIndex = len(valuesList) - 1

    # Calculating the index in-between the current highest and lowest indices
    # Doing so calls the calculateMiddleIndex method, passing in the variables lowestIndex and highestIndex for the parameters
    midpointIndex = calculateMiddleIndex(lowestIndex, highestIndex)

    while lowestIndex <= highestIndex:  # A while-loop to run while there are still numbers to check; This loop determines if the number was found in the List or not.

        midpointIndex = calculateMiddleIndex(lowestIndex, highestIndex) # At the start of the loop, reevaluate the value of the index in-between the current high and low bounds of the search space.

        if valuesList[midpointIndex] == desiredValue: # Check if the value of the List at the middle index is equal to the value the user wishes to know the index of.
            # If true, return a message informing the user that the value they wanted to search for was found at the current middle index value.
            return f"The value {desiredValue} was found at index {midpointIndex}."

        elif valuesList[midpointIndex] > desiredValue: # Checking if the value of the List at the current middle index is greater than the number the user wants to find in the List.
            highestIndex = midpointIndex  - 1  # If this condition is met, set the highest index to the index before the current middle index (as the value at middle index is greater than the value the user wants to find.)

        else:
            lowestIndex = midpointIndex + 1 # If the value being searched for is greater than the value of the List at the current middle index, set the lowest index to the index after the current middle index (as the value at middle index is less than the value the user wants to find.)

    # If every number in the List does not match up with the value the user wishes to find, return a formatted message informing them that the number they wanted to find was not entered into the List used in this program.
    return f"The value {desiredValue} was not found in the list of numbers entered." 

        
# A Main method that begins the program
# This method has no parameters, and is functionally the same as a Main method in both Java and C# code.
def main():
    # Create a variable for the List of numbers the user enters, saving the List returned from the populateList() method
    userList = populateList()
    
    # Sort the list of values entered by the user in ascending order
    userList.sort()

    # Create a variable to store the input of the user
    # As numbers are what a user is to enter, to properly store the value the user enters, the inputs must be cast to the Integer type
    searchNum = int(input("Enter a number to locate the index of: "))

    # First, call the searchList method, passing in the List variable made in this method and the number to search for that was just obtained as the method's parameters
    # After the method is called and returns a value, print out the message returned by the searchList method to the user.
    print(searchList(userList, searchNum))

if __name__ == "__main__": # Check that there is a method named main
    main() # If the method exists, call the main() method and begin the program's execution.
# End of index.py
