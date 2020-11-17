from flask import Flask, render_template, request, redirect, url_for, session
import os
# import all module
from iuda_app.auth.view import auth
from iuda_app.product.view import product

# wrapp whole application
app = Flask(__name__)

app.secret_key = os.urandom(12)

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


