from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["get", "post"])
def show_pages():
    if request.method == 'POST':
	    return render_template('result.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

