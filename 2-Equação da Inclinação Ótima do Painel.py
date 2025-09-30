import matplotlib.pyplot as plt

phi = [0, 10, 20, 30, 40, 50]
delta = [23.45]*len(phi)
beta = [p - d for p, d in zip(phi, delta)]

plt.plot(phi, beta, label='Inclinação ótima (β)', color='green')
plt.xlabel('Latitude (φ) [graus]')
plt.ylabel('Inclinação Ótima (β) [graus]')
plt.title('Inclinação do Painel vs Latitude')
plt.grid(True)
plt.legend()
plt.show()
