# WAP to find the nearest point to the origin from N points given by the user.

num = int(input("Enter the number of the point :"))
points = []

for i in range(num):
    x = int(input("Enter the x coordinate of the point :"))
    y = int(input("Enter the y coordinate of the point :"))
    points.append((x,y))
    print(points)
    def distance(x,y):
        return (x**2 + y**2)**0.5
    min_distance = min(distance(x,y) for x,y in points)
    print(f"The nearest point to the origin is {min_distance}")
    nearestpoint = points[points.index((x,y))]
    print(f"The nearest point to the origin is {nearestpoint}")