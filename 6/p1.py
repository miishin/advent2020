from string import ascii_lowercase
def main():
    f = open('input.txt', 'r')
    groups = f.read().split('\n\n')
    sum = 0
    for group in groups:
        sum += count(group)
    print(sum)

def count(group):
    """
    Count the # of unique letters in the given lines
    """
    flattened = group.replace('\n', '')
    count = 0
    for letter in ascii_lowercase:
        if letter in flattened:
            count += 1
    return count
    
if __name__ == '__main__':
    main()
