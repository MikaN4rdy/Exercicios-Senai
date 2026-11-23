
class ContaBancaria:
    def __init__(self, __saldo):
        self.__saldo = __saldo   # privado


    def get_saldo(self):       # Consultar  
        return self.__saldo


    def depositar(self, DepositarValor): # setter
        if DepositarValor > 0:
            self.__saldo += DepositarValor
conta = ContaBancaria(100) 

print("Saldo inicial", conta.get_saldo())

#Perguntar valor do depósito

valor = float(input("Digite o valor do depósito."))
conta.depositar(valor)

#Mostrando saldo
print("Saldo atual: ", conta.get_saldo())