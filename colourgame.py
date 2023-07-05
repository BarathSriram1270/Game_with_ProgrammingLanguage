from tkinter import *
from random import choice
from tkinter import messagebox
rot=Tk()
rot.title("hello barath")
rot.geometry('900x900')
x=Label(rot,text="",font=("bold",100))
x.pack()
score=0
timeavil=60
def start(event):
    if timeavil==60:
        timecount()
        shuffle()
        scorelabel.config(text="Score: 0")
def timecount():
    global timeavil
    if timeavil==0:
        messagebox.showinfo("time over","time is over and your score is "+str(score))
    if timeavil>0:
        timeavil-=1
        timelabel.config(text="time left:"+str(timeavil))
        timelabel.after(1000,timecount)
def shuffle():
    ans.delete(0,END)
    anslab.after(400,lambda:anslab.config(text=""))
    global wordclr
    clr=['red','green','orange','pink','black','navy','brown','yellow','white']
    word=choice(clr)
    wordclr=choice(clr)
    x.config(text=word,fg=str(wordclr))
def answers():
    global score
    global timeavil
    if timeavil>0:
        ans.focus_set()
        if wordclr==ans.get().lower():
            score+=1
            anslab.config(text="Correct !!!")
        else:
            anslab.config(text="Incorrect")
        scorelabel.config(text="score :"+str(score))
        shuffle()
scorelabel=Label(rot,text="Enter to start",font=24)
scorelabel.pack()
timelabel=Label(rot,text="time left:"+str(timeavil),font=12)
timelabel.pack(pady=10,padx=30)
ans=Entry(rot,font=25)
ans.pack(pady=20)
frame=Frame(rot)
frame.pack()
but2=Button(frame,text="answer",command=answers)
but2.grid(row=0,column=1,padx=10)
anslab=Label(rot,text="",font=25)
anslab.pack()
ans.focus_set()
rot.bind('<Return>',start)
rot.mainloop()