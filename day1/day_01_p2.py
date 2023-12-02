also_valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract(line):
    digits = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
        
        for j, spelled in enumerate(also_valid): 
            if line[i:(i+len(spelled))] == spelled: # look ahead
                digits.append(j + 1)
                break

    first_digit = digits[0]
    last_digit = digits[-1]

    calibration_value = first_digit * 10 + last_digit
    return calibration_value

if __name__ == "__main__":
    with open("day_01.in") as f:
        lines = f.read().strip().splitlines()

    total_sum = sum(extract(line) for line in lines)
    print(total_sum)
