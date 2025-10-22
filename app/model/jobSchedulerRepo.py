from app.shareData import ShareData
from app.model.models import db
from sqlalchemy.orm import Mapped, mapped_column

class JobScheduler(db.Model):
    job_id : Mapped[str] = mapped_column(primary_key=True)
    job_func : Mapped[str] = mapped_column()
    job_data : Mapped[str] = mapped_column()
    job_interval : Mapped[int] = mapped_column()  # in seconds
    trigger_args : Mapped[str] = mapped_column()
    create_time : Mapped[str] = mapped_column()

def query_all_jobs():
    with ShareData.app.app_context():
        return JobScheduler.query.all()