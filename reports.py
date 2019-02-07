
# Report functions


def count_games(file_name):
    with open(file_name, 'r') as opened_file:
        counter = 0
        for line in opened_file:
            counter += 1
        return counter


def decide(file_name, year):
    with open(file_name, 'r') as opened_file:
        check = 0
        for line in opened_file:
            line = line.split("\t")
            if int(line[2]) == year:
                check = 1
        if check == 1:
            return True
        else:
            return False


def get_latest(file_name):
    basic_year = ['', 0]
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            if int(line[2]) > basic_year[1]:
                basic_year[1] = int(line[2])
                basic_year[0] = line[0]
        return basic_year[0]


def count_by_genre(file_name, genre):
    number_of_games = 0
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            if line[3] == genre:
                number_of_games += 1
        return number_of_games
