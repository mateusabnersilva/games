from gtn import guess_the_number
from rps import rock_paper_scissors


while True:
    txt = """Mini Games!!!
   - Guess the Number (1)
   - Rock, Paper, Scissors (2)
   - Wordle (3)
   - ConnectFour (4)
   - Tic Tac Toe (5)

Selecione um jogo: (Pressione um número ou 'exit' para sair) \n"""

    escolha = input(txt)
   
    if escolha == '1':
        guess_the_number(100)

    elif escolha == '2':
        rock_paper_scissors()

    elif escolha == '3':
        pass

    elif escolha == '4':
        pass

    elif escolha == '5':
        pass
    elif escolha == 'exit':
        print('Saindo do mini games... See ya!')
        break