from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Property_Form(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])
    bedrooms = StringField("Number of Bedrooms", validators=[InputRequired()])
    bathrooms = StringField("Number of Bathrooms", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    price = StringField("Price", validators=[InputRequired()])
    type = SelectField("Property Type", validators=[InputRequired()], choices=[('H','House'),('A','Apartment')])
    photo = FileField("Photo of Property", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Images only!')])