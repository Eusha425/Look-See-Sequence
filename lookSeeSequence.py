# A simple look and see sequence algorithm inspired from Geeks for Geeks
# Author: Gazi MD Wasi-UL-Hoque Eusha
# Date : 22 june 2022

def lookAndSequence(n) :

    # the first two values of the sequence
    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    elif n > 2: 
        message = "11" # message value initailised as n is greater than 2        
        # to find the value of the user given nth term
        for i in range(3, n + 1): # n incremented as computer starts calculation from 0
            
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

# take string user input and convert to integer
def takeInput() :    
	n = int(input("Enter the term nth to display: ").strip())
	return n

# starter code
n = takeInput()
print(lookAndSequence(n))