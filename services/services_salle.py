#Importation de la classe DataSalle depuis le fichier data
from data.dao_salle import DataSalle

#Création de la classe ServiceSalle
class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
#Ajout d'une méthode
    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs doivent être remplis"
        if salle.capacite < 1:
            return False, "La capacité doit être >= 1"
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès"

# Ajout d'une méthode
    def  modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs doivent être remplis"
        if salle.capacite < 1:
            return False, "Capacité invalide"
        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès"

# Ajout d'une méthode
    def supprimer_salle(self, code):
        if not code:
            return False, "Code invalide"
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée"

# Ajout d'une méthode
    def rechercher_salle(self, code):
        if not code:
            return  False, "Code invalide"
        self.dao_salle.get_salle (code)

# Ajout d'une méthode
    def recuperer_salles(self):
        return self.dao_salle.get_salles()