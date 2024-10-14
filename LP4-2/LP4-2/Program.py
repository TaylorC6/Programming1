Kilograms = int(input("Package Weight in Kilograms: "))
Length = int(input("Package Length in Centimeters: "))
Width = int(input("Package Width in Centimeters: "))
Height = int(input("Package Height in Centimeters: "))
heavy = 0.0
large = 0.0
if Kilograms > 27:
	heavy = 1
if (Height * Length * Width) > 100000:
	large = 1
if heavy == 1 and large == 0:
	print("Too Heavy.")
elif heavy == 0 and large == 1:
	print("Too Large.")
elif heavy == 1 and large == 1:
	print("Too Heavy and Too Large.")
else:
	print("OK")

input()