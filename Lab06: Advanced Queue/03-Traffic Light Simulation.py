import random

class Vehicle:
    def __init__(self, id, arrival):
        self.id = id
        self.arrival = arrival

class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_length = 0

    def enqueue(self, vehicle):
        if self.size < len(self.queue):
            self.queue[self.rear] = vehicle
            self.rear = (self.rear + 1) % len(self.queue)
            self.size += 1
            if self.size > self.max_length:
                self.max_length = self.size

    def dequeue(self):
        if self.size == 0:
            return None
        v = self.queue[self.front]
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        return v

    def is_empty(self):
        return self.size == 0

def simulation():
    ns = CircularQueue(5)  
    ew = CircularQueue(5)  
    direction = "NS"
    cycles = 20
    total_wait = 0
    vehicles_passed = 0
    vehicle_id = 1

    for time in range(cycles):
        if random.random() < 0.5:
            ns.enqueue(Vehicle(vehicle_id, time))
            vehicle_id += 1
        if random.random() < 0.5:
            ew.enqueue(Vehicle(vehicle_id, time))
            vehicle_id += 1

        if direction == "NS":
            vehicle = ns.dequeue()
        else:
            vehicle = ew.dequeue()

        if vehicle:
            total_wait += time - vehicle.arrival
            vehicles_passed += 1

        direction = "EW" if direction == "NS" else "NS"

    print("Simulation completed")
    if vehicles_passed > 0:
        print("Average wait time:", total_wait / vehicles_passed)
    else:
        print("No vehicles passed")
    print("Maximum queue length NS:", ns.max_length)
    print("Maximum queue length EW:", ew.max_length)

simulation()
