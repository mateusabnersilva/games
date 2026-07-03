velocidade = float(input('Qual a velocidade do carro?'))

if velocidade > 80:

    print('MULTADO! Você excedeu o limite de velocidade.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    print('Consulte o código de trânsito para mais informações.')
    print('www.denatran.gov.br')

else:
    print('Parabéns! Você está dentro do limite de velocidade.')

print('Tenha um bom dia! Dirija com segurança!')