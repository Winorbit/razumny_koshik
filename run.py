import os
from flask import Flask, render_template, request, send_from_directory
from settings import products

app = Flask(__name__, template_folder="templates")

def take_user_input(resuest):
    address = request.form.get("address")
    money = request.form.get("money")
    categories = request.form.getlist("category")
    user_input={
        "address": address,
        "money": money,
        "categories": categories
        }
    return user_input

@app.route("/", methods=["get", "post"])
def show_pages():
    if request.method == 'POST':
        user_input=take_user_input(request)
        print(user_input)#for testing result
        return render_template('result.html', products=products)
    else:
        return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
