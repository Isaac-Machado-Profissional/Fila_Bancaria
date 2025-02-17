print("Bem vindo ao banco de Isaac Machado")

class Fila:
    """
        Classe que representa uma fila e seus comandos de inserção, remoção, próximo e vazio..
    """
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0

fila_idosos = Fila()
fila_normal = Fila()

def atender_clientes():
    """
     Função que visa atender a cada dois clientes idosos, um cliente normal.
    """

    count_idosos = 0
    while not fila_idosos.empty() or not fila_normal.empty():
        if count_idosos < 2 and not fila_idosos.empty():
            print(f"Atendendo idoso: {fila_idosos.remover()}")
            count_idosos += 1
        elif not fila_normal.empty():
            print(f"Atendendo cliente normal: {fila_normal.remover()}")
            count_idosos = 0
        else:
            count_idosos = 0

def main():
    while True:
        nome = input("Digite o seu nome: ")
        print(f"Olá {nome}, bem-vindo ao Banco!")

        idade = int(input("Digite a sua idade: "))
        print(f"Sua idade de {idade} foi armazenada com sucesso!")

        if idade >= 65:
            fila_idosos.inserir(nome)
        else:
            fila_normal.inserir(nome)

        continuar = input("Deseja adicionar mais clientes? (s/n): ")
        if continuar.lower() != 's':
            break

    atender_clientes()

if __name__ == "__main__":
    main()
