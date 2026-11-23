import tkinter as tk
from tkinter import ttk, messagebox
import database

def listar_usuarios():
    for item in tabela.get_children():
        tabela.delete(item)
    usuarios = database.listar_usuarios()
    for usuario in usuarios:
        tabela.insert("", tk.END, values=usuario)

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)
    entrada_tipo.delete(0, tk.END)
    entrada_status.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_data_cadastro.delete(0, tk.END)
    entrada_ultimo_acesso.delete(0, tk.END)
    tabela.selection_remove(tabela.selection())

def cadastrar_usuario():
    nome = entrada_nome.get().strip().replace("'", "''")
    email = entrada_email.get().strip().replace("'", "''")
    senha = entrada_senha.get().strip().replace("'", "''")
    tipo = entrada_tipo.get().strip().replace("'", "''")
    status = entrada_status.get().strip().replace("'", "''")
    telefone = entrada_telefone.get().strip().replace("'", "''")
    data_cadastro = entrada_data_cadastro.get().strip().replace("'", "''")
    ultimo_acesso = entrada_ultimo_acesso.get().strip().replace("'", "''")

    if not nome or not email or not senha or not tipo or not status or not telefone or not data_cadastro or not ultimo_acesso:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        database.cadastrar_usuario(nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso)
        limpar_campos()
        listar_usuarios()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

def selecionar_usuario(event):
    item_selecionado = tabela.selection()
    if not item_selecionado:
        return
    dados = tabela.item(item_selecionado[0], 'values')
    entrada_nome.delete(0, tk.END)
    entrada_nome.insert(0, dados[1])
    entrada_email.delete(0, tk.END)
    entrada_email.insert(0, dados[2])
    entrada_senha.delete(0, tk.END)
    entrada_senha.insert(0, dados[3])
    entrada_tipo.delete(0, tk.END)
    entrada_tipo.insert(0, dados[4])
    entrada_status.delete(0, tk.END)
    entrada_status.insert(0, dados[5])
    entrada_telefone.delete(0, tk.END)
    entrada_telefone.insert(0, dados[6])
    entrada_data_cadastro.delete(0, tk.END)
    entrada_data_cadastro.insert(0, dados[7])
    entrada_ultimo_acesso.delete(0, tk.END)
    entrada_ultimo_acesso.insert(0, dados[8])

def atualizar_usuario():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um usuário para atualizar.")
        return

    id_usuario = tabela.item(item_selecionado[0], 'values')[0]
    nome = entrada_nome.get().strip().replace("'", "''")
    email = entrada_email.get().strip().replace("'", "''")
    senha = entrada_senha.get().strip().replace("'", "''")
    tipo = entrada_tipo.get().strip().replace("'", "''")
    status = entrada_status.get().strip().replace("'", "''")
    telefone = entrada_telefone.get().strip().replace("'", "''")
    data_cadastro = entrada_data_cadastro.get().strip().replace("'", "''")
    ultimo_acesso = entrada_ultimo_acesso.get().strip().replace("'", "''")

    if not nome or not email or not senha or not tipo or not status or not telefone or not data_cadastro or not ultimo_acesso:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        database.atualizar_usuario(id_usuario, nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso)
        limpar_campos()
        listar_usuarios()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar usuário: {e}")

def excluir_usuario():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um usuário para excluir.")
        return
    id_usuario = tabela.item(item_selecionado[0], 'values')[0]
    try:
        database.excluir_usuario(id_usuario)
        limpar_campos()
        listar_usuarios()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir usuário: {e}")
    
janela = tk.Tk()

janela.title("Cadastro de Usuários")
janela.geometry("480x400")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entrada_email = tk.Entry(janela)
entrada_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Senha:").grid(row=2, column=0, padx=5, pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.grid(row=2, column=1, padx=5, pady=5)

tk.Label(janela, text="Tipo:").grid(row=3, column=0, padx=5, pady=5)
entrada_tipo = tk.Entry(janela)
entrada_tipo.grid(row=3, column=1, padx=5, pady=5)

tk.Label(janela, text="Status:").grid(row=4, column=0, padx=5, pady=5)
entrada_status = tk.Entry(janela)
entrada_status.grid(row=4, column=1, padx=5, pady=5)

tk.Label(janela, text="Telefone:").grid(row=5, column=0, padx=5, pady=5)
entrada_telefone = tk.Entry(janela)
entrada_telefone.grid(row=5, column=1, padx=5, pady=5)

tk.Label(janela, text="Data de Cadastro:").grid(row=6, column=0, padx=5, pady=5)
entrada_data_cadastro = tk.Entry(janela)
entrada_data_cadastro.grid(row=6, column=1, padx=5, pady=5)

tk.Label(janela, text="Último Acesso:").grid(row=7, column=0, padx=5, pady=5)
entrada_ultimo_acesso = tk.Entry(janela)
entrada_ultimo_acesso.grid(row=7, column=1, padx=5, pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=8, column=0, columnspan=2, pady=10)

tk.Button(frame_botoes, text="Cadastrar", command=cadastrar_usuario).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar_usuario).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir_usuario).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Limpar Campos", command=limpar_campos).pack(side=tk.LEFT, padx=5)

colunas = ("ID", "Nome", "Email", "Senha", "Tipo", "Status", "Telefone", "Data de Cadastro", "Último Acesso")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Nome")
tabela.heading("Email", text="Email")
tabela.heading("Senha", text="Senha")
tabela.heading("Tipo", text="Tipo")
tabela.heading("Status", text="Status")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Data de Cadastro", text="Data de Cadastro")
tabela.heading("Último Acesso", text="Último Acesso")

tabela.column("ID", width=50, anchor=tk.CENTER)
tabela.column("Nome", width=200, anchor=tk.W)
tabela.column("Email", width=100, anchor=tk.E)
tabela.column("Senha", width=100, anchor=tk.E)
tabela.column("Tipo", width=100, anchor=tk.E)
tabela.column("Status", width=100, anchor=tk.E)
tabela.column("Telefone", width=100, anchor=tk.E)
tabela.column("Data de Cadastro", width=100, anchor=tk.E)
tabela.column("Último Acesso", width=100, anchor=tk.E)

tabela.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

tabela.bind("<<TreeviewSelect>>", selecionar_usuario)

database.criar_tabela()
listar_usuarios()

janela.mainloop()