from emoji import emojize
from random2 import randrange
import tkinter as tk
import customtkinter
#variavel para os emogis
emg_dex = emojize(':person_cartwheeling: :')
emg_wis = emojize(':scroll: :')
emg_int = emojize(':brain: :')
emg_per = emojize(':eye: :')
emg_luck = emojize(':four_leaf_clover: :')
emg_car = emojize(':new_moon_face: :')
emg_str = emojize(':person_lifting_weights: :')
emg_dice = emojize(':game_die: :')
emg_mcn = emojize(":slot_machine: :")

def iniciar_programa():
    print(emojize( ':crossed_swords:  TACAXI-RPG :crossed_swords:  (D&D simplicado)'))
    NomeJogador = input('Digite seu nome !:')
    personagem = input('OK !, {} agora digite o nome do seu personagem !'.format(NomeJogador))
    print('Agora, você vai precisar usar um dado pra conseguir seu pontos de atributo (D20) OU aceitar os que vierem aqui ! \n \n Você quer rolar  os dados ?',emg_dice, '(1)' ' ou quer atributos aleatórios ?',emg_mcn, '(2)' '\n')
    Answer = int(input('1 ou 2 ? :'))
    
    #funcção para atributos aleatórios
    def Atributos_auto():
        dexterity = randrange(4,20)
        wisdom =  randrange(4,20)
        Inteligence = randrange(4,20)
        perception = randrange(4,20)
        luck = randrange(4,20)
        strength = randrange (4,20)
        charisma = randrange (4,20)
        print("_"*20)
        print("Personagem:",personagem)
        print("_"*20)
        print("Destreza",emg_dex,dexterity,"\n""Sabedoria",emg_wis,wisdom,"\n""Inteligência",emg_int,Inteligence,"\n""Percepsão",emg_per,perception) 
        print("Sorte",emg_luck,luck,"\n" "Força",emg_str,strength, "\n" "Carisma",emg_car,charisma)
        print("_"*20)
        print("Jogador:",NomeJogador)
        print("_"*20)
    #função para atributos rolados no dado fisico ou discord
    def Atributos_manual():
        dexterity = int(input(emojize('digite sua destreza !:person_cartwheeling: :')))
        wisdom = int(input(emojize('digite sua sabedoria !:scroll: :')))
        Inteligence = int(input(emojize('digite a inteligencia !:brain: :')))
        perception = int(input(emojize('digite a sua percepção !:eye: :')))
        luck = int(input(emojize('digite a sua sorte ! :four_leaf_clover: :')))
        strength = int(input(emojize('digite a sua força ! :person_lifting_weights: :')))
        charisma = int (input(emojize('digite o quão charmoso tu é :new_moon_face: :')))
        print("_"*20)
        print("Personagem:",personagem)
        print("_"*20)
        print("Destreza",emg_dex,dexterity,"\n""Sabedoria",emg_wis,wisdom,"\n""Inteligência",emg_int,Inteligence,"\n""Percepsão",emg_per,perception) 
        print("Sorte",emg_luck,luck,"\n" "Força",emg_str,strength, "\n" "Carisma",emg_car,charisma)
        print("_"*20)
        print("Jogador:",NomeJogador)
        print("_"*20)

    #escolhe o algoritmo de contrução da ficha
    if Answer == 1:
        Atributos_manual()
    if Answer == 2:
        Atributos_auto()

    



#TODO    
#0 tive a ideia de sortear nome de personagens de acordo com o sexo     
#1 tava pensando em recomendar classes pelo resultado dos atributo
#2 tenho que descobrir como criar uma interface de usuário para o programa
#3 poder ser legal adicionar ao atributo o valor do bonus de raça
#4 pode ser legal adicionar a função para rolar dano de ataque e 
#5 adicionar sub atributos e habilidades nos calculos


root = tk.Tk()
root.title("Gerador de Fichas")

background = tk.Frame(master = root, width= 600,height= 600, bg='magenta4')
background.pack()


def on_button_click():
    iniciar_programa()
CRIAR = tk.Button( text="gerar ficha", command= on_button_click) 
CRIAR.pack()
root.mainloop()

