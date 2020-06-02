from time import sleep
c =0
op = [1,2]
def linha(a='='):
    print('{}'.format(a) * 40)
def cab(a,b='='):
    linha(b)
    print('\033[1;35m{}\033[m'.format(a).center(50))
    linha(b)
def comp(qu,li):
    rep=1
    while rep <= li:
        if (qu - rep) % (li + 1) == 1:
            rep+=1
        else:
            break
    return rep
def jog(li):
    while True:
        ret = int(input('\033[1;33m> \033[m\033[1;34mDIGITE O QUANTO DESEJA RETIRAR: \033[m'))
        if ret > li:
            print('\033[31;1mNÚMERO INVÁLIDO!\033[m')
        else:
            break
    return ret

cab('JOGO "MIN"')
print('\033[1;33m1> \033[m\033[1;34mPARTIDA CASUAL\033[m')
print('\033[1;33m2> \033[m\033[1;34mTORNEIO\033[m')
opi = int(input('\033[1;33mOPÇÃO: \033[m'))
if opi not in op:
    while True:
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        opi = int(input('\033[1;33mDIGITE NOVAMENTE: \033[m'))
        if opi in op:
            break
if opi == 1:
    cab('JOGO CASUAL')
    qu = int(input('\033[1;33m> \033[m\033[1;34mDIGITE A QUANTIDADE DE PEÇAS: \033[m'))
    li = int(input('\033[1;33m> \033[m\033[1;34mDIGITE UM LIMITE DE PEÇAS: \033[m'))
    linha('-')
    if qu % (li + 1) == 0:
        print('\033[1;32mVOCÊ COMEÇA: \033[m')
        sleep(1)
        linha('-')
        compv = False

    else:
        print('\033[1;31mO COMPUTADOR COMEÇA\033[m')
        linha('-')
        sleep(1)
        compv = True
    while True:
        if compv:
            print('\033[1;31mPROCESSANDO...\033[m')
            sleep(1)
            qu -= comp(qu,li)
            pc = comp(qu,li)
            sleep(1)
            print('\033[1;31mO COMPUTADOR TIROU {}\033[m'.format(1+pc))
            sleep(1)
            print('\033[1;33mAINDA RESTAM {} PEÇAS!\033[m'.format(qu))
            compv = False
            linha('-')
        else:
            print('\033[1;32m> SUA VEZ\033[m')
            qu -= jog(li)
            sleep(1)
            compv= True
            print('\033[1;33mAINDA RESTAM {} PEÇAS!\033[m'.format(qu))
            linha('-')
        if qu == 0:
            break
    print('\033[1;31mVOCÊ PERDEU!\033[m')
if opi == 2:
    cab('TORNEIO')
    for c in range(1,4):
        cab('JOGO {}'.format(c),'-')
        qu = int(input('\033[1;33m> \033[m\033[1;34mDIGITE A QUANTIDADE DE PEÇAS: \033[m'))
        li = int(input('\033[1;33m> \033[m\033[1;34mDIGITE UM LIMITE DE PEÇAS: \033[m'))
        linha('-')
        if qu % (li + 1) == 0:
            print('\033[1;32mVOCÊ COMEÇA: \033[m')
            sleep(1)
            linha('-')
            compv = False

        else:
            print('\033[1;31mO COMPUTADOR COMEÇA\033[m')
            linha('-')
            sleep(1)
            compv = True
        while True:
            if compv:
                print('\033[1;31mPROCESSANDO...\033[m')
                sleep(1)
                qu -= comp(qu, li)
                pc = comp(qu, li)
                sleep(1)
                print('\033[1;31mO COMPUTADOR TIROU {}\033[m'.format(1 + pc))
                sleep(1)
                print('\033[1;33mAINDA RESTAM {} PEÇAS!\033[m'.format(qu))
                compv = False
                linha('-')
            else:
                print('\033[1;32m> SUA VEZ\033[m')
                qu -= jog(li)
                sleep(1)
                compv = True
                print('\033[1;33mAINDA RESTAM {} PEÇAS!\033[m'.format(qu))
                linha('-')
            if qu == 0:
                print('\033[1;31mVOCÊ PERDEU!\033[m')
                break
    print('\033[1;31mO COMPUTADOR VENCEU: 3 X 0\033[m')