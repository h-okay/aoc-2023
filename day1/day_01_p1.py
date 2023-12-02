def extract(line):
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in line[::-1] if char.isdigit())
    calibration_value = int(first_digit + last_digit)
    return calibration_value

if __name__ == "__main__":
    with open("day_01.in") as f:
        lines = f.read().strip().splitlines()

    total_sum = sum(extract(line) for line in lines)
    print(total_sum)
