import matplotlib.pyplot as plt

P_DC = [500, 600, 700, 800, 900]
P_AC = [450, 540, 630, 720, 810]
eta_inv = [pac / pdc for pac, pdc in zip(P_AC, P_DC)]

plt.plot(P_DC, eta_inv, label='Eficiência do Inversor (η)', color='purple')
plt.xlabel('Potência DC (P_DC) [W]')
plt.ylabel('Eficiência (η)')
plt.title('Eficiência do Inversor')
plt.grid(True)
plt.legend()
plt.show()
