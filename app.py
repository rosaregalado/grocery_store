from grocery_app.extensions import app, db
from grocery_app.main.routes import main
app.register_blueprint(main)

from grocery_app.login.routes import auth
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
