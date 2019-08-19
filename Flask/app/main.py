from app import app
import werkzeug.datastructures, numpy as np
from flask import render_template, request, redirect, url_for, Response
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
from matplotlib import pyplot as plt
k_B = 8.617332e-05
q = 1.6e-19
A = 100000.0
h = 4.135e-15
c = 30000000000.0
eps_0 = 8.8541e-14
wow = False
data_1, wlengthsQE, EQE, Vone, Jone, wlengths = ([], [], [], [], [], [])

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
    E_gn = StringField('E_gn', default='2.42', validators=[DataRequired()])
    E_gp = StringField('E_gp', default='1.17', validators=[DataRequired()])
    X_n = StringField('X_n', default='4.3', validators=[DataRequired()])
    X_p = StringField('X_p', default='4.235', validators=[DataRequired()])
    S_i = StringField('S_i', default='0', validators=[DataRequired()])
    Steps = StringField('Steps', default='30', validators=[DataRequired()])
    Vib_steps = StringField('Vib_steps', default='20', validators=[DataRequired()])
    L_n = StringField('L_n', default='8.0e-4', validators=[DataRequired()])
    L_p = StringField('L_p', default='2.9e-6', validators=[DataRequired()])
    file_name = FileField('Spectrum Data', default='.xlsx', validators=[DataRequired()])
    fileR = FileField('Reflectance', default='', validators=[DataRequired()])
    fileT = FileField('Transmittance', default='', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/parameters', methods=['GET', 'POST'])
def parameters():
    request.parameter_storage_class = werkzeug.datastructures.ImmutableOrderedMultiDict
    form = parametersForm()
    alpha_n, alpha_p, wlengths, N_0, R, T, hv = np.empty((7, 0), dtype=(np.float_))
    if request.method == 'POST':
        req = request.form
        Ta = 300
        E_gn = np.float_(req.get('E_gn'))
        E_gp = np.float_(req.get('E_gp'))
        D_n = np.float_(req.get('D_n'))
        D_p = np.float_(req.get('D_p'))
        eps_p = np.float_(req.get('eps_p'))
        eps_n = np.float_(req.get('eps_n'))
        N_a = np.float_(req.get('N_a'))
        N_d = np.float_(req.get('N_d'))
        N_cp = np.float_(req.get('N_cp'))
        N_vp = np.float_(req.get('N_vp'))
        N_cn = np.float_(req.get('N_cn'))
        N_vn = np.float_(req.get('N_vn'))
        S_n = np.float_(req.get('S_n'))
        S_p = np.float_(req.get('S_p'))
        W_n = np.float_(req.get('W_n'))
        W_p = np.float_(req.get('W_p'))
        W_pmin = np.float_(req.get('W_pmin'))
        W_pmax = np.float_(req.get('W_pmax'))
        X_n = np.float_(req.get('X_n'))
        X_p = np.float_(req.get('X_p'))
        S_i = np.float_(req.get('S_i'))
        Steps = np.float_(req.get('Steps'))
        Vib_steps = np.float_(req.get('Vib_steps'))
        L_n = np.float_(req.get('L_n'))
        L_p = np.float_(req.get('L_p'))
        fff = request.files.get('file_name')
        waiter = 0
        wait = 100 / Steps
        specdata = np.loadtxt(fff, dtype=(np.float_), usecols=(0, 1), skiprows=0)
        wlengthsneq = specdata[:, 0]
        N_0neq = specdata[:, 1]
        Rneq = np.loadtxt((request.files['fileR']), dtype=(np.float_), usecols=(1, ), skiprows=1)
        Tneq = np.loadtxt((request.files['fileT']), dtype=(np.float_), usecols=(1, ), skiprows=1)
        nn = min(len(Rneq), len(Tneq), len(wlengthsneq))
        from app import SolarHetBasic
        R, T, wlengths, hv, N_0, V_bi, alpha_n, alpha_p = SolarHetBasic.valvalues(Ta, E_gn, E_gp, D_n, D_p, eps_p, eps_n, N_a, N_d, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, W_pmin, W_pmax, X_n, X_p, S_i, Steps, Vib_steps, L_n, L_p, wlengthsneq, N_0neq, Rneq, Tneq, nn)
        globals()['wlengths'] = wlengths
        globals()['R'] = R
        globals()['T'] = T
        thickness = np.linspace(W_pmin, W_pmax, num=Steps, endpoint=True)
        gap = np.linspace(1.0, 2.0, num=Steps, endpoint=True)
        Efi_list, Voc_list, FF_list, Jsc_list = ([], [], [], [])
        voltage = np.linspace(0, V_bi, num=(Vib_steps * 2), endpoint=True)
        V_oc, FF, Efi, J_sc = (0, 0, 0, 0)
        Jone, Vone = [], []
        for n in range(len(voltage)):
            j = SolarHetBasic.Jcell(voltage[n])
            if j <= 0:
                pass
            else:
                Jone.append(j)
                Vone.append(voltage[n])

        aa = voltage[(len(Vone) - 1)]
        bb = Jone[(len(Vone) - 1)]
        cc = voltage[len(Vone)]
        dd = SolarHetBasic.Jcell(voltage[len(Vone)])
        V_oc = SolarHetBasic.Voc(aa, bb, cc, dd)
        Vone.append(V_oc)
        Jone.append(0.0)
        globals()['Vone'] = np.array(Vone, dtype=(np.float_))
        globals()['Jone'] = np.array(Jone, dtype=(np.float_))
        Efi = max(np.multiply(Jone, Vone))
        J_sc = max(Jone)
        FF = 100 * Efi / (V_oc * J_sc)
        print('\n', 'Results for input parameters:', '\n', 'Efficiency: ', Efi, 'Voc: ', V_oc, 'Jsc: ', J_sc, 'FF: ', FF, '\n')
        print('[', '*' * int(waiter), '-' * int(100 - waiter), ']')
        for WW in thickness:
            V_oc, FF, Efi, J_sc = (0, 0, 0, 0)
            W_p = SolarHetBasic.rolling(WW)
            jcell, v = [], []
            for n in range(len(voltage)):
                j = SolarHetBasic.Jcell(voltage[n])
                if j <= 0:
                    pass
                else:
                    jcell.append(j)
                    v.append(voltage[n])

            aa = voltage[(len(v) - 1)]
            bb = jcell[(len(v) - 1)]
            cc = voltage[len(v)]
            dd = SolarHetBasic.Jcell(voltage[len(v)])
            V_oc = SolarHetBasic.Voc(aa, bb, cc, dd)
            v.append(V_oc)
            jcell.append(0.0)
            Efi = max(np.multiply(jcell, v))
            J_sc = max(jcell)
            FF = 100 * Efi / (V_oc * J_sc)
            Efi_list.append(Efi)
            Voc_list.append(V_oc)
            Jsc_list.append(J_sc)
            FF_list.append(FF)
            waiter += wait
            print('[', '*' * int(waiter), '-' * int(100 - waiter), ']')

        data_1 = [
         thickness, Efi_list, Voc_list, FF_list, Jsc_list]
        globals()['data_1'] = np.array(data_1, dtype=(np.float_))
        EQE0 = SolarHetBasic.dJ_ph(0) * 10 / N_0
        IQE0 = EQE0 / (1.0 - R)
        wlengthsQE = []
        EQE = []
        IQE = []
        for i in range(len(EQE0)):
            if EQE0[i] == 0:
                pass
            else:
                EQE.append(EQE0[i])
                wlengthsQE.append(wlengths[i])
                IQE.append(IQE0[i])

        globals()['wlengthsQE'] = np.array(wlengthsQE, dtype=(np.float_))
        globals()['EQE'] = np.array(EQE, dtype=(np.float_))
        globals()['IQE'] = np.array(IQE, dtype=(np.float_))
        globals()['wow'] = True
        return redirect(url_for('graphs'))
    else:
        return render_template('form.html', form=form)


@app.route('/jccurve', methods=['GET', 'POST'])
def graphs():
    if wow == True:
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot(Vone, Jone, linewidth=0.8)
        plt.plot(Vone, Jone, 'o', linewidth=0.8)
        plt.xlabel('Voltage [V]', {'fontsize': 8})
        plt.ylabel('Current density [mA/cm²]', {'fontsize': 8})
        plt.title('Current Voltage Curve', {'fontsize': 10})
        plt.grid(True)
        plt.savefig('app\\static\\img\\JV8-300dpi.png', format='png')
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot(wlengthsQE, EQE, label='EQE', linewidth=0.8)
        plt.plot(wlengthsQE, IQE, label='IQE', linewidth=0.8)
        plt.xlabel('Wave length [nm]', {'fontsize': 8})
        plt.ylabel('QE', {'fontsize': 8})
        plt.title('Quantum Efficciency', {'fontsize': 10})
        plt.legend(loc='best')
        plt.grid(True)
        plt.savefig('app\\static\\img\\QE8-300dpi.png', format='png')
        fig, ax1 = plt.subplots(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        ax1.set_xlabel('Wave length [nm]', {'fontsize': 8})
        ax1.set_ylabel('Transmittance [%]', {'fontsize': 8})
        ax1.plot(wlengths, T, label='Transmittance TCO', linewidth=1.2)
        ax1.tick_params(axis='y')
        ax2 = ax1.twinx()
        ax2.set_ylabel('Reflectance [%]', {'fontsize': 8})
        ax2.plot(wlengths, R, label='Reflectance CIGS', linewidth=1.2, color='g')
        ax2.tick_params(axis='y')
        fig.tight_layout()
        ax1.grid(True)
        fig.legend(loc='center', fontsize='small')
        plt.savefig('app\\static\\img\\RT8-300dpi.png', format='png')
        return render_template('graphic.html', url='app\\static\\img\\JV8-300dpi.png')
    else:
        return render_template('graphics.html')


@app.route('/jsc')
def graphjsc():
    if wow == True:
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot((data_1[0] * 1.0e8), (data_1[4]), linewidth=0.8)
        plt.plot(data_1[0] * 1.0e8, data_1[4], 'o')
        plt.xlabel('Thickness [nm]', {'fontsize': 8})
        plt.ylabel('$J_{sc}$ [mA/cm$^{2}$]', {'fontsize': 8})
        plt.title('Short-circuit current density', {'fontsize': 10})
        plt.grid(True)
        plt.savefig('app\\static\\img\\Jsc8-300dpi.png', format='png')
        return render_template('jsc.html')
    else:
        return render_template('graphics.html')


@app.route('/voc')
def graphvoc():
    if wow == True:
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot((data_1[0] * 1.0e8), (data_1[2]), linewidth=0.8)
        plt.plot(data_1[0] * 1.0e8, data_1[2], 'o')
        plt.xlabel('Thickness [nm]', {'fontsize': 8})
        plt.ylabel('$V_{oc}$ [mV]', {'fontsize': 8})
        plt.title('Open-circuit voltage', {'fontsize': 10})
        plt.grid(True)
        plt.savefig('app\\static\\img\\Voc8-300dpi.png', format='png')
        return render_template('voc.html')


@app.route('/ff')
def graphff():
    if wow == True:
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot((data_1[0] * 1.0e8), (data_1[3]), linewidth=0.8)
        plt.plot(data_1[0] * 1.0e8, data_1[3], 'o')
        plt.xlabel('Thickness [nm]', {'fontsize': 8})
        plt.ylabel('FF [%]', {'fontsize': 8})
        plt.title('Fill factor', {'fontsize': 10})
        plt.grid(True)
        plt.savefig('app\\static\\img\\FF8-300dpi.png', format='png')
        return render_template('ff.html')
    else:
        return render_template('graphics.html')


@app.route('/efficiency')
def grapheffi():
    if wow == True:
        plt.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
        plt.plot((data_1[0] * 1.0e8), (data_1[1]), linewidth=0.8)
        plt.plot(data_1[0] * 1.0e8, data_1[1], 'o')
        plt.xlabel('Thickness [nm]', {'fontsize': 8})
        plt.ylabel('$\\eta$ [%]', {'fontsize': 8})
        plt.title('Efficiency', {'fontsize': 10})
        plt.grid(True)
        plt.savefig('app\\static\\img\\Effi8-300dpi.png', format='png')
        return render_template('efficiency.html')
    else:
        return render_template('graphics.html')
