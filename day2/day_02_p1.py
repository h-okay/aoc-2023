def getIdIfValid(row):
    game, results = row.split(":")
    id = game.split(" ")[1]
    sets = results.strip().split("; ")

    allowed = {"red": 12, "green": 13, "blue": 14}
    for cube_set in sets:
        pulls = cube_set.split(", ")
        for pull in pulls:
            count, color = pull.split(" ")
            if int(count) > allowed[color]:
                return 0

    return int(id)


if __name__ == "__main__":
    with open("day_02.in") as f:
        data = f.read().strip().splitlines()

    total = 0
    for row in range(len(data)):
        total += getIdIfValid(data[row])

    print(total)
