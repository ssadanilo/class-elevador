# Criando a classe Elevador
class Elevador:
    def __init__(self):
        self.totalCapacidade = 8
        self.atualCapacidade = 0
        self.totalAndar = 11
        self.atualAndar = 0
    
    def subir(self): # Criando método subir
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print(f'Subindo... {self.atualAndar}º andar')
        else:
            print('VOCÊ ESTÁ NO ANDAR MAIS ALTO')

    def descer(self): # Criando método descer
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print(f'Descendo... {self.atualAndar}º andar')
        else:
            print('VOCÊ JÁ ESTÁ NO TÉRREO')

    def entrar(self): # Criando método entrar
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print(f'Entrou 1 morador... Total {self.atualCapacidade} passageiros')
        else:
            print('O ELEVADOR ESTÁ CHEIO')

    def sair(self): # Criando método sair
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print(f'Saindo uma pessoa... Total {self.atualCapacidade} passageiros')
        else:
            print('NÃO TEM NINGUÉM')

# Uso da class Elevador
elevador = Elevador()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.entrar() # Não pode mais entrar, pois já atingiu a capacidade máxima de pessoas
elevador.subir() # Não pode mais subir, pois já atingiu a capacidade máxima de andares
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.sair()
elevador.descer()
elevador.sair()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.sair()
elevador.sair()
elevador.sair()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.sair()
elevador.sair()
elevador.sair()
elevador.sair() # Não pode mais sair, pois já atingiu desceram todas as pessoas
elevador.descer()  # Não pode mais descer, pois já atingiu a capacidade mínima de andares
