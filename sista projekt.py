#==================Import==============
from tkinter import *
import random
#=============Setting==================
window = Tk() 
window.title("sista projekt")
window.geometry("500x500") 
window.resizable(width=False , height = False)
#============variablar==================
color = "skyblue"
window.configure(bg=color)
#=================frames=================
top_first =Frame(window, width=400 , height= 50 , bg= color)
top_first.pack(side = "top")
top_second =Frame(window , width=400 , height= 50 , bg= color)
top_second.pack(side = "top")
top_third =Frame(window , width=400 , height= 50 , bg= color)
top_third.pack(side = "top")
top_fourth =Frame (window , width=400 , height= 50 , bg= color)
top_fourth.pack(side = "top")
top_fifth =Frame(window , width= 400 , height= 50, bg= color)
top_fifth.pack(side = "top")
top_six =Frame(window , width=400 , height= 50 , bg= color)
top_six.pack(side = "top")
top_seven=Frame(window , width=400 , height= 50 , bg= color)
top_seven.pack(side = "top")
top_eight =Frame(window , width=400 , height= 50 , bg= color)
top_eight.pack(side = "top")
top_nine =Frame(window , width=400 , height= 50 , bg= color)
top_nine.pack(side = "top")
#============function===================
# def kasta():



        
#================button===============
btn_kasta= Button(top_fifth, text = "kasta tärning", highlightbackground=color , width= 30 , height= 2 , font=("tahoma", 18) ,)
btn_kasta.pack( padx=10, pady= 10)
btn_beholl= Button(top_six, text = "behåll", highlightbackground=color , width= 20 , height= 2 , font=("tahoma", 16))
btn_beholl.pack(padx=5, pady= 5)
#================LAbel and text=================
lbl_firstplayer = Label(top_first ,text = "player 1 :", font=("tahoma", 40) , bg=color)
lbl_firstplayer.pack(side = LEFT , padx = 5 , pady= 5)
lbl_res = Label(top_first , text = "0", font=("tahoma", 40) , bg=color)
lbl_res.pack(side = LEFT , padx = 5 , pady= 5)
lbl_secondplayer = Label(top_second ,text = "player 2 :", font=("tahoma", 40) , bg=color)
lbl_secondplayer.pack(side = LEFT , padx = 5 , pady= 5)
lbl_res2 = Label(top_second , text = "0", font=("tahoma", 40) , bg=color)
lbl_res2.pack(side = LEFT , padx = 5 , pady= 5)
nuvarande_point = Label(top_third ,text = "Nuvarande poäng :", font=("tahoma", 15) , bg=color)
nuvarande_point.pack(side = LEFT , padx = 2 , pady= 2)
nuvarande_pointres = Label(top_third ,text = "0", font=("tahoma", 15) , bg=color)
nuvarande_pointres.pack()
point = Label(top_fourth , text = "0", font=("tahoma", 40) , bg="white")
point.pack(padx= 20 , pady= 20)

window.mainloop()

