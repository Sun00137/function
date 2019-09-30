import math 
# Function to calculate distance 
def distance(x1 , y1 , x2 , y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
    return distance
distance(1,1,2,2)