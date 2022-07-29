larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
print('Sua parede tem a dimensão de {} X {} e sua área é de {}m².'.format(larg, alt, larg * alt))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((larg * alt) / 2))
