import json
import mysql.connector
from models.salle import Salle
class DataSalle:
    def __init__(self):
        pass
    def get_connection(self):
        with open ("./data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion

    def insert_salle(self, salle):
        connexion = self.get_connection()
        crs = connexion.cursor()
        crs.execute(
            "INSERT INTO salle VALUES(%s,%s,%s,%s)",
            (salle.code, salle.libelle, salle.type, salle.capacite)
        )
        connexion.commit()
        print("Insertion OK :", salle.code)
        crs.close()
        connexion.close()

    def update_salle(self, salle):
        connexion = self.get_connection()
        crs = connexion.cursor()
        crs.execute(
            """
                UPDATE salle
                SET libelle = %s,
                    type = %s,
                    capacite = %s
                WHERE code = %s
            """,
            (salle.code, salle.libelle, salle.type, salle.capacite)
            )
        connexion.commit()
        crs.close()
        connexion.close()

    def delete_salle(self, code):
        connexion = self.get_connection()
        crs = connexion.cursor()
        crs.execute(" DELETE FROM salle WHERE code = %s", (code,)
        )
        connexion.commit()
        crs.close()
        connexion.close()

    def get_salle(self, code):
        connexion = self.get_connection()
        crs = connexion.cursor()
        crs.execute("SELECT * FROM salle WHERE code = %", (code,))

        resultat = crs.fetchone()

        connexion.commit()
        crs.close()
        connexion.close()

        if resultat:
            return Salle(*resultat)
        else:
            return None

    def get_salles(self):
        connexion = self.get_connection()
        crs = connexion.cursor()
        crs.execute("SELECT * FROM salle")
        resultat = crs.fetchall()

        salles = []
        for row in resultat:
            salles.append(Salle(*row))

        connexion.commit()
        crs.close()
        connexion.close()

        return salles