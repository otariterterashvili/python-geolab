from flask import Blueprint, request, url_for, render_template

# create product bluprint. tempalte_folder = ./templates 
product = Blueprint("product", __name__, template_folder="templates")

product_data = [
  {
    "id": 1,
    "name": "Iphone 12", 
    "description": "This is the best phone",
    "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-max-blue-hero?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1604021658000" 
  },
  {
    "id": 2,
    "name": "Iphone 11 Pro", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.",
    "img": "https://icity.ge/wp-content/uploads/2020/04/iphone-11-pro-max-space-select-2019.png" 
  }
]

# product index route
@product.route("/")
def product_home():
  return render_template("products.html", products=product_data)

@product.route("/add-product")
def add_product(): 
  return "Add prodcut"

@product.route("/<int:id>")
def get_product(id):
  for prod_element in product_data:
    if prod_element.get("id") == id:
      return render_template("product.html", product=prod_element)
  
  return "<h1>Product not founded</h1>"
  