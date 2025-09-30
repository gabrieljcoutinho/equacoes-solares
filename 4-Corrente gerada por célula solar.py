import numpy as np
import matplotlib.pyplot as plt

V = np.linspace(0, 0.6, 100)
Isc = 5
I0 = 1e-10
q = 1.6e-19
k = 1.38e-23
T = 300

I = Isc - I0 * (np.exp((q * V) / (k * T)) - 1)

plt.plot(V, I, label='Corrente (I)', color='red')
plt.xlabel('Tensão (V) [V]')
plt.ylabel('Corrente (I) [A]')
plt.title('Corrente vs Tensão em Célula Fotovoltaica')
plt.grid(True)
plt.legend()
plt.show()
