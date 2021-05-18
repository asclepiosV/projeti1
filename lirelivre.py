import tkinter as tk
from tkinter import *
import json

with open('livre.json', 'r') as json_data:
    data_dict = json.load(json_data)
    json.dumps(data_dict, indent=4)

print(data_dict[1])





fenetre = tk.Tk()

fenetre.title('Notre super livre')



fenetre.mainloop()

