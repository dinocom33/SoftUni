x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

point_position = ""

if (x == x1) or (x == x2):
    if (y < y1) or (y < y2):
        print("Border")
    elif (y > y1) or (y > y2):
        print("Inside / Outside")
if (y == y1) or (y == y2):
#    print("Border")
    if (x < x1) or (x < x2):
        print("Inside / Outside")
    elif (x > x1) or (x > x2):
        print("Inside / Outside")
elif ((x != x1) or (x != x2)) and ((y != y1) or (y != y2)):
    print("Inside / Outside")