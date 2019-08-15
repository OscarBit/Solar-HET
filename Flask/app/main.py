from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class parametersForm(FlaskForm):
    D_n = StringField('D_n', default='1.05', validators=[DataRequired()])
    D_p = StringField('D_p', default='0.65', validators=[DataRequired()])
    eps_p = StringField('eps_p', default='13.6', validators=[DataRequired()])
    eps_n = StringField('eps_n', default='10.0', validators=[DataRequired()])
    N_a = StringField('N_a', default='2.0e16', validators=[DataRequired()])
    N_d = StringField('N_d', default='1.0e17', validators=[DataRequired()])
    N_cp = StringField('N_cp', default='2.2e18', validators=[DataRequired()])
    N_vp = StringField('N_vp', default='1.8e19', validators=[DataRequired()])
    N_cn = StringField('N_cn', default='2.2e18', validators=[DataRequired()])
    N_vn = StringField('N_vn', default='1.8e19', validators=[DataRequired()])
    S_n = StringField('S_n', default='10.0', validators=[DataRequired()])
    S_p = StringField('S_p', default='1.0e7', validators=[DataRequired()])
    W_n = StringField('W_n', default='0.1e-4', validators=[DataRequired()])
    W_p = StringField('W_p', default='2.0e-4', validators=[DataRequired()])
    W_pmin = StringField('W_pmin', default='0.5e-4', validators=[DataRequired()])
    W_pmax = StringField('W_pmax', default='3.0e-4', validators=[DataRequired()])
    X_n = StringField('X_n', default='4.3', validators=[DataRequired()])
    X_p = StringField('X_p', default='4.235', validators=[DataRequired()])
    S_i = StringField('S_i', default='0', validators=[DataRequired()])
    Steps = StringField('Steps', default='30', validators=[DataRequired()])
    Vib_steps = StringField('Vib_steps', default='300', validators=[DataRequired()])
    L_n = StringField('L_n', default='.0e-4', validators=[DataRequired()])
    L_p = StringField('L_p', default='2.9e-6', validators=[DataRequired()])
    file_name = FileField('Spectrum Data', default='.xlsx', validators=[DataRequired()])
    fileR = FileField('Reflectance', default='.xls', validators=[DataRequired()])
    fileT = FileField('Transmittance', default='.xlsx', validators=[DataRequired()])
    file_name = FileField('Spectrum Data', validators=[DataRequired()])
    fileR = FileField('Reflectance', validators=[DataRequired()])
    fileT = FileField('Transmittance', validators=[DataRequired()])

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/graphics")
def graphics():
    return render_template('graphics.html')

@app.route("/parameters")
def parameters():
    form = parametersForm()
    if form.validate_on_submit():
        return 'Parameters submitted.'
    return render_template('form.html', form=form )