from utils import input_

class Restaurante:

    def __init__(self, nome_restaurante, tipo_cozinha, saldo_conta, limite_credito):
        ''' Inicializando restaurante'''

        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

        self.financeiro = Financeiro(saldo_conta, limite_credito)


class Financeiro:

    def __init__(self, saldo_conta, limite_credito):
        self.saldo_conta = saldo_conta
        self.limite_credito = limite_credito

    def mostra_saldo_conta(self):
        print(f'Saldo em conta -> R${self.saldo_conta}')

    def atualiza_saldo(self, valor:float):
        ''' Atualiza o saldo da conta, retorna True para bem sucedido e false para falha'''
        try:
            self.saldo_conta = self.saldo_conta + valor
            self.mostra_saldo_conta()
            return True
        except Exception as e:
            print(f'Não foi possível efetuar a venda, um erro aconteceu {e}')
            return False
        

    def pagar(self):
        valor_pago = input_('Qual valor deseja PAGAR R$: ', 'float')

        if valor_pago > self.saldo_conta:
            print(f'Saldo insuficiente para pagar a conta! \nA pagar: R${valor_pago}\nSaldo R$: {self.saldo_conta}')
        
        else:
            self.atualiza_saldo(valor=(-valor_pago))
            print(f'Saldo atualizado R$ {self.saldo_conta}')


    def receber(self):
        valor_receber = input_('Qual valor deseja RECEBER R$: ', 'float')

        if valor_receber <= 0:
            return None
        
        else:
            self.atualiza_saldo(valor=valor_receber)
            print(f'Saldo atualizado R$ {self.saldo_conta}')

# fin = Financeiro(saldo_conta=1000,limite_credito=0)
# fin.pagar()