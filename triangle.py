'''
The task is to calculate the field of a triangle, which corners are provided
as cartesian coordinates

The most basic formula used to calculate the triangle's field is:
a = (height * base) / 2

Obstacles to tackle with that approach:

I.      Verify if the base and the height are positioned
        horizontally/vertically on the grid

II.     If they aren't, the point from which the height stems from
        needs to be located

III.    Finding the length of a line:
            1. pick two coordinates
            2. get x by substracting the first set of coordinates into
                an absolute
            3. do the same with y
            4. add both these values after having them squared,
                then root the sum

IV.     In order to ensure the height is always inside the triangle:
        Pick the longest line as a base


Given the difficulties with locating the stem of the height, the area could be
calculated with Heron's formula instead:

A = 0.25 * (((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))**(.5))

'''

# the project

'''
1. get the coordinates
2. calculate each length
3. get the area with heron's formula
'''
coordinates = []
lengths = []
area = 0
def getCoordinates():
    global coordinates
    for p in range(3):
        coordinates.append([])
        coordinates[p].append(int(input("""Please provide the X coordinate for \
the point number %s: """ % (p+1))))
        coordinates[p].append(int(input("""Please provide the Y coordinate for \
the point number %s: """ % (p+1))))
        print()
    print("The coordinates you've provided are the following: %s\n" % coordinates)

def getLength():
    global lengths
    for l in range(len(coordinates)):
        if l+1 in range(len(coordinates)):
            lengths.append(((abs(coordinates[l][0] - \
            coordinates[l+1][0]) ** 2) + \
            (abs(coordinates[l][1] - coordinates[l+1][1]) ** 2)) ** (.5))
        else:
            lengths.append(((abs(coordinates[l][0] - \
            coordinates[l+1-len(coordinates)][0]) ** 2) + \
            (abs(coordinates[l][1] - coordinates[l+1-len(coordinates)][1]) ** 2)) ** (.5))

def formula():
    global area
    area = 0.25 * (((lengths[0] + lengths[1] + lengths[2]) *
    ((-1*lengths[0]) + lengths[1] + lengths[2]) *
    (lengths[0] - lengths[1] + lengths[2]) *
    (lengths[0] + lengths[1] - lengths[2]))**(.5))
    print ("The area of that triangle is %s. %s, to be exact.\n" % (int(area), area))

while True:
    getCoordinates()
    getLength()
    formula()
    choice = input("Do you want to check the area of another triangle? y/n: \n")
    if choice in "y":
        coordinates = []
        lengths = []
        area = 0
    else:
        break
