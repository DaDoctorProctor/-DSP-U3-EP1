#filtros1.py - 29日ー30日 十月　20年

import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *

xn = [10, 22, 24, 42, 37, 77, 89, 22, 63, 9, 52, 31, 48, 53, 29, 14, 47, 38, 70, 0, 0, 0, 0, 0]

fs = 100
ts = 1/fs
n = arange(0,64)

hn = [1/5]*5 #Filter coefficiets.

#Move the signal to the frequency domain X(M).
N = 64
vec_zeros = zeros(N - len(hn))
hn_zeros = array(hn + list(vec_zeros)) #Fill H(N) with zeros for the 64 points.
vec_zeros = zeros(N - len(xn))
xn_zeros =  array(xn + list(vec_zeros))#Fill X(N) with zeros with 64 points.
n_zeros = arange(N)

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y= xn_zeros))
fig.show()

rh,ih,mh,ah = mi_dft(hn_zeros)

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y= mh))
fig.show()

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y= ah))
fig.show()

rx,ix,mx,ax = mi_dft(xn_zeros)

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y= mx))
fig.show()

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y= ax))
fig.show()

e_xn = rx + ix*1j
e_hn = rh + ih*1j
xn_por_hn = e_xn * e_hn

xr,xi = mi_idft(xn_por_hn)

fig = go.Figure()
fig.add_traces(stem_plot(x= n_zeros, y = xr))
fig.update_layout(xaxis=dict(range[0,len(xn)]),yaxis=dict(range=[0,100]))
fig.show()

########
fig = go.Figure()
fig.add_traces(go.Scatter(x = n_zeros, y = xn))
fig.add_traces(go.Scatter(x = n_zeros, y = xr))
fig.update_layout(xaxis=dict(range = [0,len(xn)]),yaxis=dict(range=[0,100]))
fig.show()

nxn = convolve(xn,hn)
#Difference between convolution Theorem and convolution
#The convolution theorem is a multiplication between two spectres,
#The difference is that the convolution works on the time domain,
#The convolution theorem works on the frequency in a multiplication.
fig = go.Figure()
fig.add_traces(go.Scatter(x = n_zeros, y = xn))
fig.add_traces(go.Scatter(x = n_zeros, y = xr))
fig.add_traces(go.Scatter(x = arange(len(nxn)), y = nxn))
fig.update_layout(axis=dict(range=[0,len(xn)]))
fig.show()
#xn = [10, 22, 24, 42, 37, 77, 89, 22, 63, 9, 52, 31, 48, 53, 29, 14, 47, 38, 70, 0, 0, 0, 0 ,0]

