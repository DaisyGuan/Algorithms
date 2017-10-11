# Complete the function below.
import math
def  closestColor(pixels):
    def distance(c1,c2):
        (r1,g1,b1) = c1
        (r2,g2,b2) = c2
        return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

    r = int(str(pixels)[0:8],2)
    g = int(str(pixels)[8:16],2)
    b = int(str(pixels)[16:24],2)
    Origin = (r,g,b)
    color_dict = {"Black":(0,0,0),"White":(255,255,255), "Red": (255,0,0), "Green":(0,255,0), "Blue":(0,0,255)}
    #print color_dict.items()
    buff_dict = {}
    for key,value in color_dict.iteritems():
        buff_dict[key] = distance(Origin, value)
    result = min(buff_dict.items(), key = lambda x: x[1])[0]
    return result

print closestColor(101010111011111011101101)
