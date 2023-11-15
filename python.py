from flask import Flask, render_template, request

app = Flask(__name__)

# Sample products
products = [
    {"name": "", "category": ""},
    {"name": "", "category": ""},
    # Add more products as needed
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/filter", methods=["POST"])
def filter_products():
    category = request.form.get("category")
    sorted_option = request.form.get("sort")

    filtered_products = filter_by_category(products, category)
    sorted_products = sort_products(filtered_products, sorted_option)

    return render_template("product_list.html", products=sorted_products)

def filter_by_category(products, category):
    if category == "all":
        return products
    return [product for product in products if product["category"] == category]

def sort_products(products, sort_option):
    return sorted(products, key=lambda x: x["name"], reverse=(sort_option == "desc"))

if __name__ == "__main__":
    app.run(debug=True)
