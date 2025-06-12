# gerar_entrada.py

def gerar_entrada(tipo="MRUV", x0=0.0, v0=5.0, a=-9.8, tf=2.0, dt=0.1):
    with open("entrada.txt", "w") as f:
        f.write(f"{tipo}\n")
        f.write(f"{x0}\n")
        f.write(f"{v0}\n")
        if tipo.strip().upper() == "MRUV":
            f.write(f"{a}\n")
        else:
            f.write("0.0\n")  # Aceleração 0 para MRU
        f.write(f"{tf}\n")
        f.write(f"{dt}\n")
    print("✅ entrada.txt gerado com sucesso.")

# Exemplo: alterar os valores aqui se desejar
gerar_entrada(tipo="MRUV", x0=0.0, v0=5.0, a=-9.8, tf=2.0, dt=0.1)
