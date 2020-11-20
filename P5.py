import plotly.graph_objects as go 
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
from filter_lib_711 import fpb_ideal

N = 256
M = 15

w = array([1]*M)
z = [0]*(N-M)
wz = array(list(w)+z)
r,i,m1,a = mi_dft(wz)

w=bartlett(M)
z = [0]*(N-M)
wz = array(list(w)+z)
r,i,m2,a = mi_dft(wz)

w=hanning(M)
z=[0]*(N-M)
wz = array(list(w)+z)
r,i,m3,a = mi_dft(wz)

w=hamming(M)
z=[0]*(N-M)
wz = array(list(w)+z)
r,i,m4,a = mi_dft(wz)

w=blackman(M)
z=[0]*(N-M)
wz = array(list(w)+z)
r,i,m5,a = mi_dft(wz)

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(N/2), y=m1, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m2, name='Bartlett'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m3, name='Hanning'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m4, name='Hamming'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m5, name='Blackman'))
fig.update_xaxes(title_text='Frequency')
fig.update_yaxes(title_text='|x(m)|')
fig.update_layout(title='Linear-scale Window Magnitude responses.', xaxis= dict(range=[0,N/2]))
fig.write_image("P5/|x(m)|.eps")

m1n=20*log10(m1/m1[0])
m2n=20*log10(m2/m2[0])
m3n=20*log10(m3/m3[0])
m4n=20*log10(m4/m4[0])
m5n=20*log10(m5/m5[0])

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(N/2), y=m1n, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m2n, name='Barlett'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m3n, name='Hanning'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m4n, name='Hamming'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m5n, name='Blackman'))
fig.update_xaxes(title_text='Frequency')
fig.update_yaxes(title_text='Db')
fig.update_layout(title='Logarithmic-Scale Window Magnitude responses.', xaxis= dict(range=[0,N/2]))
fig.write_image("P5/db.eps")
