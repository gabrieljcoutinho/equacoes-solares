import matplotlib.pyplot as plt

eta_mod = [0.15, 0.16, 0.17, 0.18, 0.19]
eta_inv = 0.95
eta_outros = 0.90
eta_sist = [em * eta_inv * eta_outros for em in eta_mod]

plt.plot(eta_mod, eta_sist, label='Eficiência Total (η_sist)', color='brown')
plt.xlabel('Eficiência do Módulo (η_mod)')
plt.ylabel('Eficiência Total (η_sist)')
plt.title('Eficiência do Sistema Fotovoltaico')
plt.grid(True)
plt.legend()
plt.show()
