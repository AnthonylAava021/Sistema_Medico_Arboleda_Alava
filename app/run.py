from app import create_app

app = create_app()
#Correr la Api
if __name__ == '__main__':
    app.run(debug=True)
