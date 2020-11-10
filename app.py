from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return '<h2>Hello Ia</h2>'

@app.route("/company")
def get_all_comany():
  return '<ul><li><a href="/company/instagram">instagram</a></li><li><a href="/company/facebook">facebook</a></li><li><a href="/company/google">google</a></li></ul>'

@app.route("/company/<company_name>")
def get_company_page(company_name):

  return f'This is {company_name}<a href="/company">back to all company</a>'

if __name__ == "__main__":
  app.run()