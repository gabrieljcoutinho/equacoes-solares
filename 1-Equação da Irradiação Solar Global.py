import matplotlib.pyplot as plt

G_b = [100, 200, 300, 400, 500]
G_d = [50, 60, 70, 80, 90]
G = [b + d for b, d in zip(G_b, G_d)]

plt.plot(G_b, G, label='Irradiação Global (G)', color='orange')
plt.xlabel('Irradiação Direta (G_b) [W/m²]')
plt.ylabel('Irradiação Global (G) [W/m²]')
plt.title('Gráfico da Irradiação Solar Global')
plt.grid(True)
plt.legend()
plt.show()
