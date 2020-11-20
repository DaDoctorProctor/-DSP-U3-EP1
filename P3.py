

import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
from filter_lib_711 import fpb_ideal
import matplotlib.pyplot as plt

#Declaring W as 1/6 since, there are 6 coeffiecients to be calculated.
w = 1/6
N = 512

for M in range(5,65,10):
    coef = fpb_ideal(w,M)

    fig = go.Figure()
    fig.add_traces(stem_plot(x = arange(M), y = coef))
    fig.update_layout(title = 'Filter ' + str(M) + ' Taps', xaxis = dict(range=[0,M]))
    fig.write_image("P3/Filt"+str(M)+".eps")

    vec_zeros = [0]*(N - M)
    coef_zeros = array(list(coef) + vec_zeros)
    r,i,m,a = mi_dft(coef_zeros)

    fig = go.Figure()
    fig.add_traces(stem_plot(x = arange(N/2), y = m, line=dict(color='firebrick')))
    fig.update_layout(title = 'Filter response ' + str(M) + ' Taps', xaxis = dict(range=[0,M]))
    fig.write_image("P3/Resp"+str(M)+".eps")

    
                      
   
                    
