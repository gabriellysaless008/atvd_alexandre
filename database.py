import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    status TEXT NOT NULL,
    telefone INTEGER NOT NULL,
    data_cadastro DATE,
    ultimo_acesso DATE
    )
    ''')

    conexao.commit()
    conexao.close()

#Cadastrar Usuário

def cadastrar_usuario(nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO usuarios (nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso))

    conexao.commit()
    conexao.close()

#Listar Usuários

def listar_usuarios():
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    conexao.close()
    return usuarios

#Atualizar Usuário

def atualizar_usuario(id, nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('''
    UPDATE usuarios
    SET nome = ?, email = ?, senha = ?, tipo = ?, status = ?, telefone = ?, data_cadastro = ?, ultimo_acesso = ?
    WHERE id = ?
    ''', (nome, email, senha, tipo, status, telefone, data_cadastro, ultimo_acesso, id))

    conexao.commit()
    conexao.close()

#Excluir Usuário

def excluir_usuario(id):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()