from tkinter import scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

#from Saisi_chapitre import *


with open('livre.json', 'r') as json_data:
    data_dict = json.load(json_data)
    json.dumps(data_dict, indent=4)


def trouver_contenu_chapitre(numero_chapitre):
    for chapitre in data_dict:
        if chapitre["numero"] == numero_chapitre:
            return chapitre
    raise Exception(f"Chapitre {numero_chapitre} non trouvé")


def afficher_chapitre_gui(contenu):
    chap = tk.Tk()
    chap.title('Saisi chapitre')

    libnum = Label(chap, text = "Chapitre :                      ")
    libnum.grid(row=0, column=1, padx=(0, 15), pady=10)

    entnum = Label(chap, text= contenu["numero"])
    entnum.focus_set()  # boîte de saisie par défaut
    entnum.grid(row=0, column=1, padx=(0, 15), pady=10)

    entnom = Label(chap, text= contenu["nom"])
    entnom.focus_set()  # boîte de saisie par défaut
    entnom.grid(row=1, column=1, padx=(0, 15), pady=10)

    enttexte = Label(chap, text= contenu["texte"])
    enttexte.focus_set()  # boîte de saisie par défaut
    enttexte.grid(row=2, column=1, padx=(0, 15), pady=10)

    btn_choix1 = Button(chap, text= contenu["choix1"], command=lambda: affiche_chapitre(contenu["numchoix1"]))
    btn_choix1.focus_set()  # boîte de saisie par défaut
    btn_choix1.grid(row=3, column=1, padx=(0, 15), pady=10)

    btn_choix2 = Button(chap, text= contenu["choix2"])
    btn_choix2.focus_set()  # boîte de saisie par défaut
    btn_choix2.grid(row=5, column=1, padx=(0, 15), pady=10)

    btn_choix3 = Button(chap, text= contenu["choix3"])
    btn_choix3.focus_set()  # boîte de saisie par défaut
    btn_choix3.grid(row=7, column=1, padx=(0, 15), pady=10)

    bouton_quitter = Button(chap, text='Quitter ', command=chap.destroy, padx=10, pady=5)
    bouton_quitter.grid(row=9, columnspan=1, padx=5, pady=(5, 15))

    chap.mainloop()

def affiche_chapitre(numero_chapitre):
    if numero_chapitre is None:
        contenu_chapitre = data_dict[0]
    else:
        contenu_chapitre = trouver_contenu_chapitre(numero_chapitre)
    print(f"CHAPITRE : {contenu_chapitre}")
    afficher_chapitre_gui(contenu_chapitre)

affiche_chapitre(None)


sys.exit(0)



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




def numchapchoix1(n, data_dict):
    n = data_dict[n]["numchoix1"]
    print(n)
    return n
