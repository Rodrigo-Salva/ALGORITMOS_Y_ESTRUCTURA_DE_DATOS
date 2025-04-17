class Task:
    def __init__(self, name, duration, priority=0):
        self.name = name
        self.duration = duration
        self.remaining_time = duration
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

def round_robin_scheduler(tasks, quantum):
    time = 0
    queue = tasks.copy()
    completed_tasks = []

    while queue:
        task = queue.pop(0)

        if task.remaining_time > quantum:
            time += quantum
            task.remaining_time -= quantum
            queue.append(task)
        else:
            time += task.remaining_time
            task.waiting_time = time - task.duration
            task.turnaround_time = time
            task.completion_time = time
            task.remaining_time = 0
            completed_tasks.append(task)

    return completed_tasks

def show_results(completed_tasks):
    total_waiting = 0
    total_turnaround = 0

    print("\nResults per task:")
    for task in completed_tasks:
        print(f"Task {task.name} -> Waiting Time: {task.waiting_time}, Turnaround Time: {task.turnaround_time}")
        total_waiting += task.waiting_time
        total_turnaround += task.turnaround_time

    n = len(completed_tasks)
    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")

if __name__ == "__main__":
    tasks = [
        Task("A", 5),
        Task("B", 8),
        Task("C", 6)
    ]
    quantum = 3

    completed = round_robin_scheduler(tasks, quantum)
    show_results(completed)
