import customtkinter as ctk
from services.services_salle import ServiceSalle
class ViewSalle (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")
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