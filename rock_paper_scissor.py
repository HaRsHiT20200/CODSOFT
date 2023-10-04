from tkinter import *
from PIL import Image,ImageTk 
from random import *
#main window
root = Tk()
root.title("Games")
root.geometry("1000x650+250+75")
root.resizable(False,False)

root.config(background="light green")

# insert pictures
rock_user_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_user_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_user_img = ImageTk.PhotoImage(Image.open("scissors_user.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open("scissor.png"))

user_label = Label(root,image=rock_user_img,bg="light green")
comp_label = Label(root,image=rock_comp_img,bg="light green")
user_label.place(x=100,y=150)
comp_label.place(x=650,y=150)

# scores
player_score = Label(root,text=0,font=("Elephant",20),bg="Light green")
comp_score = Label(root,text=0,font=("Elephant",20),bg="Light green")
player_score.place(x=210,y=100)
comp_score.place(x=760,y=100)


# indicaters

user_indicater = Label(root,font=("Times new roman",30),text="You",bg="Light green",fg="purple")
comp_indicater = Label(root,font=("Times new roman",30),text="Computer",bg="light green",fg="blue")
user_indicater.place(x=180,y=50)
comp_indicater.place(x=700,y=50)

# message
msg = Label(root,font=("Calibri",30),bg="light green",fg="brown")
msg.place(x=430,y=430)

# update message
def update_msg(x):
    msg['text'] = x

# update user score
def update_user_score():
    score = int(player_score["text"])
    score+=1
    player_score["text"] = str(score)

# update computer score
def update_comp_score():
    score = int(comp_score["text"])
    score+=1
    comp_score["text"] = str(score)


# check winner 
def check_win(player,computer):
    if player==computer:
        update_msg("Tie!!!")
    
    elif player=="rock":
        if computer=="scissor":
            update_msg("You WIN")
            update_user_score()
        else:
            update_msg("You Lose")
            update_comp_score()
    
    elif player=="paper":
        if computer=="rock":
            update_msg("You WIN")
            update_user_score()
        else:
            update_msg("You Lose")
            update_comp_score()
    
    elif player=="scissor":
        if computer=="paper":
            update_msg("You WIN")
            update_user_score()
        else:
            update_msg("You Lose")
            update_comp_score()
    else:
        pass


# update choices
def update_choice(x):
    choices = ["rock","paper","scissor"]
    comp_choice = choices[randint(0,2)]
    
    if comp_choice=="rock":
        comp_label.config(image=rock_comp_img)
    
    elif comp_choice=="paper":
        comp_label.config(image=paper_comp_img)
    
    else:
        comp_label.config(image=scissor_comp_img)

    
    
    # for user
    if x=="rock":
        user_label.config(image=rock_user_img)
        
        
    elif x=="paper":
        user_label.config(image=paper_user_img)
    elif x=="scissor":
        user_label.config(image=scissor_user_img)
    else:
        pass

    check_win(x,comp_choice)




# buttons
# we use arguments in funtion so we use lambda function here
rock = Button(root,width=15,height=2,text="ROCK",command=lambda:update_choice("rock"),font=('Arial',16),bg="Yellow",fg="Red")
paper = Button(root,width=15,height=2,text="PAPER",command=lambda:update_choice("paper"),font=('Arial',16),bg="olive",fg="blue")
scissor = Button(root,width=15,height=2,text="SCISSOR",command=lambda:update_choice("scissor"),font=('Arial',16),bg="orange",fg="black")
rock.place(x=250,y=500)
paper.place(x=430,y=500)
scissor.place(x=610,y=500)


root.mainloop()
