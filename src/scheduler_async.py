from .resource_async import Resource
from .task_client import Task
import asyncio, time, random

class Scheduler:
    def __init__(self, num_resources, num_projects):
        self.tasks = [Task(project=f"Project {i}", priority=i) for i in range(1, num_projects+1)]
        self.resources = [Resource(i) for i in range(1, num_resources+1)]
    
    async def assign_task_to_resource(self):
        while True:
            task = self.get_next_task()
            if task is not None:
                resource = await self.get_next_available_resource()
                if resource is not None:
                    asyncio.create_task(resource.assign_task(task))
                else:
                    self.tasks.append(task)
            if len(self.tasks) == 0:
                break
            await asyncio.sleep(random.randint(1, 3))
    
    def get_next_task(self):
        if len(self.tasks) > 0:
            return max(self.tasks, key=lambda x: x.priority)
        else:
            return None
    
    async def get_next_available_resource(self):
        while True:
            for resource in self.resources:
                if not resource.is_busy():
                    return resource
            await asyncio.sleep(1)

    def all_tasks_completed(self):
        return len(self.tasks)