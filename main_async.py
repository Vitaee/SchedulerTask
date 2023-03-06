from src.scheduler_async import Scheduler
import asyncio, random, time

async def main():
    scheduler = Scheduler(num_resources=3, num_projects=5)
    await scheduler.assign_task_to_resource()

if __name__ == "__main__":
    asyncio.run(main())