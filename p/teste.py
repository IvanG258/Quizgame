print('jogo de advinhacao')
print('===================')

print('Advinhe o numero que aparecera na saida')
print('-------------------------------------------')
valor=input('digite um numero aleatorio e veja se coincide com a saida:')
import random;
print(random.randrange(1,7))
if(valor==random.randrange(1,7)):
    print('Voce ganhou')
else:
        print('infelizmente voce perdeu')
