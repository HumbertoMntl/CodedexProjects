import math
print('==================')
print('AREA CALCULATOR')
print('==================')
fig = 0
while fig != 5:
    fig = int(input('Which shape: '))
    if fig == 1:
        print('Option selected : Triangle')
        baseTriangle = int(input('Base: '))
        heightTriangle = int(input('Height: '))
        areaTriangle = (baseTriangle*heightTriangle)/2
        print (areaTriangle)
    elif fig == 2:
        print('Option selected : Rectangle')
        lengthRectangle = int(input('Length: '))
        widthRectangle = int(input('Width: '))
        areaRectangle = lengthRectangle*widthRectangle
        print (areaRectangle)
    elif fig == 3:
        print('Option selected : Square')
        sideSquare = int(input('Side: '))
        areaSquare = sideSquare**2
        print (areaSquare)
    elif fig == 4:
        print('Option selected : Circle')
        radiusCircle = int(input('Radius: '))
        areaCircle = math.pi*radiusCircle**2
        print (areaCircle)
    else:
        print('Please select a valid option')
if fig == 5:
    print('Option selected : Quit')
    print ('Thanks for using this calculator')
    SystemExit