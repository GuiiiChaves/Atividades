# Dicionário para armazenar informações de usuários (usuário, senha)
usuarios = {}

# Dicionário para armazenar informações de livros (livro, disponibilidade)
livros = {"Pequeno Principe": True, "Diario de um Banana": True, "Harry Potter": True}

usuario_logado = None

def cadastrar_usuario():
    global usuarios
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")

def fazer_login():
    global usuario_logado
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuarios.get(usuario) == senha:
        usuario_logado = usuario
        print(f"Bem-vindo, {usuario}!")
    else:
        print("Credenciais incorretas. Tente novamente.")

def listar_livros():
    global livros
    print("Livros disponíveis:")
    for livro, disponibilidade in livros.items():
        if disponibilidade:
            print(livro)

def alugar_livro():
    global usuario_logado, livros
    if usuario_logado is None:
        print("Faça o login primeiro.")
        return
    
    listar_livros()
    livro = input("Digite o nome do livro que deseja alugar: ")
    
    if livros.get(livro):
        livros[livro] = False
        print(f"{usuario_logado} alugou o livro {livro}.")
    else:
        print(f"O livro {livro} não está disponível para aluguel.")

while True:
    print("\nMenu:")
    print("1. Cadastrar usuário")
    print("2. Fazer login")
    print("3. Listar livros disponíveis")
    print("4. Alugar livro")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        listar_livros()
    elif opcao == "4":
        alugar_livro()
    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
