from apscheduler.schedulers.background import BackgroundScheduler

class BotScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def reload_jobs_from_db(self):
        # 1. Shutdonw scheduler if running
        if self.scheduler.running:
            self.scheduler.shutdown()

        # 2. stop all existing jobs
        self.scheduler.remove_all_jobs()

        # 3. Load jobs from database
        from app.model.jobSchedulerRepo import query_all_jobs
        jobs = query_all_jobs()
        from app.scheduler.schedulerTask import mapJobFunction

        for job in jobs:
            self.scheduler.add_job(
                func=mapJobFunction.get(job.job_func),
                trigger='interval',
                seconds=job.job_interval,
                id=job.job_id,
                replace_existing=False, 
                args=[job.job_data] if job.job_data else []
            )
            print(f"Loaded job {job.job_id} from database")
        
    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()   
    
    def add_listener(self, listener):
        self.scheduler.add_listener(listener)