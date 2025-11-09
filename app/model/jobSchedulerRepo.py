from app.shareData import ShareData
from app.model.models import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, create_engine, Boolean, LargeBinary

class JobScheduler(db.Model):
    job_id : Mapped[str] = mapped_column(String(255), primary_key=True)
    job_func : Mapped[str] = mapped_column(String(255))
    job_data : Mapped[str] = mapped_column(String(255))
    job_interval : Mapped[int] = mapped_column(Integer)  # in seconds
    trigger : Mapped[str] = mapped_column(String(255))
    cron_expression: Mapped[str] = mapped_column(String(255))
    create_time : Mapped[str] = mapped_column(String(255))
    misfire_grace_time : Mapped[int] = mapped_column(Integer)
    max_instances : Mapped[int] = mapped_column(Integer)
    coalesce : Mapped[bool] = mapped_column(Boolean)
    source_type: Mapped[str] = mapped_column(String(255))
    source_code: Mapped[bytes] = mapped_column(LargeBinary)  
    is_active : Mapped[bool] = mapped_column(Boolean)

def query_all_jobs():
    with ShareData.app.app_context():
        return JobScheduler.query.all()