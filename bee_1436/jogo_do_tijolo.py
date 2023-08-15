amount_cases = int(input())
number_case = 0
while amount_cases > 0:
    amount_cases -= 1
    number_case += 1
    ages = list(map(int, input().strip().split(' ')))
    age_captain = ages[(ages[0] // 2) + 1]
    print('Case {}: {}'.format(number_case, age_captain))
