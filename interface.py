import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import matplotlib.pyplot as plt

def executar_simulacao():
    try:
        # Coleta dos dados
        x0 = float(entry_x0.get())
        v0 = float(entry_v0.get())
        a = float(entry_a.get())
        tf = float(entry_tf.get())
        dt = float(entry_dt.get())

        # Gera entrada.txt para Fortran
        with open("entrada.txt", "w") as f:
            f.write("MRUV\n")
            f.write(f"{x0}\n{v0}\n{a}\n{tf}\n{dt}\n")

        # Executa o programa Fortran compilado
        resultado = subprocess.run(["./mru_mruv.exe"], capture_output=True, text=True)
        if resultado.returncode != 0:
            raise Exception(f"Erro no Fortran:\n{resultado.stderr}")

        # Lê dados.txt
        t_vals, x_vals, v_vals = [], [], []
        with open("dados.txt", "r") as f:
            next(f)  # pula cabeçalho
            for linha in f:
                partes = linha.split()
                t_vals.append(float(partes[0]))
                x_vals.append(float(partes[1]))
                v_vals.append(float(partes[2]))

        # Plota gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(t_vals, x_vals, label="Posição (x)", marker='o')
        plt.plot(t_vals, v_vals, label="Velocidade (v)", marker='x')
        plt.xlabel("Tempo (s)")
        plt.ylabel("Valor")
        plt.title("MRUV: Posição e Velocidade")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("grafico.png")
        plt.show()

        messagebox.showinfo("Sucesso", "✅ Simulação concluída com sucesso!\nGráfico salvo como 'grafico.png'.")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# GUI
root = tk.Tk()
root.title("Simulador de MRUV com Fortran")

ttk.Label(root, text="x0 (posição inicial):").grid(row=0, column=0, sticky="e")
entry_x0 = ttk.Entry(root)
entry_x0.insert(0, "0.0")
entry_x0.grid(row=0, column=1)

ttk.Label(root, text="v0 (velocidade inicial):").grid(row=1, column=0, sticky="e")
entry_v0 = ttk.Entry(root)
entry_v0.insert(0, "5.0")
entry_v0.grid(row=1, column=1)

ttk.Label(root, text="a (aceleração):").grid(row=2, column=0, sticky="e")
entry_a = ttk.Entry(root)
entry_a.insert(0, "-9.8")
entry_a.grid(row=2, column=1)

ttk.Label(root, text="tf (tempo final):").grid(row=3, column=0, sticky="e")
entry_tf = ttk.Entry(root)
entry_tf.insert(0, "2.0")
entry_tf.grid(row=3, column=1)

ttk.Label(root, text="dt (passo de tempo):").grid(row=4, column=0, sticky="e")
entry_dt = ttk.Entry(root)
entry_dt.insert(0, "0.1")
entry_dt.grid(row=4, column=1)

ttk.Button(root, text="Executar Simulação", command=executar_simulacao).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()