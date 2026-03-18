# Function to print help instructions
def print_help():
    print("Help Instructions: \n Code 0: Terminate Program \n " \
    "Code 1: Addition \n " \
    "Code 2: Subtraction \n " \
    "Code 3: Multiplication \n " \
    "Code 4: Division \n " )

# Function to sum two numbers
def addition(a,b):
    return a + b

# Function to subtract two numbers
def subtraction(a,b):
    return  a-b

# Function to multiply two numbers
def multiplication(a,b):
    return a*b

# Function to divide two numbers
def division(a,b):
    if b == 0: #check if divider is equal to 0 to avoid errors
        return "Error: division by zero"
    return a/b


# Main code starts here
print("\n \nSimple Python Calculator - Code is running: ")
loop = True
print_help()
while(loop):  
     # Ask user for operation code
    operation_code = input("Insert Code: ")

    # If operation_code is equal 0 the loop terminates
    if (operation_code == "0"):
        print("Loop Terminated\n")
        break
    
    # Check if operation_code in correct
    if (operation_code not in ["1","2","3","4"]):
        print("Incorrect Code!\n")
        continue

    # Ask numbers to be operated
    first_number = float(input("Insert first number: "))
    second_number = float(input("Insert second number: "))

    # Select the operation based on the code entered
    match operation_code:
        case "1":
            result = addition(first_number, second_number)
        case "2":
            result = subtraction(first_number, second_number)
        case "3":
            result = multiplication(first_number, second_number)
        case "4":
            result = division(first_number, second_number)

    print("Result: ", result)
        
print("Program completely terminated!")
