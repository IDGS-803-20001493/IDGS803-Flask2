from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash


import forms
app = Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf=CSRFProtect()

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'),404


@app.route("/cookies", methods=['GET','POST'])
def cookies():
    reg_user=forms.LoginForm(request.form)
    datos=''

    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos=user+'@'+password

        succes_message="Bienvenido {}".format(user)
        flash(succes_message)

    response = make_response(render_template('cookies.html', form=reg_user))
    if len(datos)>0:
        response.set_cookie("datos_user", datos)

    return response


@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get('datos_user')
    nombres =valor_cookie.split('@')
    return render_template('saludo.html', nom=nombres[0])


@app.route("/resistencia",methods=['GET','POST'])
def resistencia():
    historial=request.cookies.get('ultimaResistencia')

    if request.method=='POST':
        
        colores = ['black','chocolate','red','orangered','yellow','green','blue','purple','gray','white']
        tolerancia = ['goldenrod', 'silver']

        primerBanda = int(request.form.get('primerBanda'))
        segundaBanda = int(request.form.get('segundaBanda'))
        tercerBanda = int(request.form.get('tercerBanda'))
        cuartaBanda = int(request.form.get('cuartaBanda'))

        porcentajeTolerancia=int(10)
        if cuartaBanda == 0:
            porcentajeTolerancia=int(5)

        total = str(primerBanda) + "" + str(segundaBanda) + str( '0' * tercerBanda) 

        minimo = int(int(total) * (1 - (int(porcentajeTolerancia) / 100)))
        maximo = int(int(total) * (1 + (int(porcentajeTolerancia) / 100)))

        response = make_response(
            render_template('Act2_Resistencias.html', total=total + "Ω Ohms "+ str(porcentajeTolerancia) + "%",
                               minimo=minimo,maximo=maximo,
                               primero=str(primerBanda), segundo=str(segundaBanda),
                               tercero=str(tercerBanda),cuarto=str(cuartaBanda),
                               primerColor=colores[primerBanda],segundoColor=colores[segundaBanda],
                               tercerColor=colores[tercerBanda], cuartoColor=tolerancia[cuartaBanda],
                               historial = historial))
        
        response.set_cookie("ultimaResistencia", total + "Ω Ohms "+ str(porcentajeTolerancia) + "%")

        return response
    else:
        
        return render_template('Act2_Resistencias.html', total=0 ,minimo=0,maximo=0, historial=historial)


   




@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)

    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
        
    return render_template('Alumnos.html', form=alum_form)









@app.route("/guardar", methods=['GET','POST'])
def guardar():
    
    form_lenguaje = forms.DiccionarioForm(request.form)
    
    if form_lenguaje.validate():
        español=str(form_lenguaje.español.data).upper()
        ingles=str(form_lenguaje.ingles.data).upper()

        e=open('español.txt','a')
        e.write(español + ",")
        e.close()

        i=open('ingles.txt','a')
        i.write(ingles+ ",")
        i.close()

        succes_message="Se ha registrado correctamente"
        flash(succes_message)
    
    return render_template('Act1_Diccionario.html',  form=form_lenguaje)

@app.route("/busqueda", methods=['GET','POST'])
def busqueda():
    
    filtro = str(request.form.get('txtFiltro')).upper()
    idioma = str(request.form.get('btnLenguaje'))

    form_lenguaje = forms.DiccionarioForm(request.form)

    with open("español.txt", "r") as español:
        contenidoEspañol = español.read()

    listaEspañol = contenidoEspañol.split(",")
    listaEspañol = [elemento.strip() for elemento in listaEspañol]

    with open("ingles.txt", "r") as ingles:
        contenidoIngles = ingles.read()

    listaIngles = contenidoIngles.split(",")
    listaIngles = [elemento.strip() for elemento in listaIngles]

    resultado = "No hubo coincidencias"

    if idioma == "Ingles":
        if filtro in listaEspañol:
            posicion = str(listaEspañol.index(filtro))
            resultado = listaIngles[int(posicion)]

    if idioma == "Español":
        if filtro in listaIngles:
            posicion = str(listaIngles.index(filtro))
            resultado = listaEspañol[int(posicion)]

           
    return render_template('Act1_Diccionario.html',  form=form_lenguaje, resultado = resultado)



if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug = True)

