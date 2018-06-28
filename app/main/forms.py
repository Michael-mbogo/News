from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):

    title = StringField('Search source',validators=[Required()])
    search = TextAreaField('Category',validators=[Required()])
    submit = SubmitField('Submit')
