import plotly.graph_objects as go 
from dft_lib_correct import *
from numpy import *
import scipy.signal.windows as ssw

N = 512
M = 32

w1 = array([1]*M)
z = [0]*(N-M)
wz = array(list(w1)+z)
r,i,m1,a = mi_dft(wz)

w2=kaiser(M, 6)
z=[0]*(N-M)
wz = array(list(w2)+z)
r,i,m2,a = mi_dft(wz)

w3=kaiser(M, 7)
z=[0]*(N-M)
wz = array(list(w3)+z)
r,i,m3,a = mi_dft(wz)

w4=kaiser(M, 8)
z=[0]*(N-M)
wz = array(list(w4)+z)
r,i,m4,a = mi_dft(wz)

w5=kaiser(M, 9)
z=[0]*(N-M)
wz = array(list(w5)+z)
r,i,m5,a = mi_dft(wz)

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(M), y=m1, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(M), y=m2, name='Kaiser β = 6'))
fig.add_trace(go.Scatter(x=arange(M), y=m3, name='Kaiser β = 7'))
fig.add_trace(go.Scatter(x=arange(M), y=m4, name='Kaiser β = 8'))
fig.add_trace(go.Scatter(x=arange(M), y=m5, name='Kaiser β = 9'))
fig.update_xaxes(title_text='n')
fig.update_yaxes(title_text='W(m)')
fig.update_layout(title='Window Sample', xaxis= dict(range=[0,M-1]))
fig.write_image("P7/W(m).eps")

m1n=20*log10(m1/m1[0])
m2n=20*log10(m2/m2[0])
m3n=20*log10(m3/m3[0])
m4n=20*log10(m4/m4[0])
m5n=20*log10(m5/m5[0])

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(N/2), y=m1n, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m2n, name='Kaiser β = 6'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m3n, name='Kaiser β = 7'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m4n, name='Kaiser β = 8'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m5n, name='Kaiser β = 9'))
fig.update_xaxes(title_text='Frequency')
fig.update_yaxes(title_text='Db')
fig.update_layout(title='Window Coefficients (Normalized)', xaxis= dict(range=[0,N/4]), yaxis= dict(range=[-70,0]))
fig.write_image("P7/Db.eps")
