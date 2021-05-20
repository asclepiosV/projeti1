from tkinter import scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json


with open('livre.json', 'r') as json_data:
    data_dict = json.load(json_data)
    json.dumps(data_dict, indent=4)


def trouver_contenu_chapitre(numero_chapitre):
    for chapitre in data_dict:
        if chapitre["numero"] == numero_chapitre:
            return chapitre
    raise Exception(f"Chapitre {numero_chapitre} non trouvé")


def afficher_chapitre_gui(contenu,chap):

    nde = " "
    ligne = 40

    for c in chap.winfo_children():
        c.destroy()

    lib_numero_chapitre = Label(chap, text = "Chapitre :                      ")
    lib_numero_chapitre.grid(row=0, column=1, padx=(0, 15), pady=10)

    num_chapitre = Label(chap, text= contenu["numero"])
    num_chapitre.focus_set()
    num_chapitre.grid(row=0, column=1, padx=(0, 15), pady=10)

    nom_chapitre = Label(chap, text= contenu["nom"])
    nom_chapitre.focus_set()
    nom_chapitre.grid(row=1, column=1, padx=(0, 15), pady=10)

    ligne_chapitre = contenu["texte"]

    while len(ligne_chapitre) > ligne:
        ere = ligne_chapitre[:ligne]
        ligne_chapitre = ligne_chapitre[ligne:]
        nde += ere + "\n"
    ligne_chapitre = nde + ligne_chapitre

    texte_chapitre = Label(chap, text= ligne_chapitre)
    texte_chapitre.focus_set()
    texte_chapitre.grid(row=2, column=1, padx=(0, 15), pady=10)

    btn_choix1 = Button(chap, text= contenu["choix1"], command=lambda: affiche_chapitre(contenu["numchoix1"]))
    btn_choix1.focus_set()
    btn_choix1.grid(row=3, column=1, padx=(0, 15), pady=10)

    btn_choix2 = Button(chap, text= contenu["choix2"], command=lambda: affiche_chapitre(contenu["numchoix2"]))
    btn_choix2.focus_set()
    btn_choix2.grid(row=5, column=1, padx=(0, 15), pady=10)

    btn_choix3 = Button(chap, text= contenu["choix3"], command=lambda: affiche_chapitre(contenu["numchoix3"]))
    btn_choix3.focus_set()
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
    afficher_chapitre_gui(contenu_chapitre,chap)

chap = tk.Tk()
chap.title('lecture du livre')


affiche_chapitre(None)


sys.exit(0)
