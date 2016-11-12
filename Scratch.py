"""
Number guessing game

"""

def getInput():
    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while (answer != "h" and answer != "l" and answer != "c"):
        answer = raw_input("Invalid input. Please enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    return answer

def isTooHigh(answer):
    if answer == "h":
        return True
    else:
        return False

def checkNumber(low, high, num):
        print("My guess is " + str(num))
        ans = getInput()
        while ans != "c":
          if isTooHigh(ans):
            return checkNumber(low, num, reducer(low,num))
          else:
            return checkNumber(num, high, reducer(num,high))
        return num

def reducer(low, high):
    return (low + high)/2

print("Number guessing game! Please think of a number between 1 and 100!")
final = checkNumber(0, 100, 50)
print("Your number is " + str(final) + "!!!!")