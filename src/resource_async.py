import asyncio,random 

class Resource:
    def __init__(self, id):
        self.id = id
        self.busy = False
    
    def is_busy(self):
        return self.busy
    
    async def assign_task(self, task):
        self.busy = True
        task.assigned_to_resource = True
        print(f"Resource {self.id} is working on Task {task}")
        await asyncio.sleep(random.randint(2, 5))
        print(f"Resource {self.id} finished Task {task}")
        self.busy = False
        self.assigned_to_resource = False