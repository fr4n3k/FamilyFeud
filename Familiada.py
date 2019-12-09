import random

def number_of_players():

    while True:
        no_of_players=input("What's the number of players? (2 - 4): ")

        if no_of_players=="2" or no_of_players =="3" or no_of_players== "4":
            print(" ")
            return int(no_of_players)
        else:
            continue

def nick(no_of_players):
    nickname=[]
    for i in range(no_of_players):
        name=input("Enter a nickname: ")
        nickname.append(name)
        
    return nickname

nickname=nick(number_of_players())

def print_players(list_of_players):
    
    for index, nick in enumerate(list_of_players):
        print("Player no", index + 1, "is: ", nick)

def number_of_rounds():

    while True:
        rounds=input("How many rounds would you like to play? (1 - 5): ")

        if rounds== "0" or rounds=="2" or rounds =="3" or rounds== "4" or rounds== "5":
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
    answer_dict = {}
    for i in range (0, len(lista_question_answer)):
        answer_dict[lista_question_answer[i][0]]= lista_question_answer[i][1]
    return answer_dict
    
    
    

def create_table():

    row=["----------", "---"].copy()
    table =[]
    for i in range(10):
        table.append(row.copy())
    for index, row in enumerate(table):
        print(index+1, "  ".join(row))    
    return table

table = create_table()

def game(answer_dict):

    print ("Which food is most popular!")
    answer=input("Your answer is: " )
    if answer in answer_dict.keys():
        print(answer, answer_dict[answer])
        table_position=[answer, answer_dict[answer]]
        
    else:
        table_position=["Wrong aswer", 0]

    return table_position
    

table_position = game(read_file())
def change_table(table, table_position):
    
    which_element=10-int(table_position[1])
    if which_element in range(0, 10):
        table[which_element]=table_position
        print()
        for index, row in enumerate(table):
            print(index+1, "  ".join(row))
    else:
        print("wrong answer")        
    return table

change_table(table, table_position)

def mix_players(nickname):
    temp_players=list(nickname)
    random.shuffle(temp_players)
    print("List of players: ",  temp_players)
    return temp_players

temp_players = mix_players(nickname)

#print(round(nickname))

#not ready yet
def round(temp_players):

    for i in range(len(temp_players)):
        print("odpowiada ", temp_players[i])
        game()

