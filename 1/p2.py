SUM_TO = 2020

f = open('input.txt', 'r')
numbers = f.read().split()
numbers = [int(n) for n in numbers] # Convert strings to integers

result = 0

min_number = min(numbers)

# Remove numbers that are too big
for n in numbers:
    if n > SUM_TO - min_number:
        numbers.remove(n)

results = []
cont = True

while(cont):
    n0 = numbers.pop(0)
    for n in numbers:
        third_num = SUM_TO - n0 - n
        if third_num in numbers[1:]:
            results = [n0, n, third_num]
            cont = False
            break
    
print(results[0] * results[1] * results[2])
