import numpy as np

from sys import argv

script, lam,d_tel = argv

lam,d_tel=np.float64(lam),np.float64(d_tel)



#script, lambda, d_tel = argv

fwhm=1.0286*206265*np.float64(lam)*1e-6/np.float64(d_tel)

print(type(lam))
print(type(d_tel))
print(type(fwhm))

print("Given a wavelength of {0:.3f} and telescope diameter of {1:.3f}, the FWHM is {2:.3f}".format(lam,d_tel,fwhm))
