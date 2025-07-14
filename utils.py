def input_(prompt: str, tipo_esperado: str):
    '''Input com conversão de tipo'''
    while True:
        valor_bruto = input(prompt)

        if not valor_bruto.strip():
            print('Entrada vazia.')
            return None

        try:
            match tipo_esperado:
                case 'str':
                    return valor_bruto
                case 'int':
                    return int(valor_bruto)
                case 'float':
                    return float(valor_bruto)
                case _:
                    print('Tipo não suportado.')
                    return None
        except ValueError:
            print(f'Entrada inválida. Esperado: {tipo_esperado}')
