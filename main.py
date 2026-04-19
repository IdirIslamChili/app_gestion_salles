from models.salle import Salle
from data.dao_salle import DataSalle

data_user = DataSalle()
con = data_user.get_connection()
print(con)