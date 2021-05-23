import sys,time #importing sys and time modules
def collatz(number): #creating a function named collatz
    if number % 2 ==0:
        x=number//2
    else:
        x=3*number+1

    return x

print("Type an integer") #asking for input from a user
i = int(input())  
while True:  # a loop to make the sequence          
    print(collatz(i)) #calling the function and printing the value of the function
    i=collatz(i) #input is taking the value of the last called function
    time.sleep(0.2) #delaying the next step just to make it look fancy
    if collatz(i)==1: # if value of the function is equal to 1
        print('1') # it will print 1
        print('You have reached end of the program') 
        sys.exit() # and terminates the program
        
        
        
        
#you're welcome:)

