centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f'{round(centuries)} centuries = {round(years)} years = {round(days)} days = {round(hours)} hours = {round(minutes)} minutes')