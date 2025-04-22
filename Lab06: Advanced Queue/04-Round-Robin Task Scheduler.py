# Round-Robin Task Scheduler

class Process:
    def __init__(self, name, burst_time, arrival_time=0):
        self.name = name
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.finish_time = 0
        self.waiting_time = 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

def round_robin_scheduler(processes, quantum):
    queue = Queue()
    for p in processes:
        queue.enqueue(p)

    current_time = 0
    completed = []

    while not queue.is_empty():
        current_process = queue.dequeue()

        if current_process.remaining_time > quantum:
            current_process.remaining_time -= quantum
            current_time += quantum
            for i in range(len(queue.items)):
                queue.items[i].waiting_time += quantum
            queue.enqueue(current_process)
        else:
            current_time += current_process.remaining_time
            current_process.waiting_time += current_time - current_process.arrival_time - (current_process.finish_time - current_process.remaining_time)
            current_process.finish_time = current_time
            current_process.remaining_time = 0
            completed.append(current_process)

    print("\n[Round-Robin Results]")
    for p in completed:
        turnaround = p.finish_time - p.arrival_time
        print(f"{p.name} -> Waiting Time: {p.waiting_time}, Turnaround Time: {turnaround}")

def main():
    print("=== Round-Robin Scheduler ===")
    processes = [
        Process("P1", 10),
        Process("P2", 5),
        Process("P3", 8)
    ]
    quantum = 3
    round_robin_scheduler(processes, quantum)

if __name__ == "__main__":
    main()

# Test Case 1: Standard test case with a variety of burst times
print("Test Case 1: Standard Test Case")
processes = [
    Process("P1", 10),  # Process P1 with burst time of 10
    Process("P2", 5),   # Process P2 with burst time of 5
    Process("P3", 8)    # Process P3 with burst time of 8
]
quantum = 3
round_robin_scheduler(processes, quantum)

# Test Case 2: Process with zero burst time (edge case)
print("\nTest Case 2: Zero Burst Time")
processes = [
    Process("P1", 0),  # Process P1 with burst time of 0
    Process("P2", 5),  # Process P2 with burst time of 5
    Process("P3", 8)   # Process P3 with burst time of 8
]
quantum = 3
round_robin_scheduler(processes, quantum)

# Test Case 3: Process with burst time equal to the quantum
print("\nTest Case 3: Burst Time Equal to Quantum")
processes = [
    Process("P1", 3),  # Process P1 with burst time equal to quantum
    Process("P2", 3),  # Process P2 with burst time equal to quantum
    Process("P3", 3)   # Process P3 with burst time equal to quantum
]
quantum = 3
round_robin_scheduler(processes, quantum)
