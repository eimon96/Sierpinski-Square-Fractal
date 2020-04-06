get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pylab as plt

def gasket(pa, pb, pc, level,color):
    if level == 0: 
        plt.fill([pa[0], pb[0], pc[0]], [pa[1], pb[1], pc[1]], color) 
        plt.hold(True)
    else:
        gasket(pa, (pa + pb) / 2., (pa + pc) / 2., level - 1,color) 
        gasket(pb, (pb + pa) / 2., (pb + pc) / 2., level - 1,color) 
        gasket(pc, (pc + pa) / 2., (pc + pb) / 2., level - 1,color)
        
a = np.array([-1,1])
b = np.array([1,1])
c = np.array([1,-1])
d = np.array([-1,-1])
o = np.array([0,0])
level = 4
gasket(o,a,b, level,'r')
gasket(o,b,c, level,'r')
gasket(o,c,d, level,'r')
gasket(o,d,a, level,'r')
plt.hold(False)
plt.title("Lv.4")
plt.axis('equal')
