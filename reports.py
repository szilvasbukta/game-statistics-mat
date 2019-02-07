
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


def get_line_number_by_title(file_name, title):
    number_of_line = 0
    check = 0
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            number_of_line += 1
            if line[0] == title:
                check = 1
                break
        if check == 1:
            return number_of_line
        else:
            raise ValueError


def sort_abc(file_name):
    game_titles = []
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            if len(game_titles) == 0 or (game_titles[-1]).lower() < (line[0]).lower():
                game_titles.append(line[0])
            else:
                for x, title in enumerate(game_titles):
                    if (line[0]).lower() < title.lower():
                        game_titles.insert(x, line[0])
                        break
        return game_titles


def get_genres(file_name):
    game_genres = []
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            line = line.split("\t")
            if (len(game_genres) == 0 or (game_genres[-1]).lower() < (line[3]).lower()) and line[3] not in game_genres:
                game_genres.append(line[3])
            elif line[3] not in game_genres:
                for x, title in enumerate(game_genres):
                    if (line[3]).lower() < title.lower():
                        game_genres.insert(x, line[3])
                        break
        return game_genres
