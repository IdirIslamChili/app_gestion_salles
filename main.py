from models.salle import Salle
from data.dao_salle import DataSalle

#connexion à la base de données
data_salle = DataSalle()
connexion = data_salle.get_connection()
print(connexion)

#Création des salles
sl1=Salle("C250","INF1010", "Laboratoire", 40)
sl2=Salle("C260","INF1011", "Classe", 38)
sl3=Salle("C240","ANG1011", "Classe", 22)
sl4=Salle("C210","MAT1011", "Classe", 25)

#Ajout des salles
dao = DataSalle()
dao.insert_salle(sl1)
dao.insert_salle(sl2)
dao.insert_salle(sl3)
dao.insert_salle(sl4)

#Suppression d'une salle avec son code
dao.delete_salle("C260")

#Modifier une salle
sl1_modifie = Salle("INF1010 Modifié", "Laboratoire", 45, "C250")
dao.update_salle(sl1_modifie)

#Rechercher d'une salle par son code
salle = dao.get_salle("C250")
if salle:
    salle.afficher_info()
else:
    print("Salle introuvable")

#Récupération et affichage de toutes les salles
salles = dao.get_salles()
if salles:
    print("Liste des salles :")
    for salle in salles:
        salle.afficher_info()
        print("-------------------")
else:
    print("Aucune salle trouvée")
