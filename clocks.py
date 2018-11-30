
import matplotlib
n = int(input())
global hr, min
hradd = n // 60
minadd = n % 60
if hradd > 23:
    if hradd == 24:
        hr = 0
    else: hr = int(hradd % 24)
else:
    hr = hradd

print("Сейчас ", hr, " часов ", minadd , " минут")
print()