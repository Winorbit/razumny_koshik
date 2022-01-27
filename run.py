import os
from flask import Flask, render_template, request, send_from_directory
from settings import product_category, products
from select_cheepest_product import select_all_cheepest_product_by_categories

app = Flask(__name__, template_folder="templates")


def take_user_input(page):
    address = page.form.get("address")
    money = page.form.get("money")
    categories = page.form.getlist("category")
    user_input = {
        "address": address,
        "money": money,
        "categories": categories
    }
    return user_input


@app.route("/", methods=["get", "post"])
def show_pages():
    if request.method == 'POST':
        user_input = take_user_input(request)
        print(user_input["categories"])  # for testing result
        products = select_all_cheepest_product_by_categories(user_input["categories"])
        return render_template('result.html', products=products)
    else:
        return render_template('index.html', product_category=product_category)


@app.route('/favicon')
def show_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/map')
def show_map():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'map.png', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
