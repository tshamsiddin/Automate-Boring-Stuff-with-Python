import random #importing random function to make a list of random H and Ts
lit=[] #declaring a varibale to contain a list of H and Ts
total=0 #variable to keep track of the number of 6 straight Hs
total2=0 #variable to keep track of the number of 6 straight Ts
for i in range(10000): #loop to make a sequence of H and Ts
    x=random.randint(0,1) #random function to create either H or T
    if x==0: #if it is 0,
        lit.append('H') #list appends H
    else: #otherwise
        lit.append('T') #list appends T
for j in range(9995): #another loop to check the 6 straight H and Ts happened in the sequence
    if lit[j:j+6] == ['H','H','H','H','H','H']:
        total=total+1 
    if lit[j:j+6]==['T','T','T','T','T','T']:
        total2=total2+1
        
print(lit) #printing the orginal list
print('Number of 6-H streaks: ', total)
print('Number of 6-T streaks: ', total2)
print('Possibility of encountering number of straight Hs in 10000 flips: ', total/100, '%')
print('Possibility of encountering number of straight Ts in 10000 flips: ', total2/100, '%')

#you're welcome:)
