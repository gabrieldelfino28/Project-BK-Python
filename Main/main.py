import os

vlt = float(0)
i = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0
total = float(0)

while (i != 0):
    print('------------------------------MENU------------------------------')
    print('\nSelecione um Combo: \n')
    print('\n1 - Para 1x Combo WHOPPER')
    print('\n2 - Para 1x Cheddar Duplo + 1x Batata Suprema + 1x Free Refill')
    print('\n3 - Para 1x Combo WHOPPER + 1x Cheddar')
    print('\n4 - Para 2x Combo WHOPPER + 1x Batata Media + 1x Free Refill\n')
    op = int(input())

    if (op == 1):
        print('\nVoce selecionou 1x Combo WHOPPER\n')
        c1+=1
        vlt=vlt+19.90
        z = int(input('\nDeseja Pedir mais um combo? (1 - Sim/0 - Nao) '))
        if (z == 1):
            continue
        else :
            i=0

    elif (op == 2):
        print('\nVoce selecionou 1x Cheddar Duplo + 1x Batata Suprema + 1x Free Refiill\n')
        c2+=1
        vlt = vlt + 19.90
        z = int(input('\nDeseja Pedir mais um combo? (1 - Sim/0 - Nao) '))
        if (z == 1):
            continue
        else:
            i=0

    elif (op == 3):
        print('\nVoce selecionou 1x Combo WHOPPER + 1x Cheedar\n')
        c3+=1
        vlt = vlt + 24.90
        z = int(input('\nDeseja Pedir mais um combo? (1 - Sim/0 - Nao) '))
        if (z == 1):
            continue
        else:
            i=0

    elif (op == 4):
        print('\nVoce selecionou 2x Combo WHOPPER + 1x Batata Media + 1x Free Refill\n')
        c4+=1
        vlt = vlt + 26.90
        z = int(input('\nDeseja Pedir mais um combo? (1 - Sim/0 - Nao) '))
        if (z == 1) :
            continue
        else:
            i=0

    else:
        print('\nValor Invalido')
        break

    total = total + vlt
    print('\nQuantidade de combos vendidos:\n1o Combo:',c1,'vezes''\n2o Combo:',c2,'vezes''\n3o Combo:',c3,'vezes''\n4o Combo:',c4,'vezes')
    print('\nValor total arrecadado %.2f' % total)


os.system("pause")
