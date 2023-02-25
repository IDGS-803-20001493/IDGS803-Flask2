from  wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FieldList, FormField, SelectField, RadioField

from wtforms.fields import EmailField
from wtforms import validators


def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.data_required(message='el campos es requerido'),
        validators.length(min=4,max=15,message='no cumple con la longitud del campo')
        ])
    nombre = StringField('Nombre',[validators.data_required(message='el campos es requerido')])
    apaterno = StringField('Apaterno', [mi_validacion])
    email=EmailField('Correo')

class LoginForm(Form):
    username=StringField('usuario',[
        validators.data_required(message='el campos es requerido'),
        validators.length(min=4,max=15,message='no cumple con la longitud del campo')
        ])
    password = StringField('password',[
        validators.data_required(message='el campos es requerido'),
        validators.length(min=4,max=15,message='no cumple con la longitud del campo')
        ])


class DiccionarioForm(Form):
    ingles=StringField('ingles',[
        validators.data_required(message='el campos es requerido'),
        validators.length(min=4,max=15,message='no cumple con la longitud del campo')
        ])
    español = StringField('español',[
        validators.data_required(message='el campos es requerido'),
        validators.length(min=4,max=15,message='no cumple con la longitud del campo')
        ])
