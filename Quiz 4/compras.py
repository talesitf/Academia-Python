def valor_a_devolver(prateleiras,sistema,compras):
    valor_prateleira = 0
    valor_sistema = 0
    retorno = 0
    for produto in compras:
        etiqueta = prateleiras[produto[0]]
        caixa = sistema[produto[0]]
        valor_prateleira += etiqueta[produto[1]]*produto[2]
        valor_sistema += caixa[produto[1]]*produto[2]
    retorno = valor_sistema - valor_prateleira
    return retorno
print(valor_a_devolver({
    'requeijão': {
        'Minas': 5,
        'Buritis': 6,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10,
        'Lavagem Perfeita': 12.5,
        'Cromo': 15.7
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 25
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4,
        'Urbano': 5.3
    }
},{
    'requeijão': {
        'Minas': 5,
        'Buritis': 7,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10.5,
        'Lavagem Perfeita': 12.8,
        'Cromo': 15.7
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 26
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4.5,
        'Urbano': 5.3
    }
},[
    ['arroz','Prato Fundo',1],
    ['requeijão','Buritis',2],
    ['requeijão','Queijinho',1],
    ['sabão','Pura Espuma',3]
]))