from random import *
from tkinter import *

score = 0


def rock():
    global score
    k = randint(0, 2)
    com = 'Computer played:'+list1[k]+'  '+list2[k]
    if score < 10 :
        if k == 0:
            lbl.config(text=com)
            lbl1.config(text='Its a Draw...(✿◠‿◠)')
        elif k == 1:
            score-=1
            lbl.config(text=com)
            sclbl.config(text=score)
            lbl1.config(text='You Loose....(´。＿。`)')
        elif k == 2:
            score+=1
            sclbl.config(text=score)
            lbl.config(text=com)
            lbl1.config(text='You Win !!!!....╰(*°▽°*)╯')
    elif score==10:
        lbl.config(text='Game Over...You won')


def paper():
    global score
    k = randint(0, 2)
    com = 'Computer played:'+list1[k]+'  '+list2[k]
    if score < 10:
        if k == 0:
            score+=1
            sclbl.config(text=score)
            lbl.config(text=com)
            lbl1.config(text='You Win !!!!....╰(*°▽°*)╯')
        elif k == 1:
            lbl.config(text=com)
            lbl1.config(text='Its a Draw...(✿◠‿◠)')
        elif k == 2:
            score-=1
            sclbl.config(text=score)
            lbl.config(text=com)
            lbl1.config(text='You Loose....(´。＿。`)')
    elif score==10:
        lbl.config(text='Game Over...You won')


def scissor():
    global score
    k = randint(0, 2)
    com = list1[k]+'  '+list2[k]
    if score < 10:
        if k == 0:
            score-=1
            sclbl.config(text=score)
            lbl.config(text=com)
            lbl1.config(text='You Loose....(´。＿。`)')
        elif k == 1:
            score+=1
            sclbl.config(text=score)
            lbl.config(text=com)
            lbl1.config(text='You Win !!!!....╰(*°▽°*)╯')
        elif k == 2:
            lbl.config(text=com)
            lbl1.config(text='Its a Draw...(✿◠‿◠)')
    elif score==10:
        lbl.config(text='Game Over...You won')

list1 = ['ROCK', 'PAPER', 'SCISSORS']
list2 = ['✊', '🖐', '✌']

window = Tk()
window.title('Rock Paper Scissors')
window.config(bg='yellow')
sclbl = Label(window, text=score, font=('Arial', 30, 'bold'))
sclbl.pack()
lbl = Label(window, text='   ', font=('Arial', 30, 'bold'))
lbl.pack(padx=10,pady=20)
lbl1 = Label(window, text='   ', font=('Arial', 30, 'bold'))
lbl1.pack(padx=10,pady=20)
frame1 = Frame(window, bg='yellow', highlightbackground='red', highlightthickness='10')
frame1.pack(padx=10,pady=10)
lbl2 = Label(frame1, text='Click The Button To Play The Round', font=('Arial', 30, 'bold'))
lbl2.pack()
btn = Button(frame1, text='Rock', bg='orange', fg='black', command=rock)
btn.pack()
btn = Button(frame1, text='Paper', bg='orange', fg='black', command=paper)
btn.pack()
btn = Button(frame1, text='Scissor', bg='orange', fg='black', command=scissor)
btn.pack()

window.mainloop()
