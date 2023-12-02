def minNumberOfCubes(row):
    results = row.split(":")[1]
    sets = results.strip().split("; ")

    counter = {"red": 0, "green": 0, "blue": 0}
    for cube_set in sets:
        pulls = cube_set.split(", ")
        for pull in pulls:
            count, color = pull.split(" ")
            counter[color] = max(counter[color], int(count))

    return counter


if __name__ == "__main__":
    with open("day_02.in") as f:
        data = f.read().strip().splitlines()

    total = 0
    for row in range(len(data)):
        mul = 1
        mins = minNumberOfCubes(data[row])
        for v in mins.values():
            mul *= v
        total += mul

    print(total)
