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



    for c in chap.winfo_children():
        c.destroy()


    txnumchap = "Chapitre : " +  contenu["numero"]

    num_chapitre = Label(chap, text= txnumchap)
    num_chapitre.focus_set()
    num_chapitre.grid(row=0, column=1, padx=(0, 15), pady=10)
    num_chapitre.configure(font=("Impact", 20, ), background="#FFFAF0")

    nom_chapitre = Label(chap, text= contenu["nom"])
    nom_chapitre.focus_set()
    nom_chapitre.grid(row=1, column=1, padx=(0, 15), pady=10)
    nom_chapitre.configure(font=("Kozuka Mincho Pr6N B", 15,"bold"), background="#FFFAF0")

    ligne_chapitre = contenu["texte"]

    ligne = 110
    position_espace = 0
    position_courante = 0
    position_debut = 0
    ligne_resultat = ""

    for i in range(0, len(ligne_chapitre)):
        if ligne_chapitre[i] == " ":
            position_espace = i
        if position_courante == ligne:
            ligne_resultat += ligne_chapitre[position_debut: position_espace] + "\n"
            position_debut = position_espace + 1
            position_courante = 0
        position_courante += 1
    ligne_resultat += ligne_chapitre[position_debut:]
    ligne_chapitre = ligne_resultat

    texte_chapitre = Label(chap, text= ligne_chapitre)
    texte_chapitre.focus_set()
    texte_chapitre.grid(row=2, column=1, padx=(0, 15), pady=10)
    texte_chapitre.configure(font=("@Kozuka Mincho Pr6N B", 12), background="#FFFAF0" )

    ligne_choix1 = contenu["choix1"]
    ligne1 = 80
    position_espace1 = 0
    position_courante1 = 0
    position_debut1 = 0
    ligne_resultat1 = ""

    for i in range(0, len(ligne_choix1)):
        if ligne_choix1[i] == " ":
            position_espace1 = i
        if position_courante1 == ligne1:
            ligne_resultat1 += ligne_choix1[position_debut1: position_espace1] + "\n"
            position_debut1 = position_espace1 + 1
            position_courante1 = 0
        position_courante1 += 1
    ligne_resultat1 += ligne_choix1[position_debut1:]
    ligne_choix1 = ligne_resultat1

    btn_choix1 = Button(chap, text= ligne_choix1, command=lambda: affiche_chapitre(contenu["numchoix1"]))
    btn_choix1.focus_set()
    btn_choix1.grid(row=3, column=1, padx=(0, 15), pady=10)
    btn_choix1.configure(font=("@Kozuka Mincho Pr6N B", 8,"italic"), background="#fcf1de")

    ligne_choix2 = contenu["choix2"]
    ligne2 = 80
    position_espace2 = 0
    position_courante2 = 0
    position_debut2 = 0
    ligne_resultat2 = ""

    for i in range(0, len(ligne_choix2)):
        if ligne_choix2[i] == " ":
            position_espace2 = i
        if position_courante2 == ligne2:
            ligne_resultat2 += ligne_choix2[position_debut2: position_espace2] + "\n"
            position_debut2 = position_espace2 + 1
            position_courante2 = 0
        position_courante2 += 1
    ligne_resultat2 += ligne_choix2[position_debut2:]
    ligne_choix2 = ligne_resultat2

    btn_choix2 = Button(chap, text= ligne_choix2, command=lambda: affiche_chapitre(contenu["numchoix2"]))
    btn_choix2.focus_set()
    btn_choix2.grid(row=5, column=1, padx=(0, 15), pady=10)
    btn_choix2.configure(font=("@Kozuka Mincho Pr6N B", 8, "italic"), background="#fcf1de")

    ligne_choix3 = contenu["choix3"]
    ligne3 = 80
    position_espace3 = 0
    position_courante3 = 0
    position_debut3 = 0
    ligne_resultat3 = ""

    for i in range(0, len(ligne_choix3)):
        if ligne_choix3[i] == " ":
            position_espace3 = i
        if position_courante3 == ligne3:
            ligne_resultat3 += ligne_choix3[position_debut3: position_espace3] + "\n"
            position_debut3 = position_espace3 + 1
            position_courante3 = 0
        position_courante3 += 1
    ligne_resultat3 += ligne_choix3[position_debut3:]
    ligne_choix3 = ligne_resultat3

    btn_choix3 = Button(chap, text= ligne_choix3, command=lambda: affiche_chapitre(contenu["numchoix3"]))
    btn_choix3.focus_set()
    btn_choix3.grid(row=7, column=1, padx=(0, 15), pady=10)
    btn_choix3.configure(font=("@Kozuka Mincho Pr6N B", 8, "italic"), background="#fcf1de")

    bouton_quitter = Button(chap, text='Quitter ', command=chap.destroy, padx=10, pady=5)
    bouton_quitter.grid(row=9, columnspan=1, padx=5, pady=(5, 15))
    bouton_quitter.configure(font=("Kozuka Mincho Pr6N B", 8, "bold"), background="#fcf1de")

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
chap.configure(bg="#FFFAF0")


affiche_chapitre(None)


sys.exit(0)
