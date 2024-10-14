from math import floor
eggs = int(input("# of Eggs: "))
dozens = floor(eggs / 12)
remainder = eggs % 12
price = 0.0
tcost = 0.0
if dozens > 0 and dozens <= 4:
	price = 0.50
elif dozens > 4 and dozens <= 6:
	price = 0.45
elif dozens > 6 and dozens <= 11:
	price = 0.40
elif dozens > 11:
	price = 0.35
else:
	print("! Invalid # of Dozens !")
	

tcost = (dozens * price) + (remainder * ((1.0 / 12) * price))

print("Total Cost: $%.2f") % tcost

input()