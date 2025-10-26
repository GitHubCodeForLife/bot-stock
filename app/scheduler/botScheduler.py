from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os 
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
class BotScheduler:
    def __init__(self):
        self.init()

    def init(self):
        executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
        }
        self.scheduler = BackgroundScheduler(executors = executors)

    def reload_jobs_from_db(self):
        # 1. stop all existing jobs
        self.scheduler.remove_all_jobs()

        # 2. Load jobs from database
        from app.model.jobSchedulerRepo import query_all_jobs
        jobs = query_all_jobs()

        for job in jobs:
            # 3. Check file is source save it into scheduler folder 
            if job.source_type == 'custom_source':
                self.write_to_file(job)

            if job.trigger == "interval": 
                self.scheduler.add_job(
                    func=job.job_func,
                    name=job.job_func, 
                    trigger=job.trigger,
                    seconds=job.job_interval,
                    id=job.job_id,
                    replace_existing=True, 
                    args=[job.job_data] if job.job_data else [], 
                    misfire_grace_time = job.misfire_grace_time if job.misfire_grace_time else None, 
                    max_instances = job.max_instances, 
                    coalesce = job.coalesce 
                )
            elif job.trigger == 'cron': 
               cron_trigger_instance = CronTrigger.from_crontab(job.cron_expression)
               self.scheduler.add_job( 
                    func=job.job_func,
                    name=job.job_func,
                    trigger=cron_trigger_instance,
                    seconds=job.job_interval,
                    id=job.job_id,
                    replace_existing=True, 
                    args=[job.job_data] if job.job_data else [], 
                    misfire_grace_time = job.misfire_grace_time if job.misfire_grace_time else None, 
                    max_instances = job.max_instances, 
                    coalesce = job.coalesce
                )
            else: 
                print("Do not support trigger {job.trigger}")
         
            print(f"Loaded job {job.job_id} from database")
    
    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()
            print("bot sceduler has been started")   
    
    def add_listener(self, listener):
        self.scheduler.add_listener(listener)

    def write_to_file(self, job):
        if not job.source_code:
            print(f"⚠️ No file data for job {job.id}")
            return 
        SCHEDULER_FOLDER = "./app/scheduler"

        filename = f"{job.job_id}.py"
        file_path = os.path.join(SCHEDULER_FOLDER, filename)
         # Save file to disk
        try:
            with open(file_path, 'wb') as f:
                f.write(job.source_code)
            print(f"✅ Saved file for job {job.job_id} -> {file_path}")
        except Exception as e:
            print(f"❌ Error saving file for job {job.id}: {e}")