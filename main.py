from src.scheduler_client import Scheduler
import threading, random, time

def main():
    scheduler = Scheduler(num_resources=3, num_projects=5)
    threading.Thread(target=scheduler.assign_task_to_resource).start()

    while True:
        scheduler.lock.acquire()
        if scheduler.is_all_tasks_completed():
            scheduler.mark_all_tasks_completed()
            scheduler.lock.release()
            break
        scheduler.lock.release()
        time.sleep(random.randint(1, 5))


if __name__ == "__main__":
    main()