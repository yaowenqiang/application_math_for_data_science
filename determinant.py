from numpy.linalg import det
from numpy import array

i_het = array([3,0])
j_het = array([0,2])

basis = array([i_het, j_het]).transpose()

determinant = det(basis)

print(determinant)