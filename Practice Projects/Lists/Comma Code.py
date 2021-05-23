def lit(item): #creating a function named lit
    test='' #declaring a local string variable to contain the output
    for i in range(len(item)): #a loop to check all the item in the list
        if i==len(item)-2: #condition to check if current item is the last item or not, if it is the last item
            test=test+item[i]+' and ' #program inserts the word and after the second last item
            test=test+item[-1] #and the last item is added
            break #breaking out of loop
        else: #if current item is not the last item
            test=test+item[i]+', '  #program inserts comma after that item
    return print(test) #printing the output
spam = ['apples', 'bananas', 'tofu', 'cats'] #the list with 4 items, you can change the amount as much as you want
lit(spam) # calling the function lit



#you're welcome
