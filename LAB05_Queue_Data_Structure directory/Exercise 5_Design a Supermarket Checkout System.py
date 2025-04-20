from collections import deque

class Customer:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = items
        self.wait_time = 0

class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate
        self.queue = deque()
        self.current_customer = None
        self.remaining_items = 0
        self.customers_served = 0

    def add_customer(self, customer):
        self.queue.append(customer)

    def process(self):
        if not self.current_customer and self.queue:
            self.current_customer = self.queue.popleft()
            self.remaining_items = self.current_customer.items

        if self.current_customer:
            self.remaining_items -= self.processing_rate
            if self.remaining_items <= 0:
                print(f"✅ Customer {self.current_customer.customer_id} finished at Lane {self.lane_id}")
                self.customers_served += 1
                self.current_customer = None

class Supermarket:
    def __init__(self, num_lanes, processing_rates):
        self.lanes = [CheckoutLane(i + 1, rate) for i, rate in enumerate(processing_rates)]
        self.time = 0
        self.wait_times = {}

    def arrive_customer(self, customer):
        shortest_lane = min(self.lanes, key=lambda lane: len(lane.queue))
        shortest_lane.add_customer(customer)
        self.wait_times[customer.customer_id] = 0
        print(f"🛒 Customer {customer.customer_id} with {customer.items} items joined Lane {shortest_lane.lane_id}")

    def simulate(self, total_time):
        for _ in range(total_time):
            print(f"\n🕒 Time: {self.time}")
            for lane in self.lanes:
                for customer in lane.queue:
                    self.wait_times[customer.customer_id] += 1
                lane.process()
            self.time += 1

    def get_stats(self):
        total_wait = sum(self.wait_times.values())
        total_customers = sum(lane.customers_served for lane in self.lanes)
        avg_wait = total_wait / total_customers if total_customers > 0 else 0
        return {
            "average_wait_time": avg_wait,
            "total_customers_served": total_customers
        }

#test
market = Supermarket(2, [1, 2]) 
market.arrive_customer(Customer(1, 5))
market.arrive_customer(Customer(2, 3))
market.arrive_customer(Customer(3, 4))
market.simulate(10)
print(market.get_stats())


market = Supermarket(3, [1, 1, 3])
market.arrive_customer(Customer(1, 6))
market.arrive_customer(Customer(2, 5))
market.arrive_customer(Customer(3, 2))
market.arrive_customer(Customer(4, 1))
market.simulate(8)
print(market.get_stats())


market = Supermarket(1, [2])
market.arrive_customer(Customer(1, 10))
market.arrive_customer(Customer(2, 5))
market.simulate(15)
print(market.get_stats())
