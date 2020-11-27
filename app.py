from flask import Flask,render_template,request,redirect
from re import split
import main as main

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = './file'

logeada=False


@app.route('/',methods=["GET","POST"])
def default():
    if request.method == 'POST':
        code = request.form['code']
        if code != '':

            print(code)
            query = main.queryavector(code)
            query = main.normalizar_vector(query)

            resultado1 = main.seleccion_tweets(main.diccionario_tweets,query,main.scoring)

            resultado = main.obtener_texto(resultado1)
            print(resultado)
            return render_template("result-form.html",s=resultado,d = resultado1)

    return render_template("index.html")


if __name__ == '__main__':
    print("hello")
    app.run()
