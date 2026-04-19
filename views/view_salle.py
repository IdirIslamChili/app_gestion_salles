import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
class ViewSalle (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")

# cadre informations
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(padx=10, pady=10, fill="x")

        ctk.CTkLabel(self.frame_info, text="Code salle").grid(row=0, column=0, padx=5, pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_info)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_info, text="Libellé").grid(row=1, column=0, padx=5, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.frame_info)
        self.entry_libelle.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_info, text="Type").grid(row=2, column=0, padx=5, pady=5)
        self.entry_type = ctk.CTkEntry(self.frame_info)
        self.entry_type.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_info, text="Capacité").grid(row=3, column=0, padx=5, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.frame_info)
        self.entry_capacite.grid(row=3, column=1, padx=5, pady=5)

#cadre action
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(padx=10, pady=10, fill="x")
        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=5, pady=5)
        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=5, pady=5)
        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=5, pady=5)
        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=5, pady=5)
    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type, capacite)
        self.service_salle.ajouter_salle(salle)

        self.btn_ajouter.configure(command=self.ajouter_salle)

    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        self.service_salle.modifier_salle(code, libelle, type, capacite)

        self.btn_modifier.configure(command=self.modifier_salle)