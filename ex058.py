from random import randint

counter = 1
rand = randint(0, 10)

print('Jogo da Adivinhação')
number = int(input('Digite um número entre 0 e 10: '))
while number > 10 or number < 0:
    number = int(input('Você digitou um número indisponível, ENTRE 0 e 10: '))
while number <= 10 and number >= 0 and rand <= 10:
    if number != rand:
        number = int(input('Errou, digite outro: '))
        counter += 1
    else:
        print('Acertou!! Você tentou {} vezes.' .format(counter))
        rand += 11

#q gambiarra kkkkkk