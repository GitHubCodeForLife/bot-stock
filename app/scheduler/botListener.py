from apscheduler.events import SchedulerEvent,  JobSubmissionEvent, JobExecutionEvent, JobEvent
from app.model.jobOptLogRepo import add_job_opt_log, JobOptLog
from app.shareData import ShareData
def job_listener(event: JobEvent):
    print(event)
    # check event type
    job :JobOptLog = JobOptLog()
    if isinstance(event, JobExecutionEvent):
        job.job_func = event.job_id
        job.job_status = "SUCCESS" if event.exception is None else "FAILED"
        job.job_time = str(event.scheduled_run_time)
        job.job_message = str(event.retval) if event.exception is None else str(event.exception)
    elif isinstance(event, JobSubmissionEvent):
        job.job_func = event.job_id
        job.job_status = "SUBMITTED"
        job.job_time = str(event.scheduled_run_times)
        job.job_message = "Job has been submitted"
    elif isinstance(event, SchedulerEvent):
        print("Do nothing for SchedulerEvent")
        return 
    else:
        job.job_func = event.job_id
        job.job_status = "UNKNOWN"
        job.job_time = "N/A"
        job.job_message = "Unknown event type"
    # save to db
    # print(job.job_func, job.job_status, job.job_time, job.job_message)
    add_job_opt_log(job.job_func, job.job_status, job.job_time, job.job_message)