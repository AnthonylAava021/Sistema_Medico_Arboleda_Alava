from app import create_app
from app.configuracion_base import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada.")
    puerto = 5000
    print(f"API corriendo en http://127.0.0.1:{puerto}/docs")
    app.run(debug=True, port=puerto)
