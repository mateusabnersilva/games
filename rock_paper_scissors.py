import random

def rock_paper_scissors():

    print('Vamos jogar Pedra, Papel, Tesoura!')

    r = "Pedra"
    p = "Papel"
    s = "Tesoura"
    all_choices = [r, p, s]

    usuario = input('Digite {}, {} e {}: '.format(r, p, s)).capitalize()

    if usuario not in all_choices:
        print('Opção inválida! Tente novamente.')
        return

    computador = random.choice(all_choices)

    print('Usuário escolheu: {}, computador escolheu: {}'.format(usuario, computador))

    # r>s, s>p, p>r

    if usuario == computador:
        print('Empate!')

    elif ((usuario == r and computador == s) or (usuario == p and computador == r) or(usuario == s and computador == p)):
        print('Parabéns! Você venceu!')
    else:
        print('Poxa, você perdeu! Tenta mais uma vez!')