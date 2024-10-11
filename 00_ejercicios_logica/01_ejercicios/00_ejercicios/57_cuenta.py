"""
Haz una clase cuenta con titular, iban y
saldo se puede sacar y meter dinero
"""

class Cuenta:
    def __init__(self, titular, iban, saldo):
        self.titular = titular
        self.iban = iban
        self.saldo = saldo
    
    def ingreso(self, cantidad):
        self.saldo += cantidad
        
    def retirada(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            
            
cuenta1 = Cuenta("Josue", "ES50", 100)

cuenta1.ingreso(350)
cuenta1.retirada(200)

print(cuenta1.saldo)