from flask import Flask
from config import SECRET_KEY, DEBUG
from controllers.db import init_db
from routes import bp

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(bp)

init_db()

if __name__ == "__main__":
    app.run(debug=DEBUG)
