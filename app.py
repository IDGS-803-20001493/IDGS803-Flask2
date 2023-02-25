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
    return render_template('Act1_Diccionario.html',  form=form_lenguaje)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug = True)

