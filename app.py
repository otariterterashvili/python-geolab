from flask import Flask, render_template, request, redirect, url_for, session
import os
from flask_sqlalchemy import SQLAlchemy

# wrapp whole application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xwwfvfcisvelwv:1fb27fb94880dd2ed9a21e1b3b2dff53b40dba9f61331f6991344f07f22d8f16@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d117vqrngc069v"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.urandom(12)

db = SQLAlchemy(app)

# import all module
from iuda_app.auth.view import auth
from iuda_app.product.view import product

# import all models
from iuda_app.auth.model import User
from iuda_app.product.model import Product


# register bluprints
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(product, url_prefix="/product")

@app.route("/")
def index():
  is_login = session.get("is_login", False)
  if is_login == True:
    return render_template("home.html")
  else:
    return redirect(url_for("auth.login_page"))



if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run()


