SUM_TO = 2020

f = open('input.txt', 'r')
numbers = f.read().split()
numbers = [int(n) for n in numbers] # Convert strings to integers

result = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            if n1 + n2 == SUM_TO:
                result = n1 * n2
                break
                
print(result)
