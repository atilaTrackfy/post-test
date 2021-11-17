from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    print(request.form['foo'])
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
