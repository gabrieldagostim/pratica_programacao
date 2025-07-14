from utils import input_
from restaurante import Restaurante


class Sorveteria(Restaurante):
    ''' Inicializando sorveteria'''
    def __init__(self, nome_restaurante, tipo_cozinha, saldo_conta, limite_credito, sabores_sorvt:dict[list[str,int]]=None):

        if sabores_sorvt is None:
            sabores_sorvt = {
                1: ['Chocolate',5],
                2: ['Morango', 5],
                3: ['Baunilha', 5],
                4: ['Limão', 3.60],
                5: ['Pistache', 8]
                }
            
        super().__init__(nome_restaurante, tipo_cozinha, saldo_conta, limite_credito)

        self.sabores_sorvt = sabores_sorvt


    def listar_precos(self):
        for sabor, preco in self.sabores_sorvt.values():
            print(f'{sabor} --> R$: {preco:.2f}')


    def listar_sabores(self):
        sabores = self.sabores_sorvt
        print('Sabores disponíveis:')
        
        for i, sabor in sabores.items():
            print(f"{i} - {sabor[0]} - R$ {sabor[1]:.2f}")

    def vender_sorvete(self, opcao_vendida):
        stts_venda = False
        # recebendo o valor do sorvete
        if opcao_vendida in self.sabores_sorvt.keys():
            item = self.sabores_sorvt[opcao_vendida]
            preco_item = item[1]

            if self.financeiro.atualiza_saldo(preco_item):
                return True
                # TODO aplicar sistema de stock aqui
            else:
                return False
        else:

            print(f'Sabor inexistente, você informou: {opcao_vendida}, e não temos esse sabor')

        return stts_venda


    def servir_sorvete(self):
        self.listar_sabores()

        sabor_escolhido = input_('Digite numero do sabor desejado: ','int')

        if self.vender_sorvete(opcao_vendida=sabor_escolhido):
            print(f'Segue seu sorvete de {self.sabores_sorvt[sabor_escolhido][0]}')
        # 


chico_srvts = Sorveteria(nome_restaurante='chiquinho sorvetes',tipo_cozinha='Com geladeira', saldo_conta=5000, limite_credito=0)

chico_srvts.servir_sorvete()
