from tkinter import *
from PIL import Image, ImageTk
from random import randint




# Main Window

root = Tk()
root.title('Rock Paper Scissor')
root.configure(background = '#222560')





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

def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = str(score)

        # System Score Update

def updateSystemScore():
    score = int(system_score['text'])
    score += 1
    system_score['text'] = str(score)










# Message

msg = Label(root, font = 100, bg = '#222560', fg = 'white')
msg.grid(row = 3, column = 2)

# Update Message

def updateMessage(x):
    msg['text'] = x






# Change Choice

choices = ["rock", "paper", "scissor"]
def changeChoice(x):

# For Player
    if(x == 'rock'):
        player_label.configure(image = rock_image)
    elif(x == 'paper'):
        player_label.configure(image = paper_image)
    else:
        player_label.configure(image = scissor_image)

# For System

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
rock_btn.grid(row = 2, column = 1)
paper_btn.grid(row = 2, column = 2)
scissor_btn.grid(row = 2, column = 3)






# Check Winner

def checkWinner(player, system):
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