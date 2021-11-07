#Rectangle:
set_width = int(input('Width of Rectangle:'))
set_height = int(input('Height of rectangle:'))
print("Rectangle width:", set_width)
print("Rectangle height:", set_height)
get_area = set_width*set_height
print("Area of rectangle is:", get_area)
get_perimeter = 2 * set_width + 2 * set_height
print("Perimeter of rectangle is:", get_perimeter)
get_diagonal =  ((set_width ** 2 + set_height ** 2) ** .5)
print("Diagonal of Rectangle is:", get_diagonal)
for i in range(set_height):
    for j in range(set_width):
        print('*', end = '  ')
    print()

#Square:
side_length = int(input('Length of Square:'))
print("Length of square:", side_length)
get_area = side_length^2
print("Area of square is:", get_area)
get_perimeter = 4 * side_length
print("Perimeter of rectangle is:", get_perimeter)
get_diagonal =  ((side_length ** 2 + side_length ** 2) ** .5)
print("Diagonal of square is:", get_diagonal)
for k in range(side_length):
    for l in range(side_length):
        print('*', end = '  ')
    print()
