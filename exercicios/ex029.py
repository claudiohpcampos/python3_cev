vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (vel - 80) * 7
    print('\033[31mVocê deve pagar uma multa de \33[33mR${:.2f}'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
