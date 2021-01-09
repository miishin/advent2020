def find_sum(n, nlist):
    for i in range(len(nlist) - 1):
        for j in range(i + 1, len(nlist)):
            if nlist[i] + nlist[j] == n:
                return True
    return False

f = open('input.txt', 'r')
numbers = f.read().split('\n')[:-1]
numbers = [int(n) for n in numbers]
trailing_buffer = numbers[:25]
for i in range(25, len(numbers)):
    if not find_sum(numbers[i], trailing_buffer):
        print(numbers[i])
        break
    trailing_buffer.pop(0)
    trailing_buffer.append(numbers[i])
