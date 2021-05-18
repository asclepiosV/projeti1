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





chap = tk.Tk()

chap.title('Saisi chapitre')

# libellé 1 : Numéro de chapitre

libnum = Label(chap, text='numéro du chapitre : ')

libnum.grid(row=0, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 1 : Numéro de chapitre

entnum = Label(chap, text= data_dict[0]["numero"])
entnum.focus_set()  # boîte de saisie par défaut
entnum.grid(row=0, column=1, padx=(0, 15), pady=10)

# libellé 2 : Nom de chapitre

libnom = Label(chap, text='nom du chapitre : ')

libnom.grid(row=1, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 2 : Nom de chapitre

entnom = Label(chap, text= data_dict[0]["nom"])

entnom.focus_set()  # boîte de saisie par défaut

entnom.grid(row=1, column=1, padx=(0, 15), pady=10)

# libellé 3 : Texte du chapitre

libtexte = Label(chap, text='texte du chapitre : ')

libtexte.grid(row=2, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 3 : Texte du chapitre

enttexte = Label(chap, text= data_dict[0]["texte"])

enttexte.focus_set()  # boîte de saisie par défaut

enttexte.grid(row=2, column=1, padx=(0, 15), pady=10)

# libellé 4 : Texte choix 1

libchoix1 = Label(chap, text='premier choix : ')

libchoix1.grid(row=3, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 4 : Texte choix 1

entchoix1 = Label(chap, text= data_dict[0]["choix1"])

entchoix1.focus_set()  # boîte de saisie par défaut

entchoix1.grid(row=3, column=1, padx=(0, 15), pady=10)

# libellé 5 : Revoie choix 1


entnumchoix1 = Label(chap, text= data_dict[0]["numchoix1"])


entnumchoix1.focus_set()  # boîte de saisie par défaut

entnumchoix1.grid(row=4, column=1, padx=(0, 15), pady=10)

# libellé 6: Texte choix 2

libchoix2 = Label(chap, text='deuxieme choix')

libchoix2.grid(row=5, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 6: Texte choix 2

entchoix2 = Label(chap, text= data_dict[0]["choix2"])


entchoix2.focus_set()  # boîte de saisie par défaut

entchoix2.grid(row=5, column=1, padx=(0, 15), pady=10)



entnumchoix2 = Label(chap, text= data_dict[0]["numchoix2"])


entnumchoix2.focus_set()  # boîte de saisie par défaut

entnumchoix2.grid(row=6, column=1, padx=(0, 15), pady=10)

# libellé 8 : Texte choix 3

libchoix3 = Label(chap, text='troisieme choix : ')

libchoix3.grid(row=7, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 8: Texte choix 3

entchoix3 = Label(chap, text= data_dict[0]["choix3"])

entchoix3.focus_set()  # boîte de saisie par défaut

entchoix3.grid(row=7, column=1, padx=(0, 15), pady=10)

# libellé 9 : Revoie choix 3


entnumchoix3 = Label(chap, text= data_dict[0]["numchoix3"])


entnumchoix3.focus_set()  # boîte de saisie par défaut

entnumchoix3.grid(row=8, column=1, padx=(0, 15), pady=10)

# Le nouveau dictionnaire est "retourné" au code appelant cette fonction



bouton_quitter = Button(chap, text='Quitter ', command=chap.destroy, padx=10, pady=5)

bouton_quitter.grid(row=9, columnspan=1, padx=5, pady=(5, 15))



chap.mainloop()
