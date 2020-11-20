#filter_lib_711.py - 09日十一月20年
def my_sinc(X):
    from numpy import sin,array
    S = []
    for x in X:
        if x == 0:
            s = 1
        else:
            s = sin(x)/x
        S.append(s)
    return array(S)

def fpb_ideal(w,M):
    from numpy import arange, pi
    pm = (M-1)/2
    n = arange(M)
    m = n - pm
    rpb = my_sinc(w*m)*(w/pi) #2f * sinc(2*pi*f*m)
    return rpb
