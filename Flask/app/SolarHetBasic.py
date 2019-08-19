import numpy as np
import xlrd
from scipy import integrate
from app import app, main

#Constants Boltzmann constant, electron charge, Temperature, electrostatic field?, 

k_B = 8.617332e-5 #[eV/K]
q = 1.6e-19 #[C] 4.803e−10[statC]
A = 1e5
h = 4.135e-15 #[eV s]6.626e34[J s]
c = 3e10 #[cm/s]
eps_0 = 8.8542e-14

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

def function_alpha(hv, E_g):
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
    b = ( S_p * L_p / D_p ) + alpha_n * L_p - np.exp( - alpha_n * ( W_n - x_n) ) * ( ( S_p * L_p / D_p) * np.cosh( ( W_n - x_n ) / L_p ) + np.sinh( ( W_n - x_n ) / L_p ) )
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
    ans = dJ_scr(V) + dJ_p(V) + dJ_n(V) + (dJ_win(V) + dJ_RCEn(V) + (dJ_RCEp(V))  + dJ_abs(V)) 
    # others functions for the secound part of the calculation [OFF]
    return ans * (1.0 / 10)
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
    ans = itg(dJ_ph(V)) - Jdark(V) 
    return ans

#Read parameters file
Ta = 300 #K
def valvalues(Ta, E_gn, E_gp, D_n, D_p, eps_p, eps_n, N_a, N_d, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, W_pmin, W_pmax, X_n, X_p, S_i, Steps, Vib_steps, L_n, L_p, wlengthsneq, N_0neq, Rneq, Tneq, nn):
    alpha_n, alpha_p, wlengths, N_0, R, T, hv = np.empty((7,0), dtype=np.float_)
    nn = nn
    globals()['E_gn'] = E_gn
    globals()['E_gp'] = E_gp
    globals()['D_n'] = D_n
    globals()['D_p'] = D_p
    globals()['eps_p'] = eps_p
    globals()['eps_n'] = eps_n
    globals()['N_a'] = N_a
    globals()['N_d'] = N_d
    globals()['N_cp'] = N_cp
    globals()['N_vp'] = N_vp
    globals()['N_cn'] = N_cn
    globals()['N_vn'] = N_vn
    globals()['S_n'] = S_n
    globals()['S_p'] = S_p
    globals()['W_n'] = W_n
    globals()['W_p'] = W_p
    globals()['W_pmin'] = W_pmin
    globals()['W_pmax'] = W_pmax
    globals()['X_n'] = X_n
    globals()['X_p'] = X_p
    globals()['S_i'] = S_i
    globals()['Steps'] = Steps
    globals()['Vib_steps'] = Vib_steps
    globals()['L_n'] = L_n
    globals()['L_p'] = L_p
    for i in range(nn):
        wlengths = np.r_[wlengths, wlengthsneq[i]]
        N_0 = np.r_[N_0, N_0neq[i]]
        R = np.r_[R, Rneq[i]]
        T = np.r_[T, Tneq[i]]
    globals()
    globals()['wlengths'] = np.array(wlengths, dtype=np.float_)
    globals()['N_0'] = np.array(N_0, dtype=np.float_)
    globals()['T'] = np.array(T, dtype=np.float_)
    globals()['R'] = np.array(R, dtype=np.float_)
    hv = np.r_[hv, 4.1356e-15 * 3e17 / wlengths]
    globals()['hv'] = np.array(hv, dtype=np.float_)
    globals()['ni_n'] = ( N_cn * N_vn * np.exp( - E_gn / ( k_B * Ta ) ) )**0.5 
    globals()['ni_p'] = ( N_cp * N_vp * np.exp( - E_gp / ( k_B * Ta ) ) )**0.5 
    globals()['p_0'] = ni_n ** 2 / N_d    
    globals()['n_0'] = ni_p ** 2 / N_a 
    globals()['alpha_p'] = np.r_[alpha_p, function_alpha(hv, E_gp)]
    globals()['alpha_n'] = np.r_[alpha_n, function_alpha(hv, E_gn)]
    globals()['V_bi'] =  fV_bi(E_gp)
    globals()['tau_p'] = L_p ** 2 / D_p
    globals()['tau_n'] =  L_n ** 2 / D_n
    return R, T, wlengths, hv, N_0, V_bi, alpha_n, alpha_p
    #global Ta, E_gn, E_gp, D_n, D_p, eps_p, eps_n, N_a, N_d, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, W_pmin, W_pmax, X_n, X_p, S_i, Steps, Vib_steps, L_n, L_p

def rolling(W_p):
        globals()['W_p'] = W_p
        return W_p

#read the data of ASTM G173-03 Reference Spectra Derived from SMARTS v. 2.9.2

