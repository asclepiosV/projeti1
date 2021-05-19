from tkinter import scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Importe toutes les fonctions de la bibliothèque JSON
# (syntaxe obligeant à écrire "json." devant le nom de la fonction appelée)
import json

# Version où les classes sont recréées à chaque fois
#livre = []
# Version où on conserve les classes dans un fichier JSON



fichier = open("livre.json", "r")
livre = json.load(fichier)
fichier.close()

def cree_chapitre():

    a = entnum.get()
    b = entnom.get("1.0", END)
    c = enttexte.get("1.0", END)
    d = entchoix1.get("1.0", END)
    e = entnumchoix1.get()
    f = entchoix2.get("1.0", END)
    g = entnumchoix2.get()
    h = entchoix3.get("1.0", END)
    i = entnumchoix3.get()

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)

    chapitre = {}
    chapitre["numero"] = a
    chapitre["nom"] = b
    chapitre["texte"] = c
    chapitre["choix1"] = d
    chapitre["numchoix1"] = e
    chapitre["choix2"] = f
    chapitre["numchoix2"] = g
    chapitre["choix3"] = h
    chapitre["numchoix3"] = i

    livre.append(chapitre)
    # Recrée le fichier avec la liste modifiée
    fichier = open("livre.json", "w")
    json.dump(livre, fichier)
    fichier.close()

    entnum.delete(0, END)
    entnom.delete(1.0, END)
    enttexte.delete(1.0, END)
    entchoix1.delete(1.0, END)
    entnumchoix1.delete(0, END)
    entchoix2.delete(1.0, END)
    entnumchoix2.delete(0, END)
    entchoix3.delete(1.0, END)
    entnumchoix3.delete(0, END)


    messagebox.showinfo("Saisi de chapitre", "Chapitre Envoyé")











chap = tk.Tk()

chap.title('Saisi chapitre')

# libellé 1 : Numéro de chapitre

libnum = Label(chap, text='Entrer le numéro du chapitre : ')

libnum.grid(row=0, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 1 : Numéro de chapitre

entnum = Entry(chap, width=43)

entnum.focus_set()  # boîte de saisie par défaut

entnum.grid(row=0, column=1, padx=(0, 15), pady=10)

# libellé 2 : Nom de chapitre

libnom = Label(chap, text='Entrer le nom du chapitre : ')

libnom.grid(row=1, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 2 : Nom de chapitre

entnom = scrolledtext.ScrolledText(chap, wrap=tk.WORD, width=30, height=3)

entnom.focus_set()  # boîte de saisie par défaut

entnom.grid(row=1, column=1, padx=(0, 15), pady=10)

# libellé 3 : Texte du chapitre

libtexte = Label(chap, text='Entrer le texte du chapitre : ')

libtexte.grid(row=2, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 3 : Texte du chapitre

enttexte = scrolledtext.ScrolledText(chap, wrap=tk.WORD, width=30, height=8)

enttexte.focus_set()  # boîte de saisie par défaut

enttexte.grid(row=2, column=1, padx=(0, 15), pady=10)

# libellé 4 : Texte choix 1

libchoix1 = Label(chap, text='Entrer le premier choix : ')

libchoix1.grid(row=3, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 4 : Texte choix 1

entchoix1 = scrolledtext.ScrolledText(chap, wrap=tk.WORD, width=30, height=3)

entchoix1.focus_set()  # boîte de saisie par défaut

entchoix1.grid(row=3, column=1, padx=(0, 15), pady=10)

# libellé 5 : Revoie choix 1

libnumchoix1 = Label(chap, text='Entrer le numéro du chapitre vers lequel le choix 1 renvoie: ')

libnumchoix1.grid(row=4, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 5 : Revoie choix 1

entnumchoix1 = Entry(chap, width=43)

entnumchoix1.focus_set()  # boîte de saisie par défaut

entnumchoix1.grid(row=4, column=1, padx=(0, 15), pady=10)

# libellé 6: Texte choix 2

libchoix2 = Label(chap, text='Entrer le deuxieme choix : ')

libchoix2.grid(row=5, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 6: Texte choix 2

entchoix2 = scrolledtext.ScrolledText(chap, wrap=tk.WORD, width=30, height=3)

entchoix2.focus_set()  # boîte de saisie par défaut

entchoix2.grid(row=5, column=1, padx=(0, 15), pady=10)

# libellé 7 : Revoie choix 2

libnumchoix2 = Label(chap, text='Entrer le numéro du chapitre vers lequel le choix 2 renvoie: ')

libnumchoix2.grid(row=6, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 7 : Revoie choix 2

entnumchoix2 = Entry(chap, width=43)

entnumchoix2.focus_set()  # boîte de saisie par défaut

entnumchoix2.grid(row=6, column=1, padx=(0, 15), pady=10)

# libellé 8 : Texte choix 3

libchoix3 = Label(chap, text='Entrer le troisieme choix : ')

libchoix3.grid(row=7, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 8: Texte choix 3

entchoix3 = scrolledtext.ScrolledText(chap, wrap=tk.WORD, width=30, height=3)

entchoix3.focus_set()  # boîte de saisie par défaut

entchoix3.grid(row=7, column=1, padx=(0, 15), pady=10)

# libellé 9 : Revoie choix 3

libnumchoix3 = Label(chap, text='Entrer le numéro du chapitre vers lequel le choix 3 renvoie:')

libnumchoix3.grid(row=8, column=0, sticky=E, padx=10, pady=10)

# zone de saisie 9 : Revoie choix 3
entnumchoix3 = Entry(chap, width=43)
entnumchoix3.focus_set()  # boîte de saisie par défaut
entnumchoix3.grid(row=8, column=1, padx=(0, 15), pady=10)

# Le nouveau dictionnaire est "retourné" au code appelant cette fonction


bouton_soumission = Button(chap, text='Envoyer ce chapitre ', command=cree_chapitre, padx=15, pady=5)

bouton_soumission.grid(row=9, columnspan=2, padx=5, pady=(5, 15))

bouton_quitter = Button(chap, text='Quitter ', command=chap.destroy, padx=10, pady=5)

bouton_quitter.grid(row=9, columnspan=1, padx=5, pady=(5, 15))



chap.mainloop()






# S'affiche juste après le "break"
print("Fin du programme...")


