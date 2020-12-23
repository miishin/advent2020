MULTIPLIER = 8

def main():
    f = open('input.txt', 'r')
    lines = f.read().split()
    max_id = 0
    for line in lines:
        id = calculate_id(*split_line(line))
        if id > max_id:
            max_id = id
    print('Max ID:')
    print(max_id)

def split_line(line):
    rowseq = line[:7]
    colseq = line[7:]
    return (rowseq, colseq)

def calculate_id(rowseq, colseq):
    # Calculates ID value
    row_num = get_row_or_column(rowseq, 'B', 'F')
    col_num = get_row_or_column(colseq, 'R', 'L')
    id = row_num * MULTIPLIER + col_num
    return id
    
def get_row(seq):
    """
    Takes in a character sequence of F/B's of length 7
    Converts to binary where F = 0, B = 1 then to decimal
    """
    bin = ''
    for char in seq:
        if char == 'F':
            bin += '0'
        elif char == 'B':
            bin += '1'
    return int(bin, 2)

def get_row_or_column(seq, upper, lower):
    """
    Takes in a character sequence of L/R's of length 3
    Converts to binary where L = 0, R = 1 then to decimal
    """
    bin = ''
    for char in seq:
        if char == lower:
            bin += '0'
        elif char == upper:
            bin += '1'
    return int(bin, 2)
    
if __name__ == '__main__':
    main()
