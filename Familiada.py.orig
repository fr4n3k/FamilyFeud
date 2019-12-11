import random

def number_of_players():#zwraca nam TYLKO 1 liczbe<!!!!!
    verify=True
    while verify:
        no_of_players=int(input("What's the number of players? (2 - 4): "))
        if no_of_players in range(1,5):
            print(" ")
            verify=False
        else:
            continue
    return no_of_players

def nick(players):#zwraca nam graczy
    nickname=[]
    for i in range(players):
        name=input("Enter a nickname: ")
        nickname.append(name)
    return nickname

def print_players(list_of_players):
    
    for index, nick in enumerate(list_of_players):
        print("Player no", index + 1, "is: ", nick)


def number_of_rounds():

    while True:
        rounds=input("How many rounds would you like to play? (1 - 5): ")
        if rounds in range(rounds):
            print(" ")
            return int(rounds)
        else:
            continue

def read_file():
    lista =[]
    text = open("/home/franekj/Documents/PythonWorkshop/TopTenFoods.txt").read()
    lines = text.split('\n')
    for line in lines:
        lista.append(line)
    del lista[-1]

    lista_question_answer = []
    for item in lista[:]:
        lista_question_answer.append(item.split(','))
    current_game_answers = {}
    for i in range (0, len(lista_question_answer)):
        current_game_answers[lista_question_answer[i][0]]= lista_question_answer[i][1]
    return current_game_answers  

def create_table() -> list:
    ''' create_table prints an empty table of 10 answers and returns it'''
    row=["----------", "---"].copy()
    answers_table =[]
    for i in range(10):
        answers_table.append(row.copy())
    for index, row in enumerate(answers_table):
        print(index+1, "  ".join(row))    
    return answers_table


def game(current_game_answers) -> list:

    print ("Which food is most popular?")
    answer=input("Your answer is: " )
    if answer in current_game_answers.keys():
        print(current_player_answer, current_game_answers[current_player_answer])
        list_answer_score =[current_player_answer, current_game_answers[current_player_answer]]
        
    else:
        list_answer_score=["Wrong aswer", 0]

    return list_answer_score
    


def change_table(game_table, answer_score):
    
    which_element=10-int(answer_score[1])
    if which_element in range(0, 10):
        game_table[which_element]=answer_score
        print()
        for index, row in enumerate(game_table):
            print(index+1, "  ".join(row))
    else:
        print("wrong answer")        
    return game_table

def mix_players(players_list):
    temp_players=list(players_list)
    random.shuffle(temp_players)
    print("List of players: ",  temp_players)
    return temp_players

temp_players = mix_players(nickname)

def round(temp_players):

    for i in range(len(temp_players)):
        print(temp_players[i], 'is answering:')
        game()



how_many_players = number_of_players()
list_of_playing_people = nick(how_many_players)
print_players(list_of_playing_people)



current_game_table = create_table()
change_table(current_game_table, table_position)
table_position = game(read_file())
