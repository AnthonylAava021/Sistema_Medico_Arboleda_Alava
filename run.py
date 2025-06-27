from app import create_app
from app.configuracion_base import db  # Importa la instancia única

app = create_app()

if __name__ == "__main__":
    with app.app_context():  # Activa contexto para usar la app
        db.create_all()      # Ahora sí tiene acceso al engine vinculado
        print("Base de datos inicializada.")
    puerto = 5000
    print(f"API corriendo en http://127.0.0.1:{puerto}/docs")
    app.run(debug=True, port=puerto)
