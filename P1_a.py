#Based on filtros1.py - 29日ー30日 十月　20年

import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
import matplotlib.pyplot as plt

#Start by declaring the 2Hz Sine wave parameters.
Fs = 64
f = 2
sample = 64
x = arange(sample)
#Using a 2Hz Sine Wave signal.
xn = sin(2 * pi * f * x / Fs)

#Since we are using 1/5 because of the 5 number averaging filter, hence it will be declared as...
hn = [1/5]*5 

#Move the signal to the frequency domain X(M).
N = 64
vec_zeros = zeros(N - len(hn))
hn_zeros = array(hn + list(vec_zeros)) #Fill H(N) with zeros for the 64 points.
n_zeros = arange(N)

rh,ih,mh,ah = mi_dft(hn_zeros)

#Using n_zeros and the h(N) signal after applying DFT to it.
plt.figure()
plt.stem(n_zeros, mh)
plt.xlabel('N_Zeros')
plt.ylabel('Magnitudes')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title(" 01 - Plotting N_zeros x mh")
plt.legend()

plt.figure()
plt.stem(n_zeros, ah)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("02 - Plotting N_zeros x ah")
plt.legend()

#Remove xn_zeros, since there is no need for zeros in our signal.
rx,ix,mx,ax = mi_dft(xn) 

plt.figure()
plt.stem(n_zeros, mx)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("03- Plotting N_zeros x Mx")
plt.legend()

plt.figure()
plt.stem(n_zeros, ax)
plt.xlabel('N_Zeros')
plt.ylabel('Angles')
plt.xlim(n_zeros[0],n_zeros[-1])
plt.title("04- Plotting N_zeros x Ax")
plt.legend()

#Use the convolution Theorem to find the answer.
e_xn = rx + ix*1j
e_hn = rh + ih*1j
xn_por_hn = e_xn * e_hn

#Applying the IDFT to reverse to the time domain.
xr,xi = mi_idft(xn_por_hn)

#Using only the convolution function
nxn = convolve(xn,hn)
#Difference between convolution Theorem and convolution
#The convolution theorem is a multiplication between two spectres,
#The difference is that the convolution works on the time domain,
#The convolution theorem works on the frequency in a multiplication.

#Plotting the results.
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