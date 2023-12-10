purchases = {}

with open(file='purchase_log.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        key = line.split(':')[1].split(',')[0][2:-1]
        value = line.split(':')[2][2:-3]
        purchases[key] = value

print(purchases)
