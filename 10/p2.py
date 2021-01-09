invalid_number = 22406676

f = open('input.txt', 'r')
numbers = f.read().split('\n')[:-1]
numbers = [int(n) for n in numbers]

def find_solution():
    for i in range(len(numbers)):
        sum_so_far = numbers[i]
        numbers_so_far = [numbers[i]]
        for j in range(i + 1, len(numbers)):
            if sum_so_far == invalid_number:
                return numbers_so_far
            sum_so_far += numbers[j]
            numbers_so_far.append(numbers[j])

x = find_solution()
x.sort()
print(x[0] + x[-1])
