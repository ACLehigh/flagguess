from tkinter import *

import random

from tkinter.messagebox import showerror, showwarning, showinfo

win=Tk()

score=0

lives=3

def flag():

    global score, lives, a

    fvalue=entry1.get()

    if fvalue.lower()=='argentina' and a==1:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="austria" and a==2:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="belarus" and a==3:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="bulgaria" and a==4:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="belgium" and a==5:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="canada" and a==6:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="finland" and a==7:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="germany" and a==8:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="iceland" and a==9:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="isreal" and a==10:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="russia" and a==11:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="south korea" and a==12:

        score+=1

        label4.configure(text=f'Score: {score}')

    elif fvalue.lower()=="south africa" and a==13:

        score+=1

        label4.configure(text=f'Score: {score}')

    else:

        lives-=1

        label3.configure(text=f'Lives: {lives}')

    a=random.randint (1,13)

    if a==1:

        label2.configure(image=photo1)

    elif a==2:

        label2.configure(image=photo2)

    elif a==3:

        label2.configure(image=photo3)

    elif a==4:

        label2.configure(image=photo4)

    elif a==5:

        label2.configure(image=photo5)

    elif a==6:

        label2.configure(image=photo6)

    elif a==7:

        label2.configure(image=photo7)

    elif a==8:

        label2.configure(image=photo8)

    elif a==9:

        label2.configure(image=photo9)

    elif a==10:

        label2.configure(image=photo10)

    elif a==11:

        label2.configure(image=photo11)

    elif a==12:

        label2.configure(image=photo12)

    else:

        label2.configure(image=photo13)

    entry1.delete(0, END)

    if lives==0:

        showerror(title="Game Over!", message=f'You Lost. Your score is: {score}')

        win.destroy()



win.geometry("1920x1080")

win.config(bg="#9cc72e")

label1=Label(win, font=("Garamond", 65), text="Flag Guesser", bg="#9cc72e")

label1.place(relx=0.4, rely=0.0005)



photo1=PhotoImage(file="ag.gif")

photo2=PhotoImage(file="au.gif")

photo3=PhotoImage(file="be.gif")

photo4=PhotoImage(file="bg.gif")

photo5=PhotoImage(file="bm.gif")

photo6=PhotoImage(file="ca.gif")

photo7=PhotoImage(file="fi.gif")

photo8=PhotoImage(file="gm.gif")

photo9=PhotoImage(file="ic.gif")

photo10=PhotoImage(file="is.gif")

photo11=PhotoImage(file="ru.gif")

photo12=PhotoImage(file="sk.gif")

photo13=PhotoImage(file="so.gif")

a=random.randint(1,13)



label2=Label(win, image=photo1)

label2.place(relx=0.1, rely=0.4)

if a==1:

    label2.configure( image=photo1)

elif a==2:

    label2.configure( image=photo2)

elif a==3:

    label2.configure( image=photo3)

elif a==4:

    label2.configure(image=photo4)

elif a==5:

    label2.configure( image=photo5)

elif a==6:

    label2.configure( image=photo6)

elif a==7:

    label2.configure( image=photo7)

elif a==8:

    label2.configure(image=photo8)

elif a==9:

    label2.configure(image=photo9)

elif a==10:

    label2.configure(image=photo10)

elif a==11:

    label2.configure( image=photo11)

elif a==12:

    label2.configure( image=photo12)

else:

    label2.configure(image=photo13)



label3=Label(win, font=("Garamond", 45), text="Lives: 3", bg="#9cc72e")

label3.place(relx=0.75,rely=0.0005)

label4=Label(win, font=("Garamond", 45), text="Score: 000", bg="#9cc72e")

label4.place(relx=0.75, rely=0.05)

label5=Label(win, font=("Garamond", 50), text="Which flag is this?", bg="#9cc72e")

label5.place(relx=0.4, rely=0.25)

entry1=Entry(win,font=("Garamond", 40))

entry1.place(relx=0.4, rely=0.4)

button1=Button(win, font=("Garamond", 30), text="Submit", command=flag)

button1.place(relx=0.54, rely=0.5)









win.mainloop()