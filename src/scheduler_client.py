from .resource_client import Resource
from .task_client import Task
import threading, time, random

class Scheduler:
    def __init__(self, num_resources, num_projects):
        self.tasks = [Task(project=f"Project {i}") for i in range(1, num_projects+1)]
        self.resources = [Resource(i) for i in range(1, num_resources+1)]
        self.lock = threading.Lock()
    
    def assign_task_to_resource(self):
        while True:
            task = self.get_next_task()
            if task is not None:
                self.lock.acquire()
                resource = self.get_next_available_resource()
                if resource is not None:
                    threading.Thread(target=resource.assign_task, args=(task,)).start()
                else:
                    self.tasks.append(task)
                self.lock.release()
            time.sleep(random.randint(1, 3))
    
    def get_next_task(self):
        if len(self.tasks) > 0:
            return self.tasks.pop(0)
        else:
            return None
    
    def get_next_available_resource(self):
        for resource in self.resources:
            if not resource.is_busy():
                return resource
        return None

    def all_tasks_completed(self):
        return len(self.tasks)