from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data import *

### COLOR ###
color_0 = "#0d0d0d" #black
color_1 = "#F5FFFA"#white
color_2 = "#4169E1"#blue
color_3 = "#38576b"#value
color_4 = "#403d3d"#write
color_5 = "#FF6347"#red

#creat windows
windows = Tk()
windows.title('')
windows.geometry('550x510')
windows.configure(bg=color_1)

ttk.Separator(windows, orient = HORIZONTAL).grid(row=0,columnspan=1, ipadx=272)

style = ttk.Style(windows)
style.theme_use("classic")

#creat frame
frame_pokemon = Frame(windows, width=550,height=308,relief="flat")
frame_pokemon.grid(row=1,column=0)

#Func for Switch Pokemon

def switch_pok(i):
    global image_pok,pok_image

    #Type
    pok_name['text'] = i
    pok_name['bg'] = pokemon[i]['Description'][3] #color ['bg']
    pok_description['text'] = pokemon[i]['Description'][1]
    pok_description['bg'] = pokemon[i]['Description'][3]
    pok_id['text'] = pokemon[i]['Description'][0]
    pok_id['bg'] = pokemon[i]['Description'][3]
    image_pok= pokemon[i]['Description'][2]

    #Frame Pokemon
    frame_pokemon['bg']= pokemon[i]['Description'][3]
   
    #image
    image_pok = Image.open(image_pok)
    image_pok = image_pok.resize((248, 238))
    image_pok = ImageTk.PhotoImage(image_pok)

    pok_image = Label(frame_pokemon,image= image_pok, relief='flat',bg=pokemon[i]['Description'][3], fg=color_1)
    pok_image.place(x=75,y=50)

    pok_description.lift() #put text over image

    pok_hp['text'] = pokemon[i]['Status'][0]
    pok_attack['text'] = pokemon[i]['Status'][1]
    pok_defense['text'] = pokemon[i]['Status'][2]
    pok_speed['text'] = pokemon[i]['Status'][3]
    pok_total['text'] = pokemon[i]['Status'][4]
    pok_power['text'] = pokemon[i]['Skills'][0]
    pok_power2['text'] = pokemon[i]['Skills'][1]
    

#name
pok_name = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg= color_1, fg=color_1)
pok_name.place(x=12,y=15)

#description
pok_description = Label(frame_pokemon, text="Eletric", relief='flat', anchor=CENTER, font=('Ivy 12 bold'), fg=color_1)
pok_description.place(x=12,y=55)

#id
pok_id = Label(frame_pokemon, text="#025", relief='flat', anchor=CENTER, font=('Ivy 12 bold '), fg=color_1)
pok_id.place(x=12,y=80)

#Status
pok_status = Label(windows, text="Status", relief='flat', anchor=CENTER, font=('Verdana 21'),bg=color_1, fg=color_0)
pok_status.place(x=15,y=315)

#HP
pok_hp = Label(windows, text="HP:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_hp.place(x=15,y=365)

#Attack
pok_attack = Label(windows, text="Attack:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_attack.place(x=15,y=390)

#Defense
pok_defense = Label(windows, text="Defense:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_defense.place(x=15,y=415)

#Speed
pok_speed = Label(windows, text="Speed:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_speed.place(x=15,y=440)

#Total
pok_total = Label(windows, text="Total:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_total.place(x=15,y=465)

#Skills
pok_skills = Label(windows, text="Skills:", relief='flat', anchor=CENTER, font=('Verdana 21'),bg=color_1, fg=color_4)
pok_skills.place(x=290,y=315)

#Power
pok_power = Label(windows, text="Power:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_power.place(x=290,y=365)

#Power2
pok_power2 = Label(windows, text="Power:", relief='flat', anchor=CENTER, font=('Verdana 10'),bg=color_1, fg=color_4)
pok_power2.place(x=290,y=390)


####Create button for Pokemon####
#Pikachu
image_pok1 = Image.open('img/Pikachu_head.png')
image_pok1 = image_pok1.resize((40,40))
image_pok1 = ImageTk.PhotoImage(image_pok1)

button_pok1 = Button(windows,command=lambda:switch_pok('Pikachu'),image= image_pok1,text='Pikachu',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok1.place(x=375,y=10)

#Charmander
image_pok2 = Image.open('img/cabeca-charmander.png')
image_pok2 = image_pok2.resize((40,40))
image_pok2 = ImageTk.PhotoImage(image_pok2)

button_pok2 = Button(windows,command=lambda:switch_pok('Charmander'),image= image_pok2,text='Charmander',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok2.place(x=375,y=60)

#Dragonite
image_pok3 = Image.open('img/cabeca-dragonite.png')
image_pok3 = image_pok3.resize((40,40))
image_pok3 = ImageTk.PhotoImage(image_pok3)

button_pok3 = Button(windows,command=lambda:switch_pok('Dragonite'),image= image_pok3,text='Dragonite',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok3.place(x=375,y=110)

#Gengar
image_pok4 = Image.open('img/cabeca-gengar.png')
image_pok4 = image_pok4.resize((40,40))
image_pok4 = ImageTk.PhotoImage(image_pok4)

button_pok4 = Button(windows,command=lambda:switch_pok('Gengar'),image= image_pok4,text='Gengar',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok4.place(x=375,y=160)

#Gyarados
image_pok5 = Image.open('img/cabeca-gyarados.png')
image_pok5 = image_pok5.resize((40,40))
image_pok5 = ImageTk.PhotoImage(image_pok5)

button_pok5 = Button(windows,command=lambda:switch_pok('Gyarados'),image= image_pok5,text='Gyarados',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok5.place(x=375,y=210)

#Bulbasaur
image_pok6 = Image.open('img/cabeca-bulbasaur.png')
image_pok6= image_pok6.resize((40,40))
image_pok6 = ImageTk.PhotoImage(image_pok6)

button_pok6 = Button(windows,command=lambda:switch_pok('Bulbasaur'),image= image_pok6,text='Bulbasaur',width=150,relief='flat',overrelief=RIDGE,compound=LEFT,padx=5,anchor=NW,font=('Verdana 12'),bg=color_1,fg=color_0)
button_pok6.place(x=375,y=260)

switch_pok('Pikachu')





windows.mainloop()