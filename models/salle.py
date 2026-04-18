class Salle:
    def __init__(self, code, libelle, type, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type
        self.capacite = capacite
    def afficher_info(self):
        print(f"Code de la salle : {self.code}, libelle : {self.libelle}, type : {self.type}, sa capacité : {self.capacite}.")
