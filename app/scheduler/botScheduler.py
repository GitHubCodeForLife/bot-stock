from app.model.models import JobScheduler, JobOptLog
from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduler.schedulerTask import mapJobFunction
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

def job_listener(event):
    print(f"Job {event.job_id} event received: {event.exception}")
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')
    if event.exception:
        log = JobOptLog(
            job_id=event.job_id,
            job_status="FAILED",
            job_message =f"Job {event.job_id} failed with exception: {event.exception}"
        )
    else:
        log = JobOptLog(
            job_id=event.job_id,
            job_status="SUCCESS",
            job_message =f"Job {event.job_id} executed successfully."
        )
    log.save()

class BotScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def reload_jobs_from_db(self):
        # 1. Shutdonw scheduler if running
        if self.scheduler.running:
            self.scheduler.stop()

        # 2. stop all existing jobs
        self.scheduler.remove_all_jobs()

        # 3. Load jobs from database
        jobs = JobScheduler.query.all()
        for job in jobs:
            self.scheduler.add_job(
                func=mapJobFunction.get(job.job_func),
                trigger='interval',
                seconds=job.job_interval,
                id=job.job_id,
                replace_existing=True, 
                args=[job.job_data] if job.job_data else []
            )
            print(f"Loaded job {job.job_id} from database")
        
    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()   
    
    def add_listener(self, listener, event_mask):
        self.scheduler.add_listener(listener, event_mask)