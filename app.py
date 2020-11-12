from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(12)

user_data = [
  {"email": "oto@gmail.com", "password": "oto12345" },
  {"email": "ia@gmail.com", "password": "ia12345" }
]

@app.route("/")
def index():
  is_login = session.get("is_login", False)
  if is_login == True:
    return render_template("home.html")
  else:
    return redirect(url_for("login_page"))

@app.route("/sign-in", methods=['GET', 'POST'])
def login_page():
  method = request.method

  error_msg = ""
  if method == "POST":
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    print(email, password)
    if email and password:
      for user in user_data:
        if user.get("email") == email and user.get("password") == password:
          session["is_login"] = True
          session["user_email"] = email
          return redirect(url_for("index"))
        else:
          error_msg = "Invalid credentional"
          render_template("login.html", error_msg=error_msg)
    else:
      error_msg = "Please fill all field"
      render_template("login.html", error_msg=error_msg)

  return render_template("login.html", error_msg=error_msg)

@app.route("/logout")
def logout():
  session["is_login"] = False
  return redirect(url_for("login_page"))





if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run()


