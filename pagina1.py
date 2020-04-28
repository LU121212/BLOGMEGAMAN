from flask import Flask,render_template # llamando al framework

app= Flask(__name__)#definimos el nombre de la variable
@app.route('/') # para ir a la url
def home(): #una vez establecida la ruta establecemos los define
    return render_template("index.html")

@app.route('/about')
def about(): #una funcion que va a manejar la ruta por usa usa el define
    return render_template("home.html")    

if __name__== "__main__": #se jecuta el archivo principal y no un modulo
    app.run(debug=True) #cada cambio que haga se actualiza solo

