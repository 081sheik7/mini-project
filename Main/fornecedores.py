import tkinter as tk
from tkinter import ttk

def cadastrar_fornecedor():
    # Aqui você pode adicionar o código para salvar os dados do fornecedor em um banco de dados ou fazer o que for necessário.
    nome = nome_entry.get()
    cnpj = cnpj_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    celular = celular_entry.get()
    cep = cep_entry.get()
    endereco = endereco_entry.get()
    numero = numero_entry.get()
    complemento = complemento_entry.get()
    cidade = cidade_entry.get()
    bairro = bairro_entry.get()
    estado = estado_entry.get()
    
    # Exemplo: Imprimir os dados
    print("Nome:", nome)
    print("CNPJ:", cnpj)
    print("Email:", email)
    print("Telefone:", telefone)
    print("Celular:", celular)
    print("CEP:", cep)
    print("Endereço:", endereco)
    print("Número:", numero)
    print("Complemento:", complemento)
    print("Cidade:", cidade)
    print("Bairro:", bairro)
    print("Estado:", estado)

# Cria a janela principal
root = tk.Tk()
root.title("Cadastro de Fornecedores")

# Define uma cor de fundo mais agradável
root.configure(bg='#E0F2F1')

# Crie um frame para o título
title_frame = tk.Frame(root, bg='#00A896')
title_frame.pack(pady=20)

# Adicione um título maior e em destaque no topo central da tela
title_label = tk.Label(title_frame, text="Cadastro de Fornecedores", font=('Arial', 24, 'bold'), bg='#00A896', fg='white', padx=20, pady=10)
title_label.pack()

# Crie um frame para os campos
fields_frame = tk.Frame(root, bg='#E0F2F1')
fields_frame.pack(pady=20)

# Divide a interface em dois frames, um para os campos à esquerda e outro para os campos à direita
left_frame = tk.Frame(fields_frame, bg='#E0F2F1')
left_frame.pack(side=tk.LEFT)

# Adicione uma barra de divisão
separator = ttk.Separator(fields_frame, orient='vertical')
separator.pack(side='left', fill='y', padx=10)

right_frame = tk.Frame(fields_frame, bg='#E0F2F1')
right_frame.pack(side=tk.RIGHT)

# Define um estilo maior para rótulos
label_style = {'bg': '#E0F2F1', 'font': ('Arial', 16)}

# Define um estilo maior para campos de entrada
entry_style = {'font': ('Arial', 16)}

# Cria os campos de entrada e rótulos com os estilos maiores
campos = [
    ("Nome:", ""),
    ("CNPJ:", ""),
    ("Email:", ""),
    ("Telefone:", ""),
    ("Celular:", ""),
    ("CEP:", ""),
    ("Endereço:", ""),
    ("Número:", ""),
    ("Complemento:", ""),
    ("Cidade:", ""),
    ("Bairro:", ""),
    ("Estado:", "")
]

for i, (label_text, entry_text) in enumerate(campos):
    label = tk.Label(left_frame if i < 6 else right_frame, text=label_text, **label_style)
    label.pack()
    
    entry = tk.Entry(left_frame if i < 6 else right_frame, **entry_style)
    entry.insert(0, entry_text)
    entry.pack()

# Botão para cadastrar o fornecedor maior e mais atraente
cadastrar_button = tk.Button(root, text="Cadastrar", command=cadastrar_fornecedor, bg='#00A896', fg='white', font=('Arial', 20))
cadastrar_button.pack()

root.geometry("500x600")  # Define o tamanho da janela
root.mainloop()
