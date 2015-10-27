from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('enter name', validators=[Required()])
    submit = SubmitField('submit')


