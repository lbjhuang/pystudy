#分割
number = '6 5 6 5 8'
total = 0
for i in number.split(' '):
    total += int(i)

print(total)
