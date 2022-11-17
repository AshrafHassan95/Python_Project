numbers = [5, 2, 5, 2, 5]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

for x in range(5):
    for y in range(4):
        print(f"({x}),({y})")
