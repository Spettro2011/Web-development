from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def ciao_mondo():
    moneta = random.randint(0, 1)
    if moneta == 1:
        moneta = "Testa"
    else:
        moneta = "Croce"
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return render_template("gta.html",r=r,g=g,b=b,moneta=moneta)
@app.route("/iscritti")
def gta5():
    return '<a href="/"> torna alla pagina precedente</a><h1> ciao mondo</h1>'

app.run(debug=True)
