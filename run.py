import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def show_pages():
    if request.method == 'POST':
        return render_template('result.html')
    else:
        return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
