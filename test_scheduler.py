from src.resource_client import Resource
from src.scheduler_client import Scheduler
from src.task_client import Task
import time, threading

def test_scheduler():
    scheduler = Scheduler(num_resources=2, num_projects=3)
    threading.Thread(target=scheduler.assign_task_to_resource, daemon=True).start()
    
    time.sleep(1)
    assert len(scheduler.tasks) == 2
    
    time.sleep(7)
    assert len(scheduler.tasks) == 0
    

def test_task_repr():
    task = Task("Test project")
    assert str(task) == "Test project"

def test_task_assigned_to_resource():
    task = Task("Test project")
    assert not task.assigned_to_resource

    # Assign the task to a resource
    resource = Resource(1)
    resource.assign_task(task)

    # Verify that the task is now assigned to a resource
    assert task.assigned_to_resource