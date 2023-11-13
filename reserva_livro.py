print('Ambiente de reserva de livro! \n')
class Livro:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def reservar(self):
        if self.quantidade > 0:
            self.quantidade -= 1
            print(f"Reserva do livro {self.titulo} realizada com sucesso!\n")
        else:
            print(f"Desculpe, o livro {self.titulo} está esgotado.\n")

# Lista de livros
livros = [
    Livro("O Hobbit", 3),
    Livro("Harry Potter", 1),
    Livro("O Pequeno Príncipe", 0)
    ]

# Mostrar ao usuário a lista de livros
print("Livros disponíveis:")
for i, livro in enumerate(livros):
    print(f"{i+1}. {livro.titulo}")

# Solicitar ao usuário que escolha um livro
escolha = int(input("Digite o número do livro que você deseja reservar: ")) - 1

# Verificar se a escolha é válida
if 0 <= escolha < len(livros):
    livros[escolha].reservar()
else:
    print("Escolha inválida.")