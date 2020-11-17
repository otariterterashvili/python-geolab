from flask import Blueprint, request, render_template, redirect, url_for, session

auth = Blueprint("auth", __name__, template_folder="templates")

user_data = [
  {"email": "oto@gmail.com", "password": "oto12345" },
  {"email": "ia@gmail.com", "password": "ia12345" }
]

@auth.route("/")
def auth_home():
  return redirect(url_for("auth.login_page"))

@auth.route("/sign-in", methods=['GET', 'POST'])
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

@auth.route("/logout")
def logout():
  session["is_login"] = False
  return redirect(url_for("auth.login_page"))
