from .resource_client import Resource
from .task_client import Task
import threading, time, random, sys

class Scheduler:
    def __init__(self, num_resources, num_projects):
        self.tasks = [Task(project=f"Project {i}", priority=i) for i in range(1, num_projects+1)]
        self.resources = [Resource(i) for i in range(1, num_resources+1)]
        self.lock = threading.Lock()
        self.all_tasks_completed = False

    
    def assign_task_to_resource(self):
        while not self.all_tasks_completed:
            task = self.get_next_task()
            if task is not None:
                self.lock.acquire()
                resource = self.get_next_available_resource()
                if resource is not None:
                    threading.Thread(target=resource.assign_task, args=(task,)).start()
                self.lock.release()
            time.sleep(random.randint(1, 3))
    
    def get_next_task(self):
        if len(self.tasks) > 0:
            highest_priority_task = max(self.tasks, key=lambda task: task.priority)
            self.tasks.remove(highest_priority_task)
            return highest_priority_task
        else:
            return None
    
    def get_next_available_resource(self):
        for resource in self.resources:
            if not resource.is_busy():
                return resource
        return None
    
    def mark_all_tasks_completed(self):
        self.all_tasks_completed = True
    
    def is_all_tasks_completed(self):
        return len(self.tasks) == 0 and all([not resource.is_busy() for resource in self.resources])