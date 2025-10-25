from app.shareData import ShareData
from app.model.models import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, create_engine

class JobScheduler(db.Model):
    job_id : Mapped[str] = mapped_column(String(255), primary_key=True)
    job_func : Mapped[str] = mapped_column(String(255))
    job_data : Mapped[str] = mapped_column(String(255))
    job_interval : Mapped[int] = mapped_column(Integer)  # in seconds
    trigger : Mapped[str] = mapped_column(String(255))
    cron_expression: Mapped[str] = mapped_column(String(255))
    create_time : Mapped[str] = mapped_column(String(255))

def query_all_jobs():
    with ShareData.app.app_context():
        return JobScheduler.query.all()