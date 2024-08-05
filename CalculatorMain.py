#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return None

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Function to input numbers and handle errors
def input_number(prompt):
    while True:
        value = input(prompt)
         
        if isinstance(value, str) and value.endswith('$'):
            print(value)
            return value[-1]
        elif isinstance(value, str) and value.endswith('#'):
            print(value)
            print("Done. Terminating")
            exit()
        else:
            print(value)
            return float(value)
               
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice in '+-*/^%':
        a = input_number("Enter first number: ")

        if not a =='$':
            b = input_number("Enter second number: ")
        
        if a =='$' or b == '$':
            return
        else:
            if choice == '+':
                result = add(a, b)
                print(f"{a:.1f} + {b:.1f} = {result:.1f}")
            elif choice == '-':
                result = subtract(a, b)
                print(f"{a:.1f} - {b:.1f} = {result:.1f}")
            elif choice == '*':
                result = multiply(a, b)
                print(f"{a:.1f} * {b:.1f} = {result:.1f}")
            elif choice == '/':
                result = divide(a, b)
                if result is None:
                    print(f"{a:.1f} / {b:.1f} = None")
                else:
                    print(f"{a:.1f} / {b:.1f} = {result:.1f}")
            elif choice == '^':
                result = power(a, b)
                print(f"{a:.1f} ^ {b:.1f} = {result:.1f}")
            elif choice == '%':
                result = remainder(a, b)
                print(f"{a:.1f} % {b:.1f} = {result:.1f}")
    elif choice == '#': #terminate
        return -1
    elif choice == '$': #reset
        return 0
    else:
        print("Unrecognized operation")


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
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