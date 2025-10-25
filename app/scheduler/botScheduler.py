from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import os 
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
class BotScheduler:
    def __init__(self):
        jobstores = {
            'default': SQLAlchemyJobStore(url=os.getenv('SQLALCHEMY_DATABASE_URI'))
        }
        executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }
        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors = executors, job_defaults = job_defaults)

    def reload_jobs_from_db(self):
        # 1. Shutdonw scheduler if running
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)

        # 2. stop all existing jobs
        self.scheduler.remove_all_jobs()

        # 3. Load jobs from database
        from app.model.jobSchedulerRepo import query_all_jobs
        jobs = query_all_jobs()
        from app.scheduler.schedulerTask import mapJobFunction

        for job in jobs:
            if job.trigger == "interval": 
                self.scheduler.add_job(
                    func=mapJobFunction.get(job.job_func),
                    trigger=job.trigger,
                    seconds=job.job_interval,
                    id=job.job_id,
                    replace_existing=True, 
                    args=[job.job_data] if job.job_data else []
                )
            elif job.trigger == 'cron': 
               cron_trigger_instance = CronTrigger.from_crontab(job.cron_expression)
               self.scheduler.add_job( func=mapJobFunction.get(job.job_func),
                    trigger=cron_trigger_instance,
                    seconds=job.job_interval,
                    id=job.job_id,
                    replace_existing=True, 
                    args=[job.job_data] if job.job_data else []
                )
            else: 
                print("Do not support trigger {job.trigger}")
         
            print(f"Loaded job {job.job_id} from database")
        
    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()   
    
    def add_listener(self, listener):
        self.scheduler.add_listener(listener)