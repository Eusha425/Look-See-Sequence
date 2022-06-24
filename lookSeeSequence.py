# A simple look and see sequence algorithm inspired from Geeks for Geeks
# Author: Gazi MD Wasi-UL-Hoque Eusha
# Date : 22 june 2022

def lookAndSequence(term) :

    valid = True
    while valid != False:
        # the first two values of the sequence
        if term == 1:
            return "1"
        elif term == 2:
            return "11"
        elif term > 2: 
            message = "11" # message value initailised as n is greater than 2        
            # to find the value of the user given nth term
            for i in range(3, term + 1): # n incremented as computer starts calculation from 0
                
                message += "x"      # updating the content of the message by one so that the loop functions as intended
                tempMessage = ""    # temporary place holder when the content of the current message needs to be updated
                count = 1           # to count the consecutive duplicate numbers
                
                # to check the concurrent two values to calculate the next value of the sequence
                for j in range(1, len(message)):
                    if message[j] == message[j - 1]:
                        count += 1                  # incrementing value when there is a match
                    else:
                        tempMessage += str(count)       # the total duplicates
                        tempMessage += message[j - 1]   # the previous value(the one whose total duplicate is calculated)
                        count = 1                   # changing back the value of count so that the next value can be calculated               
                message = tempMessage
            return message
        elif term <= 0: # to check validity of the term
            print("Invalid number!")
            valid = True
            term = takeInput()

# take string user input and convert to integer
def takeInput() :    
	userInput = int(input("Enter the number of terms you want to display: ").strip())
	return userInput

# starter code
print("How many terms you want to display?")
userInput = takeInput()
for i in range(1, userInput + 1):
    print(lookAndSequence(i))
