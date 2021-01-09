ACTIVE = '#'
INACTIVE = '.'
def main():
    f = open('input.txt', 'r')
    initial_slice = f.read().split('\n')[:-1]
    cubes = get_cubes(initial_slice)
    active_cubes = cubes[0]
    inactive_cubes = cubes[1]
    for i in range(6):
        print('cycle ' + str(i))
        cubes = run_cycle(active_cubes, inactive_cubes)
        active_cubes = filter_cubes(cubes[0])
        inactive_cubes = filter_cubes(cubes[1])
    print(len(active_cubes))

def run_cycle(active_cubes, inactive_cubes):
    """
    Given a list of 3d positions of the active cubes and inactive cubes,
    runs one cycle.
    If a cube is active it becomes inactive unless 2/3 of its neighbors are active.
    If a cube is inactive it becomes active if 3 of its neighbors are active
    """
    updated_active_cubes = []
    updated_inactive_cubes = []
    for cube in active_cubes:
        neighbors = get_neighbors(*cube)
        count_active = 0
        for neighbor in neighbors:
            if neighbor in active_cubes:
                count_active += 1
            else:
                updated_inactive_cubes.append(neighbor)
        if count_active == 2 or count_active == 3:
            updated_active_cubes.append(cube)
        else:
            updated_inactive_cubes.append(cube)
    for cube in inactive_cubes:
        neighbors = get_neighbors(*cube)
        count_active = 0
        for neighbor in neighbors:
            if neighbor in active_cubes:
                count_active += 1
            else:
                updated_inactive_cubes.append(neighbor)
        if count_active == 3:
            updated_active_cubes.append(cube)
        else:
            updated_inactive_cubes.append(cube)
    return updated_active_cubes, updated_inactive_cubes

def filter_cubes(cubes):
    # Remove duplicates
    filtered = []
    [filtered.append(cube) for cube in cubes if cube not in filtered]
    return filtered

def get_cubes(initial_slice):
    """
    Returns two lists:
    A list of the positions of the active cubes in the initial state
    A list of the positions of the inactive cubes in the initial state
    """
    active_positions = []
    inactive_positions = []
    for i in range(len(initial_slice[0])):
        for j in range(len(initial_slice)):
            if initial_slice[i][j] == ACTIVE:
                active_positions.append((i, j, 0))
            else:
                inactive_positions.append((i, j, 0))
    return active_positions, inactive_positions

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
