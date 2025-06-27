#Conexión con la base de datos PostgreSQL
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://citas:anthony@localhost:5432/citasdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False