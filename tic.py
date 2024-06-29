board=[' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |   ')
    print(' '+ board[1] +' | '+ board[2] +' | '+ board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+ board[4] +' | ' +board[5] +' | '+ board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+ board[7] +' | '+ board[8] +' | '+ board[9])
    print('   |   |   ')
    
def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
    
def IsWinner(b,l):
    return ((b[1]==l and  b[2] ==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l ) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l) )

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')


def computerMove():
    possibleMove=[x for x,letter in enumerate(board) if  letter ==' 'and x!=0 ]
    move=0
    
    for let in ['O','X']:
        for i in possibleMove:
            boardCopy=board[:]
            boardCopy[i]=let
            if IsWinner(boardCopy,let):
                move=i
                return move
            
    cornerOpen=[]
    for i in possibleMove:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
            
    if len(cornerOpen)>0:
        move= selectRandom(cornerOpen)
        return move
        
    if 5 in possibleMove:
        move=5
        return move
    
    edgeOpen=[]
    for i in possibleMove:
        if i in [2,4,6,8]:
            edgeOpen.append(i)

    if len(edgeOpen)>0:
        move=selectRandom(edgeOpen)
        return move
            
def selectRandom(li):
     import random
     ln =len(li)
     r= random.randrange(0,ln)
     return li[r]

def main():
    print("welcome to the game!")
    printBoard(board)

    while not (isBoardFull(board)):
        if  not(IsWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break
        if not(IsWinner(board,'X')):
            move=computerMove()
            if move ==0:
                print("tie Game")
            else:
                insertLetter('O',move)
                print('computer placed an O in position',move,':')
                printBoard(board)

        else:
            print("you win!")
            break

    if  isBoardFull(board):
        print("tie game")

while True:
    x= input("do you want to play again? y/n\n")
    if x.lower()=='y':
        board=[' 'for x in range(10)]
        print('------------------')
        main()
    else:
        break

