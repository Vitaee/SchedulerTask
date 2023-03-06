import time, random

class Resource:
    def __init__(self, id):
        self.id = id
        self.busy = False
    
    def is_busy(self):
        return self.busy
    
    def assign_task(self, task):
        self.busy = True
        task.assigned_to_resource = True
        print(f"Resource {self.id} is working on Task {task}")
        time.sleep(random.randint(2, 7))
        print(f"Resource {self.id} finished Task {task}")
        self.busy = False
        self.assigned_to_resource = False