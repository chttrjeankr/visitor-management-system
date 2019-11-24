from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class CheckInForm(FlaskForm):
    v_name = StringField('Visitor Name', validators=[DataRequired()])
    v_email = StringField('Visitor Email', validators=[DataRequired(),Email()])
    v_phone = StringField('Visitor Phone', validators=[DataRequired(),Length(10,10,"Enter 10 digit mobile number")])
    h_name = StringField('Host Name', validators=[DataRequired()])
    h_email = StringField('Host Email', validators=[DataRequired(),Email()])
    h_phone = StringField('Host Phone', validators=[DataRequired(),Length(10,10,"Enter 10 digit mobile number")])
    address = TextAreaField('Address', validators=[DataRequired()])
    submit = SubmitField('Check In')

class CheckOutForm(FlaskForm):
    timestamp = IntegerField('Enter Check-In ID', validators=[DataRequired()])
    submit = SubmitField('Check Out')
