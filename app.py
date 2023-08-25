from flask import Flask, render_template



app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/igreja/sobre')
def sobre_igreja():
    return render_template("A_Igreja.html")


@app.route('/grupos_reformados/')
def grupo_reformados():
    return render_template("grupos_reformados.html")


@app.route('/Cultos')
def Cultos():
    return render_template("Cultos.html")


@app.route('/igreja/sobre/equipe_pastoral')
def equipe_pastoral():
    return render_template('equipe_pastoral.html')


@app.route('/igreja/sobre/Dizimos_&_Ofertas')
def dizimo_ofertas():
    return render_template('Dizimos_&_Ofertas.html')

@app.route('/igreja/sobre/Ministerios')
def MInisterioss():
    return render_template('Ministerios.html')


if __name__ == '__main__':
    app.run()