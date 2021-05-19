from tkinter import scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

#from Saisi_chapitre import *

with open('livre.json', 'r') as json_data:
    data_dict = json.load(json_data)
    json.dumps(data_dict, indent=4)

print(data_dict)

#pour accéder à tes valeur :
#prends data_dict[i] i représente ta page
#rajoute encore [str] str est le nom de ta clé (par exemple "numero")
#donc si tu fais data_dict[0]["numero"] tu accède au numero de page de ta première page qui est 1
 
#exemple
print(data_dict[0]['numero'])
print(data_dict[1]['texte'])

#pour faire les boites de texte j'ai juste replacé le Entry() pas Label() et le texte par ce qu'il représente avec data_dict[i][str]

#pour faire une fenetre plus longue
data_dict[0]['texte'] = "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla \n"



n = 0

def numchapchoix1():
    n = data_dict["numchoix1"]
    return n

chap = tk.Tk()

chap.title('Saisi chapitre')


# zone de saisie 1 : Numéro de chapitre

libnum = Label(chap, text = "Chapitre :                      ")
libnum.grid(row=0, column=1, padx=(0, 15), pady=10)

entnum = Label(chap, text= data_dict[n]["numero"])
entnum.focus_set()  # boîte de saisie par défaut
entnum.grid(row=0, column=1, padx=(0, 15), pady=10)



# zone de saisie 2 : Nom de chapitre

entnom = Label(chap, text= data_dict[n]["nom"])

entnom.focus_set()  # boîte de saisie par défaut

entnom.grid(row=1, column=1, padx=(0, 15), pady=10)



# zone de saisie 3 : Texte du chapitre

enttexte = Label(chap, text= data_dict[n]["texte"])

enttexte.focus_set()  # boîte de saisie par défaut

enttexte.grid(row=2, column=1, padx=(0, 15), pady=10)


# zone de saisie 4 : Texte choix 1

btn_choix1 = Button(chap, text= data_dict[n]["choix1"], command = numchapchoix1)

btn_choix1.focus_set()  # boîte de saisie par défaut

btn_choix1.grid(row=3, column=1, padx=(0, 15), pady=10)




# zone de saisie 6: Texte choix 2

btn_choix2 = Button(chap, text= data_dict[n]["choix2"])


btn_choix2.focus_set()  # boîte de saisie par défaut

btn_choix2.grid(row=5, column=1, padx=(0, 15), pady=10)




# zone de saisie 8: Texte choix 3

btn_choix3 = Button(chap, text= data_dict[n]["choix3"])

btn_choix3.focus_set()  # boîte de saisie par défaut

btn_choix3.grid(row=7, column=1, padx=(0, 15), pady=10)

# libellé 9 : Revoie choix 3




bouton_quitter = Button(chap, text='Quitter ', command=chap.destroy, padx=10, pady=5)

bouton_quitter.grid(row=9, columnspan=1, padx=5, pady=(5, 15))



chap.mainloop()
