from customtkinter import *
from json import *

# Paramètres de la fenêtre
windows = CTk()
windows.title("Formulaire Python")
windows.geometry("720x550")
windows.config(bg="#333")

password_entry = None
age_bar = None
name_entry = None

def soumission(donnees, error_dict):
    # Réinitialision de l'état d'erreur au début de chaque soumission
    error_dict["error_bool"] = False
    error_dict["error_messages"][0] = ""
    error_dict["error_messages"][1] = ""
    error_dict["error_messages"][2] = ""

    #Validation du nom
    current_name = name_entry.get()
    if current_name == "":
        error_dict["error_bool"] = True
        error_dict["error_messages"][0] = "Le pseudo doit avoir au moins un caractère"
    else:
        donnees["name"] = current_name

    # Validation du mot de passe
    current_password = password_entry.get()
    if len(current_password) >= 8:
        donnees["password"] = current_password
    else:
        error_dict["error_bool"] = True
        error_dict["error_messages"][1] = "Le mot de passe doit contenir au moins 8 caractères."

    # Validation de l'âge
    current_age_input = age_bar.get()
    if not current_age_input.isdigit(): # Vérifie si la chaîne entière ne contient que des chiffres
        error_dict["error_bool"] = True
        error_dict["error_messages"][2] = "L'âge doit être sous format numérique."
    else:
        donnees["age"] = int(current_age_input)

    donnees["sexe"] = donnees["sexe"].get()

    # Mise à jour le texte des étiquettes d'erreur
    error_label0.configure(text=error_dict["error_messages"][0])
    error_label1.configure(text=error_dict["error_messages"][1])
    error_label2.configure(text=error_dict["error_messages"][2])

    # Gestion de la visibilité des étiquettes d'erreur dynamiquement
    if error_dict["error_messages"][0]: # S'il y a un message d'erreur du nom, afficher label0
        error_label0.grid(row=1, column=0, sticky=N, padx=10, columnspan=3)
    else:
        error_label0.grid_forget() # Masquer label1 s'il n'y a pas d'erreur

    if error_dict["error_messages"][1]: # S'il y a un message d'erreur de mot de passe, afficher label1
        error_label1.grid(row=3, column=0, sticky=N, padx=10, columnspan=3)
    else:
        error_label1.grid_forget() # Masquer label1 s'il n'y a pas d'erreur

    if error_dict["error_messages"][2]: # S'il y a un message d'erreur d'âge, afficher label2
        error_label2.grid(row=6, column=0, sticky=N, columnspan=3)
    else:
        error_label2.grid_forget() # Masquer label2 s'il n'y a pas d'erreur

    if not error_dict["error_bool"]:
        print("Formulaire soumis avec succès!")
        with open("data.json", "w") as f:
            dump(donnees, f)
    else:
        print("Erreurs de validation, veuillez corriger.")

def suppression(donnees):
    #Vider les champs
    password_entry.delete(0, END)
    age_bar.delete(0, END)
    name_entry.delete(0, END)
    donnees["sexe"].set(None)

#donnees du users
donnees = {
    "name" : "",
    "password" : "",
    "age" : 0,
    "sexe" : StringVar(value="")
}

error = {
    "error_bool" : False,
    "error_messages" : ["","",""]
}

#éléments de l'interface utilisateur
box = CTkFrame(windows, width=400, height=500, fg_color="#2B2B2B", bg_color="#333", corner_radius=20 , border_color="#41DA5D", border_width=1)
title = CTkLabel(box , text="FORMULAIRE", bg_color="#2B2B2B", text_color="white", font=("BOUNCY", 30, "bold"))
label_name = CTkLabel(box, text="Pseudo:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
name_entry = CTkEntry(box, width=230, height=20, corner_radius=0, border_width=0)
label_password = CTkLabel(box, text="Mot de passe:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
password_entry = CTkEntry(box, width=230, height=20, corner_radius=0, border_width=0, show="*")
label_sexe = CTkLabel(box, text="Sexe:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
m_radio = CTkRadioButton(box, variable=donnees["sexe"], value="male", text="M", text_color="white", fg_color="#41DA5D")
f_radio = CTkRadioButton(box, variable=donnees["sexe"], value="female", text="F", text_color="white", fg_color="#41DA5D")
label_age = CTkLabel(box, text="âge:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
age_bar = CTkEntry(box, width=50, corner_radius=0, border_color="#41DA5D", border_width=1)
#Utiliser lambda pour retarder l'appel de la fonction jusqu'au clic sur le bouton
reset_btn = CTkButton(box, width=50, height=30, text="Supprimer", corner_radius=10, bg_color="#2B2B2B", fg_color="#41DA5D", cursor="hand2", command=lambda: suppression(donnees))
submit_btn = CTkButton(box, width=50, height=30, text="S'inscrire", corner_radius=10, bg_color="#2B2B2B", fg_color="#41DA5D", cursor="hand2", command=lambda: soumission(donnees=donnees, error_dict=error))

# Étiquettes d'erreur initialement vides
error_label0 = CTkLabel(box, text="", bg_color="#2B2B2B", text_color="red", font=("LORA", 13))
error_label1 = CTkLabel(box, text="", bg_color="#2B2B2B", text_color="red", font=("LORA", 13))
error_label2 = CTkLabel(box, text="", bg_color="#2B2B2B", text_color="red", font=("LORA", 13))


#Application des éléments à l'écran
title.grid(pady=20, row=0, column=0, columnspan=3)
label_name.grid(row=2, column=0, padx=10, pady=10, sticky=W)
name_entry.grid(sticky=E, padx=10, pady=17, row=2, column=1, columnspan=2)
label_password.grid(sticky=W, padx=10, pady=10, row=4, column=0)
password_entry.grid(sticky=E, padx=10, pady=17, row=4, column=1, columnspan=2)
label_sexe.grid(row=5, column=0, padx=10, pady=10, sticky=W)
m_radio.grid(row=5, column=1, pady=15, sticky=W)
f_radio.grid(row=5, column=2, pady=15, sticky=E)
label_age.grid(sticky=W, padx=10, pady=10, row=7, column=0)
age_bar.grid(sticky=W, padx=10, pady=17, row=7, column=1)
reset_btn.grid(row=8, column=1, pady=10, sticky=E, columnspan=1)
submit_btn.grid(row=8, column=2, padx=10, pady=10, sticky=E, columnspan=1)
box.grid(row=0, column=0)

# Rend la box non redimensionnable
box.grid_propagate(False)
'''
box_2 = CTkFrame(windows, width=500, height=200, fg_color="#2B2B2B", bg_color="#333", corner_radius=20 , border_color="#41DA5D", border_width=1)
box_2.grid(row=0, column=0)
box_2.grid_propagate(False)
'''
# Centre la box
windows.grid_anchor(CENTER)

# Boucle de fonctionnement
windows.mainloop()