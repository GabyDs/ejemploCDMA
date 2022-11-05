# Ejemplo CDMA

import numpy as np
import numpy.matlib as mat
import matplotlib.pyplot as plt

n_data = 3 # nro de bits de datos
n_PN = 30 # nro de bits secuencia pseudo aleatoria 
n = 2 # cantidad de usuarios simultaneos

# generacion de datos

# generacion de datos y las secuencias pseudo aleatorias para la
# codificacion

data = np.random.randint(2, size=(n_data, n))
PN = np.random.randint(2, size=(n_PN, n))

#print(f"Data: \n{data}")
#print(f"PN: \n{PN}")

#for i in range(n):
#    print(f"Data usuario {i} :\n{np.transpose(data[:,i])}")

#for i in range(n):
#    print(f"Secuencia pseudoaleatoria usuario {i} :\n{np.transpose(PN[:,i])}")

# Codificacion
#
# codificacion

data = 2*data - 1

signal = np.zeros((90,2), dtype=int)

for i in range(n):
    signal[:,i] = np.kron(data[:,i], PN[:,i])

#print(f"Signal: \n{signal}")

# concatena la secuencia PN n_data veces

PN_long = mat.repmat(PN, n_data, 1) 

#print(f"Secuencia de valores PN: \n{PN_long}")

PN_mat_plot = mat.repmat(PN_long,100,1)
data_plot = mat.repmat(data,100,1) 
signal_plot = mat.repmat(signal,100,1)

L = len(PN_mat_plot)

#print(f"Tamaño de PN_mat_plot: {L}")

x = np.arange(0,9,0.001)
y = PN_mat_plot[:,0]
plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')

plt.show()