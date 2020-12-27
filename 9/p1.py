ACTIVE = '#'
INACTIVE = '.'
def main():
    f = open('input.txt', 'r')
    initial_slice = f.read().split('\n')[:-1]
    print(get_active_cubes(initial_slice))

def convert_slice_to_3d(initial_slice):
    """
    Takes in the 2d slice of the entire cube and returns
    that slice as a list of 3d positions
    """
    row_length = len(initial_slice[0])
    col_length = len(initial_slice)
    cubes = [[[0] for j in range(col_length)] for i in range(row_length)]
    for i in range(row_length):
        for j in range(col_length):
            if initial_slice[i][j] == ACTIVE:
                cubes[i][j][0] = 1
    return cubes

def get_active_cubes(initial_slice):
    active_positions = []
    for i in range(len(initial_slice[0])):
        for j in range(len(initial_slice)):
            if initial_slice[i][j] == ACTIVE:
                active_positions.append((i, j, 0))
    return active_positions

def get_neighbors(x, y, z):
    # Returns the neighbors of the given 3d coordinate
    # Neighbors are at most 1 unit away in each dimension
    # Imagine a 3x3x3 cube centered on the given coordinate.
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                neighbors.append((x + i, y + j, z + k))
    neighbors.remove((x, y, z))
    return neighbors
    
if __name__ == '__main__':
    main()
