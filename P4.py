
import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
from filter_lib_711 import fpb_ideal

#Declaring W as 1/6 since, there are 6 coeffiecients to be calculated.
w = 1/6 
N = 512

for M in range(5,65,10):
    coef = fpb_ideal(w,M)

    vec_zeros = [0]*(N - M)
    coef_zeros = array(list(coef) + vec_zeros)
    r,i,m,a = mi_dft(coef_zeros)

    window = blackman(M)
    coef_w = coef*window
    coef_zeros_w = array(list(coef_w) + vec_zeros)
    r,i,m,a = mi_dft(coef_zeros_w)
    fig = go.Figure()
    fig.add_traces(go.Scatter(x=arange(N/2),y=m,line=dict(color='fuchsia')))
    fig.update_layout(title='filter + window response ' + str(M) + ' taps')
    fig.write_image("P4/Resp"+str(M)+".eps")


    
                      
    
                    
