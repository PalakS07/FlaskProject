# Importing website folder and the Flask app that we created
from website import create_app

app = create_app()

if __name__ == "__main__":  # type: ignore
    app.run(debug=True)  
