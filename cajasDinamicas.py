from flask import Flask, render_template
from flask import request
from collections import Counter

import forms

app = Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    alumn_form = forms.UserForm(request.form)
    if request.method == 'POST':
        print(alumn_form.matricula.data)
        print(alumn_form.nombre.data)
    return render_template('Alumnos.html', form=alumn_form)








@app.route("/cajasDinamicas", methods=['GET', 'POST'])
def cajasDinamicas():
    if request.method == 'POST':
        cantidad = int(request.form.get('txtCantidad'))
        return render_template('cajasDinamicas.html', cantidad = cantidad)
    else:
        return render_template('cajasDinamicas.html', cantidad = 0)



@app.route("/cajasDinamicasResultado", methods=['POST'])
def cajasDinamicasResultado():
    cantidadcajas = request.form.get('txtcantidadOculta')
    lista = []

    for i in range(1, int(cantidadcajas)+1):
        valor = int(request.form.get('caja'+str(i)))
        lista.append(valor)

    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista)/int(cantidadcajas)

    contador = Counter(lista)
    
    return render_template('cajasDinamicasResultado.html', maximo = str(maximo), minimo = str(minimo), promedio = str(promedio), contador = contador, lenCont = len(contador))

if __name__ == "__main__":
    app.run(debug=True)
