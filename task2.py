#Calculator

print("This is basic calculator to solve Arthmetic operations like '+' , '-' , '*' , '/' etc. ")

#Calculator

# user take input start program or not

print("START PRESS :- 1")

print("EXIT PRESS :- 0")

start= int(input("PRESS :- "))

if start == 1:
    
    # take input to the user
    
    b = int (input("Enter the first number :- "))
    
    c = int (input("Enter the second number :- "))
    

elif start == 0:
    
    print("Thank for use ")
    
    exit()
    
else:
    
    exit()
    
operation = input(f"{b} enter the operation {c} : ")

if operation == "+" :
    
    print( "This  is the Final Result :- ",b+c)
    
    
elif operation == "*":
    
    print( "This  is the Final Result :- ",b*c)
    
elif operation == "-":
    
    print ("This  is the Final Result :- ",b-c)
    
elif operation == "/":
    
    print ("This  is the Final Result :- ",b/c)
    
else :
    
    exit()

    
    

