import matplotlib.pyplot as plt

G = [200, 400, 600, 800, 1000]
A = 1.6  # área fixa (m²)
eta = 0.18  # eficiência fixa (18%)
P = [g * A * eta for g in G]

plt.plot(G, P, label='Potência Gerada (P)', color='blue')
plt.xlabel('Irradiação Solar (G) [W/m²]')
plt.ylabel('Potência (P) [W]')
plt.title('Potência Gerada pelo Painel')
plt.grid(True)
plt.legend()
plt.show()
