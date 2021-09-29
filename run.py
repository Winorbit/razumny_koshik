from flask import Flask, render_template, request
from settings import products



app = Flask(__name__, template_folder = "templates")

@app.route("/", methods = ["get", "post"])
def show_pages():
    if request.method == 'POST':
	    return render_template('result.html', products=products)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

