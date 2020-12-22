def main():
    f = open('input.txt', 'r')
    lines = f.read().split('\n')
    print(parse_lines(lines[:-1]))

def parse_lines(lines):
    n = 0
    for line in lines:
        if parse_line(line):
            n += 1
    return n

def parse_line(line):
    """
    Parses a given line and returns whether the password was valid.
    """
    components = line.split()
    num_range = components[0].split('-')
    pos1 = int(num_range[0]) - 1
    pos2 = int(num_range[1]) - 1

    letter = components[1][0]

    password = components[2]

    return check_password(pos1, pos2, letter, password)
                          
def check_password(pos1, pos2, letter, password):
    if password[pos1] == letter:
        return password[pos2] != letter
    else:
        return password[pos2] == letter

if __name__ == '__main__':
    main()
