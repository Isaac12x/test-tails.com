from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from main.app.api_utils import PostcodeFinder


class NewStoreForm(FlaskForm):
    name = StringField("Store neigborhood", validators=[DataRequired()])
    postcode = StringField("Postcode", validators=[DataRequired()])
    submit = SubmitField("Add")
