class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        return "Car with the maximum speed of {} {}".format(self.max_speed, self.unit)

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return "Boat with the maximum speed of {} knots".format(self.max_speed)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    q = int(data[0])
    queries = data[1:]
    
    for query in queries:
        parts = query.split()
        vehicle_type = parts[0]
        
        if vehicle_type == 'car':
            max_speed = int(parts[1])
            unit = parts[2]
            car = Car(max_speed, unit)
            print(car)
        
        elif vehicle_type == 'boat':
            max_speed = int(parts[1])
            boat = Boat(max_speed)
            print(boat)

if __name__ == "__main__":
    main()
