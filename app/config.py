#Conexión con la base de datos PostgreSQL
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:clave@localhost:5432/citasdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False