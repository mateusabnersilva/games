#Distancia da viagem
distancia = float(input('Qual é a distância da viagem?'))
print('A distância da viagem é de {:.2f} km'.format(distancia))
 
if distancia <= 200:
    preco = (distancia * 0.50)
else:
    preco = (distancia * 0.45)

print('O preço da sua viagem é R${:.2f}'.format(preco))
