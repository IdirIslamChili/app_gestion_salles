import customtkinter as ctk
from models.salle import Salle
from tkinter import ttk

class ViewSalle (ctk.CTk):
    def __init__(self, service_salle):
        super().__init__()
        self.service_salle = service_salle

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
        self.btn_ajouter.configure(command=self.ajouter_salle)
        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=5, pady=5)
        self.btn_modifier.configure(command=self.modifier_salle)
        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=5, pady=5)
        self.btn_supprimer.configure(command=self.supprimer_salle)
        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=5, pady=5)
        self.btn_rechercher.configure(command=self.rechercher_salle)

# Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "libelle", "type", "capacite"),
                                     show="headings")

# En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

# Largeur des colonnes
        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()

    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)
        self.service_salle.ajouter_salle(salle)
        self.lister_salles()

    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)
        self.service_salle.modifier_salle(salle)
        self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()

        self.service_salle.supprimer_salle(code)
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)
        if salle :
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, salle.capacite)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert(
                "",
                "end",
                values=(s.code, s.libelle, s.type_salle, s.capacite)
            )