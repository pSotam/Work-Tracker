import tkinter as tk

janela = tk.Tk()
janela.title("Work Tracker")

janela.geometry("500x550")
janela.resizable(False, False)

janela.configure(bg="#1D1C35")

# TEXTOS
label = tk.Label(janela, text="Olá, seja bem vindo(a) ao Work Tracker!",
                 font=('Arial',14,'bold'),
                 bg="#535280",
                 fg="#000000")
label.pack(pady=7)

label = tk.Label(janela, text="Registre seu progresso no dia a dia!",
                 font=('Arial',11,'bold'),
                 bg="#535280",
                 fg="#000000")
label.pack(pady=5)

# CAIXA DE TEXTO 1 // NOME DA TAREFA
frame_input = tk.Frame(janela,bg="#1D1C35")
frame_input.pack(pady=10)

label_nome = tk.Label(frame_input, 
                      text="Nome da tarefa:",
                      font=("Arial",12,"bold"),
                      bg="#535280",
                      fg="#070714")
label_nome.pack(side="left", padx=10)

nome_tarefa = tk.Entry(frame_input,bg="#ADABDB")
nome_tarefa.pack(side="left")

# CAIXA DE TEXTO 2 // DESCRIÇÃO
frame_descricao = tk.Frame(janela, bg="#1D1C35")
frame_descricao.pack(pady=10)

label_desc = tk.Label(frame_descricao,
                              text="Descrição (Opcional):",
                              font=("Arial",12,"bold"),
                              bg="#535280",
                              fg="#070714")
label_desc.pack(anchor="w", padx=5)

texto_personalizado = tk.Text(frame_descricao,
                              bg="#ADABDB",
                              font=('Arial',12),
                              height=5,
                              width=30)
texto_personalizado.pack(side="left", padx=5)

# CAIXA DE TEXTO 3 // SKU
frame_sku = tk.Frame(janela, bg="#1D1C35")
frame_sku.pack(pady=10)

label_sku = tk.Label(frame_sku, 
                      text="SKU:",
                      font=("Arial",12,"bold"),
                      bg="#535280",
                      fg="#070714")
label_sku.pack(side="left", padx=5)

codigo_sku = tk.Entry(frame_sku,bg="#ADABDB")
codigo_sku.pack(side="left")

# CAIXA DE TEXTO 4 // MLB
frame_mlb = tk.Frame(janela, bg="#1D1C35")
frame_mlb.pack(pady=10)

label_mlb = tk.Label(frame_mlb, 
                      text="MLB / CÓDIGO MELI:",
                      font=("Arial",12,"bold"),
                      bg="#535280",
                      fg="#070714")
label_mlb.pack(side="left", padx=5)

codigo_mlb = tk.Entry(frame_mlb,bg="#ADABDB")
codigo_mlb.pack(side="left")

# BOTÕES
dados = []

def botao_final():
    tarefa = nome_tarefa.get().strip()
    if(tarefa == ''):
        mensagem.config(text="Nome da tarefa é obrigatório!")
        return
    else:
        mensagem.config(text="")

    descricao = texto_personalizado.get("1.0", "end-1c").strip()
    if descricao == "":
        descricao = "N/A"

    sku = codigo_sku.get().strip()
    if sku == "":
        sku = "N/A"

    mlb = codigo_mlb.get().strip()
    if mlb == "":
        mlb = "N/A"

    print(tarefa)
    print(descricao)
    print(sku)
    print(mlb)

    dados_func = {"nome":tarefa,
                  "desc":descricao,
                  "sku":sku,
                  "mlb":mlb}
    
    dados.append(dados_func)
    print(dados)

    nome_tarefa.delete(0, tk.END)
    texto_personalizado.delete("1.0", tk.END)
    codigo_sku.delete(0, tk.END)
    codigo_mlb.delete(0, tk.END)

    mensagem.config(text="Tarefa salva com sucesso!", fg="green")

    # BOTÃO DE ENVIAR
botao = tk.Button(janela, 
                  text='Enviar', 
                  command=botao_final, 
                  bg="#908FB1", 
                  fg="black", 
                  activebackground="#636283", 
                  font=('Arial',12,"bold"),
                  width=12)
botao.pack(pady=20)

    # BOTÃO DE SAIR
botao = tk.Button(janela,
                  text="Fechar",
                  command=janela.quit,
                  bg="#ff4d4d",
                  fg="black",
                  activebackground="#a4161a",
                  font=('Arial',12,"bold"),
                  width=12)
botao.pack(pady=10)

mensagem = tk.Label(janela,
                    text="",
                    font=("Arial",10,"bold"),
                    bg="#1D1C35",
                    fg="#ff4d4d")
mensagem.pack()

janela.mainloop()