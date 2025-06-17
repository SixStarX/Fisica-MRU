import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import matplotlib.pyplot as plt
from pathlib import Path

# ---------- funções utilitárias ----------
def alternar_tipo(event=None):
    """Habilita ou desabilita o campo 'a' conforme o tipo."""
    if tipo_var.get() == "MRU":
        entry_a.config(state="disabled")
        entry_a.delete(0, tk.END)
        entry_a.insert(0, "0.0")
    else:
        entry_a.config(state="normal")

def executar_simulacao():
    try:
        # Coleta dados da interface
        tipo = tipo_var.get()
        x0 = float(entry_x0.get())
        v0 = float(entry_v0.get())
        a  = float(entry_a.get()) if tipo == "MRUV" else 0.0
        tf = float(entry_tf.get())
        dt = float(entry_dt.get())

        # Gera entrada.txt
        with open("entrada.txt", "w") as f:
            f.write(f"{tipo}\n{x0}\n{v0}\n{a}\n{tf}\n{dt}\n")

        # Verifica se o executável existe
        exe = Path("mru_mruv.exe")
        if not exe.exists():
            raise FileNotFoundError("mru_mruv_calc.exe não encontrado. Compile o Fortran primeiro.")

        # Executa o programa Fortran
        run = subprocess.run([str(exe)], capture_output=True, text=True)
        if run.returncode != 0:
            raise RuntimeError(f"Erro no Fortran:\n{run.stderr}")

        # Lê dados.txt
        t_vals, x_vals, v_vals = [], [], []
        with open("dados.txt") as f:
            next(f)  # pula cabeçalho
            for linha in f:
                t, x, v = map(float, linha.split())
                t_vals.append(t)
                x_vals.append(x)
                v_vals.append(v)

        # Gera gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(t_vals, x_vals, label="Posição (m)")
        plt.plot(t_vals, v_vals, label="Velocidade (m/s)")
        plt.xlabel("Tempo (s)")
        plt.title(f"Simulação {tipo}")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("grafico.png", dpi=300)
        plt.show()

        messagebox.showinfo("Sucesso", "✅ Simulação concluída.\nArquivos 'dados.txt' e 'grafico.png' atualizados.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# ---------- construção da GUI ----------
root = tk.Tk()
root.title("Simulador MRU / MRUV")

tipo_var = tk.StringVar(value="MRU")

ttk.Label(root, text="Tipo de movimento:").grid(row=0, column=0, sticky="e")
combo_tipo = ttk.Combobox(root, textvariable=tipo_var, values=["MRU", "MRUV"], width=6, state="readonly")
combo_tipo.grid(row=0, column=1)
combo_tipo.bind("<<ComboboxSelected>>", alternar_tipo)

ttk.Label(root, text="x₀ (m):").grid(row=1, column=0, sticky="e")
entry_x0 = ttk.Entry(root); entry_x0.insert(0, "0.0"); entry_x0.grid(row=1, column=1)

ttk.Label(root, text="v₀ (m/s):").grid(row=2, column=0, sticky="e")
entry_v0 = ttk.Entry(root); entry_v0.insert(0, "5.0"); entry_v0.grid(row=2, column=1)

ttk.Label(root, text="a (m/s²):").grid(row=3, column=0, sticky="e")
entry_a = ttk.Entry(root); entry_a.insert(0, "0.0"); entry_a.grid(row=3, column=1)
entry_a.config(state="disabled")  # começa desabilitado (MRU)

ttk.Label(root, text="t_final (s):").grid(row=4, column=0, sticky="e")
entry_tf = ttk.Entry(root); entry_tf.insert(0, "2.0"); entry_tf.grid(row=4, column=1)

ttk.Label(root, text="Δt (s):").grid(row=5, column=0, sticky="e")
entry_dt = ttk.Entry(root); entry_dt.insert(0, "0.1"); entry_dt.grid(row=5, column=1)

ttk.Button(root, text="Executar Simulação", command=executar_simulacao)\
    .grid(row=6, column=0, columnspan=2, pady=8)

root.mainloop()