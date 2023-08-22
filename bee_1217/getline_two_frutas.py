cases = int(input()) 
list_values = []
list_fruits = []
while cases > 0:
    cases -= 1
    value = float(input())
    fruits = input().strip().split(' ')
    list_values.append(value)
    list_fruits.append(fruits)
amount = 0
for day, kg in enumerate (list_fruits, start = 1):
    amount += len(kg)
    print('day {}: {} kg'.format(day, len(kg)))
print('{:.2f} kg by day'.format(amount / len(list_fruits)))
print('R$ {:.2f} by day'.format(sum(list_values) / len(list_values)))
