
#==================Import============== alvin
from tkinter import *
import random
#=============Setting================== alvin
window = Tk() 
window.title("sista projekt")
window.geometry("500x500") 
window.resizable(width=False , height = False)
#============variablar================== mahan
color = "skyblue"
window.configure(bg=color)
#=================frames================= alvin och mahan
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

#============funktioner=================== alvin
# Speldata
poäng = [0, 0]  # Totala poäng för spelare 1 och 2
nuvarande_poäng = 0
aktiv_spelare = 0  # 0 för spelare 1, 1 för spelare 2
spelet_slut = False

def kasta_tärning():
    global nuvarande_poäng, aktiv_spelare, spelet_slut
    if spelet_slut:
        return
    kast = random.randint(1, 6)
    point.config(text=str(kast))
    if kast == 1:
        nuvarande_poäng = 0
        nuvarande_pointres.config(text="0")
        byt_spelare()
    else:
        nuvarande_poäng += kast
        nuvarande_pointres.config(text=str(nuvarande_poäng))

def behåll_poäng():
    global poäng, nuvarande_poäng, aktiv_spelare, spelet_slut
    if spelet_slut:
        return
    poäng[aktiv_spelare] += nuvarande_poäng
    nuvarande_poäng = 0
    nuvarande_pointres.config(text="0")
    lbl_res.config(text=str(poäng[0]))
    lbl_res2.config(text=str(poäng[1]))
    if poäng[aktiv_spelare] >= 100:
        point.config(text=f"Spelare {aktiv_spelare + 1} vinner!")
        spelet_slut = True
    else:
        byt_spelare()

def byt_spelare():
    global aktiv_spelare
    aktiv_spelare = 1 - aktiv_spelare  # Växla mellan spelare 0 och 1

#============funktioner=================== alvin
# Speldata
poäng = [0, 0]  # Totala poäng för spelare 1 och 2
nuvarande_poäng = 0
aktiv_spelare = 0  # 0 för spelare 1, 1 för spelare 2
spelet_slut = False

def kasta_tärning():
    global nuvarande_poäng, aktiv_spelare, spelet_slut
    if spelet_slut:
        return
    kast = random.randint(1, 6)
    point.config(text=str(kast))
    if kast == 1:
        nuvarande_poäng = 0
        nuvarande_pointres.config(text="0")
        byt_spelare()
    else:
        nuvarande_poäng += kast
        nuvarande_pointres.config(text=str(nuvarande_poäng))

def behåll_poäng():
    global poäng, nuvarande_poäng, aktiv_spelare, spelet_slut
    if spelet_slut:
        return
    poäng[aktiv_spelare] += nuvarande_poäng
    nuvarande_poäng = 0
    nuvarande_pointres.config(text="0")
    lbl_res.config(text=str(poäng[0]))
    lbl_res2.config(text=str(poäng[1]))
    if poäng[aktiv_spelare] >= 100:
        point.config(text=f"Spelare {aktiv_spelare + 1} vinner!")
        spelet_slut = True
    else:
        byt_spelare()

def byt_spelare():
    global aktiv_spelare
    aktiv_spelare = 1 - aktiv_spelare  # Växla mellan spelare 0 och 1


#================button=============== mahan
btn_kasta = Button(top_fifth, text="kasta tärning", command=kasta_tärning, highlightbackground=color, width=30, height=2, font=("tahoma", 18))
btn_kasta.pack( padx=10, pady= 10)


btn_beholl = Button(top_six, text="behåll", command=behåll_poäng, highlightbackground=color, width=20, height=2, font=("tahoma", 16))
btn_beholl.pack(padx=5, pady= 5)
#================LAbel and text================= mahan och rodion
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

