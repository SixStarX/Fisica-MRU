import matplotlib.pyplot as plt

tempos = []
posicoes = []
velocidades = []

with open('dados.txt', 'r') as f:
    for linha in f:
        if linha.strip().startswith('Tempo'):
            continue
        try:
            t, x, v = map(float, linha.strip().split())
            tempos.append(t)
            posicoes.append(x)
            velocidades.append(v)
        except:
            continue

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(tempos, posicoes, 'b-', label='Posição (m)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição vs. Tempo')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(tempos, velocidades, 'r-', label='Velocidade (m/s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade vs. Tempo')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()