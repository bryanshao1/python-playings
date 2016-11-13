import math

def polysum( n, s ):
    perimeter = n * s
    area = (0.25 * perimeter * s)/(math.tan(math.pi/n))
    return round((perimeter**2 + area), 4)