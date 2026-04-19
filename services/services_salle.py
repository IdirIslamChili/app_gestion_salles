from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs doivent être remplis"

        if salle.capacite < 1:
            return False, "La capacité doit être >= 1"

        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès"

    def  modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs doivent être remplis"

        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès"