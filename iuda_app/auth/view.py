from flask import Blueprint, request, render_template, redirect, url_for, session
from app import db
from .model import User

auth = Blueprint("auth", __name__, template_folder="templates")

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
      # get user from user table where user.email = email
      user = User.query.filter_by(email=email).first()
      # serilize user data
      user = user.serilize()
      
      if user.get("password") == password:
        session["is_login"] = True
        session["user_name"] = user.get("name")
        return redirect(url_for("index"))
      else:
        error_msg = "Invalid credentional"
        render_template("login.html", error_msg=error_msg)
    else:
      error_msg = "Please fill all field"
      render_template("login.html", error_msg=error_msg)

  return render_template("login.html", error_msg=error_msg)

@auth.route("/sign-up", methods=['GET', 'POST'])
def register_user():
  method = request.method
  error_msg = ""
  if method == "POST":
    name = request.form.get("name", "")
    email = request.form.get("email")
    password = request.form.get("password", "")
    print("password", password)
    if email == None or email == "":
      error_msg = "Email is not provied"
      return render_template("register.html", error_msg=error_msg)
    elif len(password) < 6:
      error_msg = "Password is too short"
      return render_template("register.html", error_msg=error_msg)
    
    try:
      user_model = User(name, email, password)
      db.session.add(user_model)
      db.session.commit()
      return redirect(url_for("auth.login_page"))

    except Exception as e:
      print(e)
      return "server error"


  return render_template("register.html")


@auth.route("/logout")
def logout():
  session["is_login"] = False
  return redirect(url_for("auth.login_page"))
