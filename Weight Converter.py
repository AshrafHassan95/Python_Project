weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    conversion = weight / 2.205
    print(f"Your weight is {conversion} kg")
else:
    conversion = weight * 2.205
    print(f"Your weight is {conversion} lbs")