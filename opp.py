# # class Cadastro: 
# #        def __init__(self):
# #            self.email = None
# #            self.age = None
# #            self.name  =  None

# #        def display(self):
# #            self.email = input('Digite seu e-mail')
# #            self.name = input('Digite seu nome ')
# #            self.age = input('Digite idade')
# #            print(f'O nome é {self.name}, idade: {self.age}, email:{self.email}') 
 
# #        def verification(self):
# #            if not self.name  or not self.email or not self.age: 
# #               print ('Digite o nome, sua idade e email ')
               
# #            else:
# #                print(f'Ola{self.name}seja bem vindo')
            

# # # cadastro = Cadastro () #filho
# # cadastro2 = Cadastro()
# # # cadastro.display()
# # cadastro2.display()
# # cadastro2.verification()


# # 1 -

# class Dog: 
#       def __init__(self, name):
#           self.name =  name


#       def latir(self):
#           print(f'Late {self.name}!')         
#           print('wolf!!!')

# my_dog =  Dog('rex')

# my_dog.latir()


# # 2


# class Retangulo: 
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura


#     def calcular(self):
#          print(self.altura * self.largura)





# area = Retangulo(10,50)   
# area.calcular()



# class Car: 
#       def __init__(self):
#            self.velocity = 0


#       def aumentar(self): 
#             for n  in range(self.velocity, 101,5): 
#               print(f'Aumentando a velocidade: {n}')
 

# car = Car()
# car2 = Car()
# car.aumentar()
# car2.aumentar()



# 4 - Crie uma classe chamada Gato que herda da classe Cachorro 
# do exercício anterior. 
#  O método latir da classe Cachorro deve ser substituído por 
# um método miar na classe 
# Gato que imprime "Miau!".


# class Cat: 
#      def __init__(self, som):
#           self.som = som



#      def miar(self): 
#          print('Miau...')

# cat =  Cat('Miau')
# cat.miar()

# ***Exercício 4: Crie uma classe chamada `Conta_bancaria` 
# com um atributo `saldo` inicializado com 0. Em seguida, 
# crie métodos `deposito` e `saque` que atualizem o saldo. 
# Crie um objeto da classe `ContaBancaria`, faça um depósito 
# e um saque, e imprima o saldo resultante.***


class Conta_bancaria:
    def __init__(self):
          self.saldo = 0  


    def deposito(self, valor1):
        self.saldo += valor1
        print()
    
    def saque(self, valor): 
        if valor <= self.saldo:
            result = self.saldo - valor  
            print(result) 
        else: 
           print('saldo insuficiente!') 

minha_conta = Conta_bancaria()    
minha_conta.deposito(150)
minha_conta.saque(50)


     








