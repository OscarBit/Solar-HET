from app import app
import werkzeug.datastructures
import numpy as np
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
from io import BytesIO
from tensorflow.python.lib.io import file_io

k_B = 8.617332e-5 #[eV/K]
q = 1.6e-19 #[C] 4.803e−10[statC]
A = 1e5
h = 4.135e-15 #[eV s]6.626e34[J s]
c = 3e10 #[cm/s]
eps_0 = 8.8541e-14

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
    fileR = FileField('Reflectance', default='', validators=[DataRequired()])
    fileT = FileField('Transmittance', default='', validators=[DataRequired()])

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/parameters", methods=['GET', 'POST'])
def parameters():
    request.parameter_storage_class = werkzeug.datastructures.ImmutableOrderedMultiDict
    form = parametersForm()
    if request.method == "POST":
        req = request.form
        D_n = np.float_(req.get("D_n"))
        D_p = np.float_(req.get("D_p"))
        eps_p = np.float_(req.get("eps_p"))
        eps_n = np.float_(req.get("eps_n"))
        N_a = np.float_(req.get("N_a"))
        N_d = np.float_(req.get("N_d"))
        N_cp = np.float_(req.get("N_cp"))
        N_vp = np.float_(req.get("N_vp"))
        N_cn = np.float_(req.get("N_cn"))
        N_vn = np.float_(req.get("N_vn"))
        S_n = np.float_(req.get("S_n"))
        S_p = np.float_(req.get("S_p"))
        W_n = np.float_(req.get("W_n"))
        W_p = np.float_(req.get("W_p"))
        W_pmin = np.float_(req.get("W_pmin"))
        W_pmax = np.float_(req.get("W_pmax"))
        X_n = np.float_(req.get("X_n"))
        X_p = np.float_(req.get("X_p"))
        S_i = np.float_(req.get("S_i"))
        Steps = np.float_(req.get("Steps"))
        Vib_steps = np.float_(req.get("Vib_steps"))
        L_n = np.float_(req.get("L_n"))
        L_p = np.float_(req.get("L_p"))
        Rneq = np.loadtxt(request.files['fileR'], dtype=np.float_, usecols=(1,), skiprows=1)
        Tneq = np.loadtxt(request.files['fileT'], dtype=np.float_, usecols=(1,), skiprows=1)
        fff = request.files['file_name'].read()
        f = BytesIO(file_io.read_file_to_string(fff, binary_mode=True))
        datafono = np.load(f)
        wlengthsneq = np.loadtxt(datafono, dtype=np.float_, usecols=(0,), skiprows=1)
        N_0neq = np.loadtxt(datafono, dtype=np.float_, usecols=(1,), skiprows=0)
        wlengths, N_0, R, T, hv = [], [], [], [], []
        print(len(fff))#len(Rneq), len(Tneq), len(wlengthsneq), 

        return render_template('graphics.html')

    return render_template('form.html', form=form )