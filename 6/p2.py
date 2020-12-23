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
    Count the number of times all members in a group answered
    "yes" for the same question.
    Converts to sets then finds intersection.
    """
    people = group.split('\n')
    sets = []
    for p in people:
        if p:
            sets.append(set(p))
    count = 0
    shared_answers = set.intersection(*sets)
    return len(shared_answers)

if __name__ == '__main__':
    main()
