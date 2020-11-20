#filtros1.py - 29日ー30日 十月　20年

import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
import matplotlib.pyplot as plt

#xn = [10, 22, 24, 42, 37, 77, 89, 22, 63, 9, 52, 31, 48, 53, 29, 14, 47, 38, 70, 0, 0, 0, 0, 0]

Fs = 64
f = 8
sample = 64
x = arange(sample)
xn = sin(2 * pi * f * x / Fs)


hn = [1/5]*5 #Filter coefficiets.

#Move the signal to the frequency domain X(M).
N = 64
vec_zeros = zeros(N - len(hn))
hn_zeros = array(hn + list(vec_zeros)) #Fill H(N) with zeros for the 64 points.
#vec_zeros = zeros(N - len(xn))
#xn_zeros =  array(xn + list(vec_zeros))#Fill X(N) with zeros with 64 points.
n_zeros = arange(N)

rh,ih,mh,ah = mi_dft(hn_zeros)

#fig = go.Figure()
#fig.add_traces(stem_plot(x= n_zeros, y= mh))
#fig.show()

#Para emitir n sin zeros y mh, 
plt.figure()
plt.stem(n_zeros, mh)
plt.xlabel('N_Zeros')
plt.ylabel('Magnitudes')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title(" 01 - Plotting N_zeros x mh")
plt.legend()


#fig = go.Figure()
#fig.add_traces(stem_plot(x= n_zeros, y= ah))
#fig.show()

plt.figure()
plt.stem(n_zeros, ah)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("02 - Plotting N_zeros x ah")
plt.legend()


rx,ix,mx,ax = mi_dft(xn) #Remove xn_zeros for xn standart.

#fig = go.Figure()
#fig.add_traces(stem_plot(x= n_zeros, y= mx))
#fig.show()

plt.figure()
plt.stem(n_zeros, mx)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("03- Plotting N_zeros x Mx")
plt.legend()

#fig = go.Figure()
#fig.add_traces(stem_plot(x= n_zeros, y= ax))
#fig.show()

plt.figure()
plt.stem(n_zeros, ax)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("04- Plotting N_zeros x Ax")
plt.legend()


e_xn = rx + ix*1j
e_hn = rh + ih*1j
xn_por_hn = e_xn * e_hn

xr,xi = mi_idft(xn_por_hn)

#fig = go.Figure()
#fig.add_traces(stem_plot(x= n_zeros, y = xr))
#fig.update_layout(xaxis=dict(range[0,len(xn)]),yaxis=dict(range=[0,100]))
#fig.show()

########
#fig = go.Figure()
#fig.add_traces(go.Scatter(x = n_zeros, y = xn))
#fig.add_traces(go.Scatter(x = n_zeros, y = xr))
#fig.update_layout(xaxis=dict(range = [0,len(xn)]),yaxis=dict(range=[0,100]))
#fig.show()

nxn = convolve(xn,hn)
#Difference between convolution Theorem and convolution
#The convolution theorem is a multiplication between two spectres,
#The difference is that the convolution works on the time domain,
#The convolution theorem works on the frequency in a multiplication.
#fig = go.Figure()
#fig.add_traces(go.Scatter(x = n_zeros, y = xn))
#fig.add_traces(go.Scatter(x = n_zeros, y = xr))
#fig.add_traces(go.Scatter(x = arange(len(nxn)), y = nxn))
#fig.update_layout(axis=dict(range=[0,len(xn)]))
#fig.show()
#xn = [10, 22, 24, 42, 37, 77, 89, 22, 63, 9, 52, 31, 48, 53, 29, 14, 47, 38, 70, 0, 0, 0, 0 ,0]

plt.figure()
plt.plot(n_zeros, xn, label='Original Signal')
plt.plot(n_zeros, xr, label='Convolution Theorem')
plt.xlabel('N_Zeros')
plt.ylabel('XR_Output')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("05 - Plotting N_zeros x Xr")
plt.legend()

nxn_len = arange(0,len(nxn))

plt.figure()
plt.plot(n_zeros, xn, label='Original Signal')
plt.plot(n_zeros, xr, label='Convolution Theorem')
plt.plot(nxn_len, nxn, label='Convolution Function')
plt.xlabel('N_Zeros')
plt.ylabel('NXN_Output')
plt.xlim(nxn_len[0],64)
plt.title("06 - Plotting N_zeros x Xnx")
plt.legend()

plt.show()