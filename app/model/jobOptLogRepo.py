from app.shareData import ShareData
from app.model.models import db
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class JobOptLog(db.Model):
    log_id : Mapped[int] = mapped_column(primary_key=True)
    job_func : Mapped[str] = mapped_column()
    job_status : Mapped[str] = mapped_column()
    job_time : Mapped[str] = mapped_column()
    job_message : Mapped[str] = mapped_column()

def add_job_opt_log(job_func, job_status, job_time, job_message):
    with ShareData.app.app_context():
        log = JobOptLog(
            job_func=job_func,
            job_status=job_status,
            job_time=job_time,
            job_message=job_message
        )
        db.session.add(log)
        db.session.commit()