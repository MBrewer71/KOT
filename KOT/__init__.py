from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()

@app.route('/charselect', methods=['GET', 'POST'])
def charselect():
    if request.method=='GET':
       return render_template("charselect.html")
    return redirect(url_for('main'))

@app.route('/game', methods=['GET','POST'])
def  game():
    if request.method=='GET':
        return render_template("game.html")
    return redirect(url_for('main'))    