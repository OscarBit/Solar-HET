import numpy as np
import xlrd
from matplotlib import pyplot 
from scipy import integrate
from matplotlib.backends.backend_pdf import PdfPages

#Constants Boltzmann constant, electron charge, Temperature, electrostatic field?, 

k_B = 8.617332e-5 #[eV/K]
q = 1.6e-19 #[C] 4.803e−10[statC]
A = 1e5
h = 4.135e-15 #[eV s]6.626e34[J s]
c = 3e10 #[cm/s]
eps_0 = 8.8541e-14
#Read parameters file
file_name = 'ESAM.xlsx'
fileR = 'REFLECTANCE.xls'
fileT = 'Transmitancia.xlsx'
D_n = np.float_(1.05)
D_p = np.float_(0.65)
eps_p = np.float_(13.6)
eps_n = np.float_(10)
N_a = np.float_(2.0e16)
N_d = np.float_(1.0e17)
E_gn = np.float_(2.42)
E_gp = np.float_(1.17)#me recuerda entonces
E_gpmin = np.float_(1.0)
E_gpmax = np.float_(2.0)
N_cp = np.float_(2.2e18)
N_vp = np.float_(1.8e19)
N_cn = np.float_(2.2e18)
N_vn = np.float_(1.8e19)
S_n = np.float_(10)
S_p = np.float_(1.0e7)
W_n = np.float_(0.1e-4)
W_p = np.float_(2.0e-4)
W_pmin = np.float_(0.5e-4)
W_pmax = np.float_(3.0e-4)
X_n = np.float_(4.3)
X_p = np.float_(4.235)
Ta = np.float_(300)
S_i = np.float_(0)
Steps = int(30)
Vib_steps = 300
L_n = 8.0e-4
L_p = 2.9e-6
waiter = 0
wait = 100/Steps
tau_n =  L_n ** 2 / D_n 
tau_p =  L_p ** 2 / D_p

#read the data of ASTM G173-03 Reference Spectra Derived from SMARTS v. 2.9.2

#input('\\nName of file whit reflectance data [NAME.xls]: ') 
#'REFLECTANCE.xls'
book2 = xlrd.open_workbook(fileR)
#input('\\nName of file whit Transmittance data [NAME.xls]: ') 
#'Transmitancia.xlsx'
book3 = xlrd.open_workbook(fileT)
sheet2 = book2.sheet_by_index(0)
sheet3 = book3.sheet_by_index(0)
book = xlrd.open_workbook(file_name)
sheet = book.sheet_by_index(0)
wlengths,  N_0, R, T = [], [], [], []
rows = []
#nn = min([len(R)],)
for i in range(1141):#sheet.nrows):#, row in enumerate(range(sheet.nrows)):
    if i <= 1:
        continue
    r, r2, r3 = [], [], []
    for j in [0,1]:
        r.append(sheet.cell_value(i, j))
        r2.append(sheet2.cell_value(i, j))
        r3.append(sheet3.cell_value(i, j))
    rows.append(r)
    wlengths.append(float(r[0]))
    N_0.append((r[1]))
    R.append(float(r2[1]))
    T.append(float(r3[1]))
wlengths = np.array(wlengths, dtype=np.float_) #[cm]
N_0 = np.array(N_0, dtype=np.float_)
T = np.array(T, dtype=np.float_)
R = np.array(R, dtype=np.float_)
hv = np.array(4.1356e-15 * 3e17 / wlengths, dtype=np.float_)

def functionx_p(V):
    ans = ( ( 2 * eps_p * eps_n * N_d * eps_0 * ( V_bi - V ) ) / ( N_a * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
    if ans >= W_p:
    # x_p value > W_p
        ans = W_p 
    return ans

def functionx_n(V):
    ans = ( ( 2 * eps_p * eps_n * eps_0 * N_a * ( V_bi - V ) ) / ( N_d * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
    if ans >= W_n:
    # x_n value > W_n
        ans = W_n
    return ans

def function_alpha(wlengths, E_g):
    ans = []
    for hvi in hv:
        if hvi <= E_g:
            ans.append(0.0)
        else:
            ans.append( A * ( ( hvi - E_g ) )**0.5 )
    ans = np.array(ans, dtype=np.float_)
    return ans

def itg(y):
    return integrate.simps(y, wlengths, even='avg')

def Voc(x1,y1,x2,y2):
    ans = -(y2 - (( y2 - y1 ) / ( x2 - x1 )) * x2)/(( y2 - y1 ) / ( x2 - x1 ))
    return ans

def fV_bi(E):
    ans = ( ( E - E_gn ) / 2 )  + ( X_p - X_n ) + ( k_B * Ta * np.log( (N_a * N_d) / (ni_p * ni_n) ) ) - ( 0.5 * k_B * Ta * np.log( (N_cn * N_vp) / (N_cp * N_vn) ) )
    return ans

### Photocurrent equations
# [1]

def dJ_p(V):
    x_p = functionx_p(V)
    x_n = functionx_n(V)
    a = N_0 * (1.0 - R) * T * alpha_n * L_p / ( ( ( alpha_n ** 2 * L_p ** 2 ) - 1.0 ) )    
    b = ( S_p * L_p / D_p ) + alpha_n * L_p - np.exp( - alpha_n * ( W_n - x_n) ) * ( ( S_p * L_p / D_p) * np.cosh( ( W_n - x_n ) / L_p ) + np.sinh( ( W_n -x_n ) / L_p ) )
    c = ( S_p * L_p / D_p ) * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
    d = alpha_n * L_p * np.exp( - alpha_n * (W_n - x_n) )
    ans = a*( b/c - d)
    return ans

def dJ_n(V):
    x_p = functionx_p(V)
    x_n = functionx_n(V)
    a = N_0 * (1.0 - R) * T * alpha_p * L_n * np.exp( - (alpha_n * W_n + alpha_p * x_p) ) /  ( alpha_p**2 * L_n**2 - 1.0 )
    b = ( S_n * L_n / D_n ) * ( np.cosh( ( W_p - x_p ) / L_n ) - np.exp( - alpha_p * ( W_p - x_p ) ) ) + np.sinh( ( W_p - x_p ) / L_n ) + alpha_p * L_n * np.exp( - alpha_p * ( W_p - x_p ) )        
    c = ( S_n * L_n / D_n ) * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )        
    d = alpha_p * L_n
    ans = a * ( d - b / c )
    return ans

def dJ_scr(V):
    x_p = functionx_p(V)
    x_n = functionx_n(V)
    ans = N_0 * (1.0 - R) * T * np.exp( - alpha_n * ( W_n - x_n ) ) * ( ( 1.0 - np.exp( - alpha_n * x_n ) ) + np.exp( - alpha_n * x_n ) * ( 1.0 - np.exp( - alpha_p * x_p ) ) )
    return ans 

def dJ_RCEp(V):
    x_p = functionx_p(V)
    if x_p == W_p:
        ans = N_0 * T * ( 1.0 - R ) * np.exp( - alpha_n * W_n - alpha_p * W_p - 0 * alpha_p * ( W_p - x_p ) ) * ( 1.0 - np.exp( - 0 * alpha_p * x_p ) )
    else:
        ans = N_0 * T * ( 1.0 - R ) * np.exp( - alpha_n * W_n - alpha_p * W_p - alpha_p *
              ( W_p - x_p ) ) * ( 1.0 - np.exp( - alpha_p * x_p ) )
        
    return ans

def dJ_RCEn(V):
    ans = N_0 * T * ( 1.0 - R ) * np.exp( - alpha_n * W_n - alpha_p * 2 * W_p ) * ( 1.0 - np.exp( - alpha_n ) )
    return ans 

def dJ_abs(V):
    x_p = functionx_p(V)
    a = N_0 * T * ( 1.0 - R ) * alpha_p * ( L_n / ( alpha_p ** 2 * L_n ** 2 - 1.0 ) ) * np.exp( - alpha_n * W_n - alpha_p * W_p )
    b = alpha_p * L_n
    c = S_n * L_n / D_n * ( np.cosh( ( W_p -x_p ) / L_n ) - np.exp( - alpha_p * ( W_p - x_p) )) + np.sinh( ( W_p -x_p ) / L_n ) + alpha_p * L_n * np.exp( - alpha_p * ( W_p - x_p ) )        
    d = S_n * L_n / D_n * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )        
    ans = a * ( b - c / d)
    return ans 

def dJ_win(V):
    x_n = functionx_n(V)
    a = N_0 * T * ( 1.0 - R ) * alpha_n * L_p / ( alpha_n ** 2 * L_p ** 2 - 1.0 ) * np.exp( - alpha_n * ( W_n + x_n ) - alpha_p * ( 2 * W_p ) )
    b = S_p * L_p / D_p * ( np.cosh( ( W_n - x_n ) / L_p ) - np.exp( -alpha_n * ( W_n - x_n ) ) ) + np.sinh( ( W_n - x_n ) / L_p ) + alpha_n * L_p * np.exp( alpha_n * ( W_n - x_n ) )
    c = S_p * L_p / D_p * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
    ans = a * ( alpha_n * L_p - b/c )
    return ans 

### All contributions & integration

def dJ_ph(V):
    ans =dJ_p(V) + dJ_scr(V) + dJ_n(V) + (dJ_win(V) + dJ_RCEn(V) + (dJ_RCEp(V))  + dJ_abs(V)) 
    # others functions for the secound part of the calculation [OFF]
    return ans * (1.0 / 10)

def intdJ_ph(V):
    ans = itg(dJ_ph(V))
    return ans

### Dark Photocurrent equations 

def J_0p(V):
    x_n = functionx_n(V)
    a = q * D_p * p_0 / L_p
    b = ( S_p * L_p / D_p ) * np.cosh( ( W_n - x_n ) / L_p ) + np.sinh( ( W_n - x_n ) / L_p )
    c = ( S_p * L_p / D_p ) * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
    ans = a * ( b / c )
    return ans * 1000

def J_0n(V):
    x_p = functionx_p(V)
    a = q * D_n * n_0 / L_n
    b = ( S_n * L_n / D_n ) * np.cosh( ( W_p - x_p ) / L_n ) + np.sinh( ( W_p - x_p ) / L_n )        
    c = ( S_n * L_n / D_n ) * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )        
    ans = a * ( b / c )
    return ans * 1000 

def J_00(V):
    x_n = functionx_n(V)
    x_p = functionx_p(V)
    ans = q * 1000 * ( x_n * ni_n / tau_p + x_p * ni_p / tau_n )
    return ans

def J_000(V):
    ans = q * S_i * ( ( ( ( N_cp * N_vp ) / ( N_cn * N_vn ) ) ** 0.5 ) * ni_n + ni_p )
    return ans * 1000

def Jdark(V):
    ans = ( J_0p(V) + J_0n(V) ) * ( np.exp( V / ( k_B * Ta ) ) - 1.0 ) + ( J_00(V) + J_000(V) ) * ( np.exp( V / ( 2 * k_B * Ta ) ) - 1.0 )  
    return ans

def Jcell(V):
    ans = intdJ_ph(V) - Jdark(V) 
    return ans

thickness = np.linspace(W_pmin, W_pmax, num=Steps, endpoint=True) 
gap = np.linspace(1.0, 2.0, num=Steps, endpoint=True) 
ni_n = ( N_cn * N_vn * np.exp( - E_gn / ( k_B * Ta ) ) )**0.5 
p_0 = ni_n ** 2 / N_d                          
alpha_n = function_alpha(wlengths, E_gn)       
count = 0
E_gp = np.float_(1.17)
alpha_p = function_alpha(wlengths, E_gp)
ni_p = ( N_cp * N_vp * np.exp( - E_gp / ( k_B * Ta ) ) )**0.5 
n_0 = ni_p ** 2 / N_a
V_bi = fV_bi(E_gp)
Efi_list, Voc_list, FF_list, Jsc_list, Jcell_w, Volt_w = [], [], [], [], [], []
voltage = np.linspace(0,(V_bi),num=(Vib_steps*2),endpoint=True)
V_oc, FF, Efi, J_sc = 0, 0, 0, 0
Jone, Vone = [], []
for n in range(len(voltage)):
    j = Jcell(voltage[n])
    if j <= 0:
        pass 
    else:
        Jone.append(j)
        Vone.append(voltage[n])
aa = voltage[len(Vone)-1]
bb = Jone[len(Vone)-1]
cc = voltage[len(Vone)]
dd = (Jcell(voltage[len(Vone)]))
#points for calculate
V_oc = Voc(aa, bb, cc, dd)
Vone.append(V_oc)
Jone.append(0.0)
Efi = max(np.multiply(Jone, Vone))
J_sc = max(Jone)
FF = 100 * Efi / ( V_oc * J_sc )
print('\n')
print('Results for input parameters:')
print('Efficiency: ',(Efi),'Voc: ',(V_oc),'Jsc: ',(J_sc),'FF: ',(FF))
print('\n')

data_1 = []
thickness = np.linspace(W_pmin, W_pmax, num=Steps, endpoint=True) 
gap = np.linspace(1.0, 2.0, num=Steps, endpoint=True) 
ni_n = ( N_cn * N_vn * np.exp( - E_gn / ( k_B * Ta ) ) )**0.5 
p_0 = ni_n ** 2 / N_d                          
alpha_n = function_alpha(wlengths, E_gn)       
count = 0
E_gp = np.float_(1.17)
alpha_p = function_alpha(wlengths, E_gp)
ni_p = ( N_cp * N_vp * np.exp( - E_gp / ( k_B * Ta ) ) )**0.5 
n_0 = ni_p ** 2 / N_a
V_bi = fV_bi(E_gp)
Efi_list, Voc_list, FF_list, Jsc_list, Jcell_w, Volt_w = [], [], [], [], [], []
voltage = np.linspace(0,(V_bi),num=(Vib_steps*2),endpoint=True)
print('[','*'*int(waiter),'-'*int(100-waiter),']')
for WW in thickness:
    V_oc, FF, Efi, J_sc = 0, 0, 0, 0
    W_p = WW
    jcell, v = [], []
    for n in range(len(voltage)):
        j = Jcell(voltage[n])
        if j <= 0:
            pass 
        else:
            jcell.append(j)
            v.append(voltage[n])
    aa = voltage[len(v)-1]
    bb = jcell[len(v)-1]
    cc = voltage[len(v)]
    dd = (Jcell(voltage[len(v)]))
    #points for calculate
    V_oc = Voc(aa, bb, cc, dd)
    v.append(V_oc)
    jcell.append(0.0)
    Efi = max(np.multiply(jcell, v))
    J_sc = max(jcell)
    FF = 100 * Efi / ( V_oc * J_sc )
    Efi_list.append(Efi)
    Voc_list.append(V_oc)
    Jsc_list.append(J_sc)
    FF_list.append(FF)
    waiter += wait
    print('[','*'*int(waiter),'-'*int(100-waiter),']')
data_1 = [thickness, Efi_list, Voc_list, FF_list, Jsc_list]
data_1 = np.array(data_1, dtype=np.float_)

EQE0 = dJ_ph(0) * 10/ N_0
IQE0 = EQE0 / ( 1.0 - R )
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
        
###########################################################################
## Graphics
###########################################################################

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(thickness*1.0e7, data_1[4], linewidth=0.8)
pyplot.plot(thickness*1.0e7, data_1[4], 'o')
#pyplot.plot(thickness*1.0e7, data_2[4], linewidth=0.8)
#pyplot.plot(thickness*1.0e7, data_2[4], 'o')
pyplot.xlabel('Thickness [nm]', {'fontsize':8})
pyplot.ylabel('$J_{sc}$ [mA/cm$^{2}$]', {'fontsize':8})
pyplot.title('Short-circuit current density', {'fontsize':10})
pyplot.grid(True)
#pyplot.axis([490, 3010, 34.4, 34.9])
pyplot.savefig('jSC81.pdf')
pyplot.show()

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(thickness*1.0e7, data_1[3] , linewidth=0.8)
pyplot.plot(thickness*1.0e7, data_1[3], 'o')
#pyplot.plot(thickness*1.0e7, data_2[3] , linewidth=0.8)
#pyplot.plot(thickness*1.0e7, data_2[3], 'o')
pyplot.xlabel('Thickness [nm]', {'fontsize':8})
pyplot.ylabel('FF [%]', {'fontsize':8})
pyplot.title('Fill factor', {'fontsize':10})
pyplot.grid(True)
#pyplot.axis([490, 3010, 34.4, 34.9])
pyplot.savefig('FF81.pdf')
pyplot.show()

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(thickness*1.0e7, data_1[2]*1e3 , linewidth=0.8)
pyplot.plot(thickness*1.0e7, data_1[2]*1e3, 'o')
#pyplot.plot(thickness*1.0e7, data_2[2]*1e3 , linewidth=0.8)
#pyplot.plot(thickness*1.0e7, data_2[2]*1e3, 'o')
pyplot.xlabel('Thickness [nm]', {'fontsize':8})
pyplot.ylabel('$V_{oc}$ [mV]', {'fontsize':8})
pyplot.title('Open-circuit voltage', {'fontsize':10})
pyplot.grid(True)
#pyplot.axis([490, 3010, 34.4, 34.9])
pyplot.savefig('Voc81.pdf')
pyplot.show()

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(thickness*1.0e7, data_1[1] , linewidth=0.8)
pyplot.plot(thickness*1.0e7, data_1[1], 'o')
#pyplot.plot(thickness*1.0e7, data_2[1] , linewidth=0.8)
#pyplot.plot(thickness*1.0e7, data_2[1], 'o')
pyplot.xlabel('Thickness [nm]', {'fontsize':8})
pyplot.ylabel('$\\eta$ [%]', {'fontsize':8})
pyplot.title('Efficiency', {'fontsize':10})
pyplot.grid(True)
pyplot.savefig('Effi81.pdf')
pyplot.show()

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(wlengthsQE, EQE, label='EQE', linewidth=0.8)
pyplot.plot(wlengthsQE, IQE, label='IQE', linewidth=0.8)
pyplot.xlabel('Wave length [nm]', {'fontsize':8})
pyplot.ylabel('QE', {'fontsize':8})
pyplot.title('Quantum Efficciency', {'fontsize':10})
pyplot.legend(loc='best')
pyplot.grid(True)
pyplot.savefig('QE8-300dpi.pdf')
pyplot.show()

fig, ax1, = pyplot.subplots(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
ax1.set_xlabel('Wave length [nm]', {'fontsize':8})
ax1.set_ylabel('Transmittance [%]', {'fontsize':8})
ax1.plot(wlengths, T, label='Transmittance TCO', linewidth=1.2)
ax1.tick_params(axis='y')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Reflectance [%]', {'fontsize':8})  # we already handled the x-label with ax1
ax2.plot(wlengths, R, label='Reflectance CIGS', linewidth=1.2, color='g')
ax2.tick_params(axis='y')
fig.tight_layout()# otherwise the right y-label is slightly clipped
ax1.grid(True)
fig.legend(loc='center', fontsize='small')
pyplot.savefig('RT8-300dpi.pdf')
pyplot.show()

pyplot.figure(figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
pyplot.plot(Vone, Jone, linewidth=0.8)
pyplot.xlabel('Voltage [V]', {'fontsize':8})
pyplot.ylabel('Current density [mA/cm²]', {'fontsize':8})
pyplot.title('Current Voltage Curve', {'fontsize':10})
pyplot.grid() 
pyplot.savefig('JV8-300dpi.pdf')
pyplot.show()
