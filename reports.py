
# Report functions


def count_games(file_name):
    with open(file_name, 'r') as opened_file:
        counter = 0
        for line in opened_file:
            counter += 1
        return counter
