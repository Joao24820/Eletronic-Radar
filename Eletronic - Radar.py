vel = float(input('Qual a velocidade atual do carro ?\nKM: '))
mul = (vel - 80) * 7.0

if vel > 80:
    print('Voce está correndo!! ')
    print('MULTADO!\nVoce exedeu o limite permitido que é de 80KM ')
    print('Será pago o valor de R$ 7.00 a cada Km ultrapassado')
    print('Voce deve pagar uma multa de R$ {:.2f}'.format(mul))
    print('Tenha um bom dia!! Dirija com segurança. ')
else:
    print('voce está dentro do limite da via. ')
    print('Tenha um bom dia!! Dirija com segurança. ')
