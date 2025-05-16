from customtkinter import *
from _json import *

#paramtre de la fenetre
windows = CTk()
windows.title("Formulaire Python")
windows.geometry("720x550")
windows.config(bg="#333")

name = StringVar()
password = StringVar()
sexe= StringVar()

#create element
box = CTkFrame(windows, width=400, height=500, fg_color="#2B2B2B", bg_color="#333", corner_radius=20 , border_color="#41DA5D", border_width=1)
title = CTkLabel(box , text="FORMULAIRE", bg_color="#2B2B2B", text_color="white", font=("BOUNCY", 30, "bold"))
label_name = CTkLabel(box, text="Pseudo:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
name_entry = CTkEntry(box, width=230, height=20, corner_radius=0, border_width=0)
label_password = CTkLabel(box, text="Mot de passe:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
password_entry = CTkEntry(box, width=230, height=20, corner_radius=0, border_width=0, show="*")
label_sexe = CTkLabel(box, text="Sexe:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
m_radio = CTkRadioButton(box, variable=sexe, value="male", text="M", text_color="white", fg_color="#41DA5D")
f_radio = CTkRadioButton(box, variable=sexe, value="female", text="F", text_color="white", fg_color="#41DA5D")
label_age = CTkLabel(box, text="age:", bg_color="#2B2B2B", text_color="white", font=("LORA", 18))
age_bar = CTkEntry(box, width=230, fg_color="#41DA5D")
reset_btn = CTkButton(box, width=50, height=30, text="Supprimer", corner_radius=10, bg_color="#2B2B2B", fg_color="#41DA5D", cursor="hand2")
submit_btn = CTkButton(box, width=50, height=30, text="S'inscrire", corner_radius=10, bg_color="#2B2B2B", fg_color="#41DA5D", cursor="hand2")
#application des elements a l'ecran
title.grid(pady=20, row=0, column=0, columnspan=3)
label_name.grid(row=1, column=0, padx=10, pady=10, sticky=W)
name_entry.grid(sticky=E, padx=10, pady=17, row=1, column=1, columnspan=2)
label_password.grid(sticky=W, padx=10, pady=10, row=2, column=0)
password_entry.grid(sticky=E, padx=10, pady=17, row=2, column=1, columnspan=2)
label_sexe.grid(row=3, column=0, padx=10, pady=10, sticky=W)
m_radio.grid(row=3, column=1, pady=15, sticky=W)
f_radio.grid(row=3, column=2, pady=15, sticky=E)
label_age.grid(sticky=W, padx=10, pady=10, row=4, column=0)
age_bar.grid(sticky=E, padx=10, pady=17, row=4, column=1, columnspan=2)
reset_btn.grid(row=5, column=1, padx=10,  pady=10, sticky=SE, columnspan=1)
submit_btn.grid(row=5, column=2, padx=10, pady=10, sticky=SE, columnspan=1)
box.grid(row=0, column=0)
#rend la box non redimensionable
box.grid_propagate(False)
#centre la box
windows.grid_anchor(CENTER)

#boucle de fonctionnement
windows.mainloop()