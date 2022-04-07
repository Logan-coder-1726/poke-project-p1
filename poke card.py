from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("Endless pokemon card Game")
root.geometry("600x400")

root.configure(background="green2")

Img=ImageTk.PhotoImage(Image.open ("gmaxstoise.jpg"))
Img=ImageTk.PhotoImage(Image.open ("gmaxasaur.jpg"))

player1 = Label(root, text = "player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_poke_label = Label(root, bg = "chocolate1", fg = "white")
random_poke_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()
