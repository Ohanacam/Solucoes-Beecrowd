fase1 = input()
fase2 = input()
fase3 = input()

if fase1 == 'vertebrado':
    if fase2 == 'ave':
        if fase3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if fase3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if fase2 == 'inseto':
        if fase3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if fase3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')