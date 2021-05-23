#this program is inspired by the project given on the book but I optimized a little and now you can actually play it. 
#Disclaimer : I didn't write functions to check if the cell is available to input so you can give input to one cell as many times as you want, I hope you don't :)
#reason is I am a student and I don't have much time to finish this. Maybe you'll do it.
import sys, time
theboard={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
print('X or O')
x=input()
def check(theboard):
    for i in range(9):
        if theboard[1]==theboard[2]==theboard[3]:
            print(theboard[1], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[4]==theboard[5]==theboard[6]:
            print(theboard[4], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[7]==theboard[8]==theboard[9]:
            print(theboard[7], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[1]==theboard[4]==theboard[7]:
            print(theboard[1], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[2]==theboard[5]==theboard[8]:
            print(theboard[2], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[3]==theboard[6]==theboard[9]:
            print(theboard[3], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[1]==theboard[5]==theboard[9]:
            print(theboard[1], 'You won')
            time.sleep(3)
            sys.exit()
        elif theboard[3]==theboard[5]==theboard[7]:
            print(theboard[3], 'You won')
            time.sleep(3)
            sys.exit()
    

def space(board):
    print('')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('')
    check(theboard)

for i in range(1,10):
    space(theboard)
    if x=='x':
        print(i,') Turn for: ', x.upper(), '. Which position?')
        pos=int(input())
        theboard[pos]='X'
        x='o'
    elif x=='o':
        print(i,') Turn for: ', x.upper(), '. Which position?')
        pos=int(input())
        theboard[pos]='O'
        x='x'

space(theboard)
