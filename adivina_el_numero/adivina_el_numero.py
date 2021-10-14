import random 


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    vidas = 4

    while numero_aleatorio != numero_elegido:

        if vidas == 1:
            print('CUIDADO! TE QUEDA SOLO UNA VIDA')
        
        if vidas == 0:
            print('No tienes mas vidas... GAME OVER')
            break

        if numero_elegido < numero_aleatorio:
            print('Intenta con un número mas grande')
            vidas -=1

        elif numero_elegido > numero_aleatorio:
            print('Intenta con un número mas pequeño')
            vidas -=1

        numero_elegido = int(input('Elige un numero entre 1 y 100: '))

    print('Ganaste!')


if __name__ == '__main__':
    run()    
 