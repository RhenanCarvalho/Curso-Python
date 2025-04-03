#idade = 25
#altura = 1.75
#
#resultado = (idade >= 18) and (altura >= 1.70)
#
#print(resultado)

print('Faça a sua inscrição no evento!')

idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))

if (altura >= 1.70) and (idade >= 18):
    print('Bem-vindo ao evento!')
else:
    print('Você não atende aos requisitos mínimos.')


print('Verifique se a porta e a janela estão abertas ou fechadas! Para aberta, digite "a" e para fechada digite "f".')

porta = input('A porta está aberta ou fechada? ')
janela = input('A janela está aberta ou fechada? ')

if (porta != 'a' and porta != 'f') or (janela != 'a' and janela != 'f'):
    print('Letra inválida, digite "a" para aberta e "f" para fechada')
else:
    if (porta == 'a') or (janela == 'a'):
        print('Alarme tocando!!! Portas ou janelas abertas')
    else:
        print('Está tudo fechado!')


tem_dinheiro = True
tem_dinheiro = not tem_dinheiro

msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)