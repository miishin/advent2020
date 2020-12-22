RISE = 1
RUN = 3

def main():
    f = open('input.txt', 'r')
    global rows
    rows = f.read().split('\n')
    global height
    height = len(rows)
    global width
    width = len(rows[0])
    print(travel(0, 0, 0))

    
def travel(x, y, trees):
    """
    Travels along the map defined by the given section
    Returns the number of trees hit if traveling along
    slope rise/run (positive rise = downwards)
    x, y is the current position
    trees is the number of trees hit so far
    """
    if y >= height - 1:
        return trees
    if x > width - 1:
        x = x % width
    if rows[y][x] == '#':
        trees += 1
    return travel(x + RUN, y + RISE, trees)
    
if __name__ == '__main__':
    height = 0
    width = 0
    rows = None
    main()

