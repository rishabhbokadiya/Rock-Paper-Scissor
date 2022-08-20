from tkinter import *
from PIL import Image, ImageTk
from random import randint





# Main Window

root = Tk()
root.title('Rock Paper Scissor')
root.configure(background = '#222560')
global sysChoice, scorep, scores





# Pictures

rock_image = ImageTk.PhotoImage(Image.open('Rock.png'))
paper_image = ImageTk.PhotoImage(Image.open('Paper.png'))
scissor_image = ImageTk.PhotoImage(Image.open('Scissor.png'))

# Insert Pictures

player_label = Label(root, image = rock_image, bg = '#222560')
system_label = Label(root, image = rock_image, bg = '#222560')
player_label.grid(row = 1 , column = 0)
system_label.grid(row = 1 , column = 4)






# Players

player_ind = Label(root, font = 200, text = 'PLAYER', bg = '#222560', fg = 'white')
system_ind = Label(root, font = 200, text = 'SYSTEM', bg = '#222560', fg = 'white')
player_ind.grid(row = 0, column = 0)
system_ind.grid(row = 0, column = 4)





# Score Card

player_score = Label(root, font = 100, text = 0, bg = '#222560', fg= 'white')
system_score = Label(root, font = 100, text = 0, bg = '#222560', fg= 'white')
player_score.grid(row = 1, column = 1)
system_score.grid(row = 1, column = 3)

# Update Scores

        # Player Score Update

def updatePlayerScore(flagp = 0):
    global scorep
    scorep = int(player_score['text'])
    if(flagp):
        scorep = 0
        
    else:
        scorep += 1

    #end call
    if(scorep==5):
        updateMessage("You won the Game! 5-"+ str(scores))
        #root.after(ms = 2000)
        scorep = 0
        updateSystemScore(1)   
    
    player_score['text'] = str(scorep)

        # System Score Update

def updateSystemScore(flags = 0):

    global scores
    scores = int(system_score['text'])
    if(flags):
        scores = 0
    else:
        scores += 1
    
    #end call
    if(scores==5):
        updateMessage("System won the Game! 5-" + str(scorep))
        #root.after(ms = 2000)
        scores = 0
        updatePlayerScore(1)

           
         
    system_score['text'] = str(scores)










# Message

msg = Label(root, font = 100, bg = '#222560', fg = 'white')
msg.grid(row = 3, column = 2)

# Update Message

def updateMessage(x):
    msg['text'] = x






# Change Choice

choices = ["rock", "paper", "scissor", "reset_score"]
def changeChoice(x):

# For Player
    if(x == 'rock'):
        player_label.configure(image = rock_image)
    elif(x == 'paper'):
        player_label.configure(image = paper_image)
    elif(x == 'scissor'):
        player_label.configure(image = scissor_image)
    else:
        checkWinner('rst', 'rst', 1)   

# For System
    if(x != 'reset_score'):
        sysChoice = choices[randint(0,2)]

        if(sysChoice == 'rock'):
            system_label.configure(image = rock_image)
        elif(sysChoice == 'paper'):
            system_label.configure(image = paper_image)
        else:
            system_label.configure(image = scissor_image)

        checkWinner(x, sysChoice)






# Buttons

rock_btn = Button(root, text= 'ROCK', command = lambda : changeChoice('rock'), width= 20, height=2, bg= '#ff1616', fg= 'white')
paper_btn = Button(root, text= 'PAPER', command = lambda : changeChoice('paper'), width= 20, height=2, bg= 'brown', fg= 'white')
scissor_btn = Button(root, text= 'SCISSOR', command = lambda : changeChoice('scissor'), width= 20, height=2, bg= 'green', fg= 'white')
reset_btn = Button(root, text= 'RESET', command = lambda : changeChoice('reset_score'), width= 20, height=2, bg= 'green', fg= 'white')
rock_btn.grid(row = 2, column = 1)
paper_btn.grid(row = 2, column = 2)
scissor_btn.grid(row = 2, column = 3)
reset_btn.grid(row=2, column=4)






# Check Winner

def checkWinner(player, system, reset_flag = 0):
    if(reset_flag):
        updatePlayerScore(1)
        updateSystemScore(1)
        updateMessage("Game Reset Successfully")

    if(player == 'rst'):
        return    
        
    if(player == system):
        updateMessage("Its a tie !!")
    elif(player == 'rock'):
        if(system == 'paper'):
            updateMessage('You Loose !')
            updateSystemScore()
        else:
            updateMessage('You Won !')
            updatePlayerScore()

    elif(player == 'paper'):
        if(system == 'scissor'):
            updateMessage('You Loose !')
            updateSystemScore()
        else:
            updateMessage('You Won !')
            updatePlayerScore()
    
    elif(player == 'scissor'):
        if(system == 'rock'):
            updateMessage('You Loose !')
            updateSystemScore()
        else:
            updateMessage('You Won !')
            updatePlayerScore()

    else:
        pass



root.mainloop()