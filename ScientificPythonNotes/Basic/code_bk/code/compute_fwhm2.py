import numpy as np

def run(lambda=1.6,d_tel=8.2):


 fwhm=1.0286*206265*lambda*1e-6/d_tel

 print("Given a wavelength of {0:.3f} and telescope diameter of {1:.3f}, the FWHM is {2:.3f}".format(lambda,d_tel,fwhm))
