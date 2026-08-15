import numpy as np

def run(filename='nearestAstars.txt'):


 outfile=open(filename,'w')

 name=['Sirius','Altair']
 distance_ly=[8.6,16.7]


 outfile.write('The nearest A star is {0:s} at a distance of {1:.3f} parsecs'.format(name[0],distance_ly[0]/3.26))
 outfile.write("\n")
 outfile.write('The second nearest A star is {0:s} at a distance of {1:.4f} parsecs'.format(name[1],distance_ly[1]/3.26))
 outfile.close()

 
