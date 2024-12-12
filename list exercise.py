single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
cubes = []

for num in single_digits:
    for digit in str(num):
        print(num)
    squares.append(num**2)
    cubes.append(num**3)
    print(squares)        
    print(cubes)        
