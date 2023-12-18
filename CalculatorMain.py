# Functions for arithmatic operations
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print("e")
        
def power(a,b):
    return a^b

def remainder(a,b): 
    return a%b

# Get User inuts for values
def select_op(choice):
    if(choice == '#'):
        return -1
    elif(choice in ('+','-','*','/','^','%')):
        while True:
            first_input = input("Enter first number: ")
            print(first_input)
            try:
                num1 = float(first_input) 
                break
            except:
                print("Not a valid number,please enter again")
                continue
        while True:
            second_input = input("Enter second number: ")
            print(second_input)            
            try:
                num2 = float(second_input) 
                break
            except:
                print("Not a valid number,please enter again")
                continue
            
        if(choice == '+'):
            print(num1, '+', num2, '=', add(num1, num2))
        elif(choice == '-'):
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif(choice == '*'):
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif(choice == '/'):
            print(num1, '/', num2, '=', divide(num1, num2))
        elif(choice == '^'):
            print(num1, '^', num2, '=', power(num1, num2))
        elif(choice == '%'):
            print(num1, '%', num2, '=', remainder(num1, num2))
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")
# Main loop. 
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()