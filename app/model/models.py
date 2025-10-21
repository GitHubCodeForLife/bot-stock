from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class JobScheduler(db.Model):
    job_id : Mapped[str] = mapped_column(primary_key=True)
    job_func : Mapped[str] = mapped_column()
    job_data : Mapped[str] = mapped_column()
    job_interval : Mapped[int] = mapped_column()  # in seconds
    trigger_args : Mapped[str] = mapped_column()
    create_time : Mapped[str] = mapped_column()

class JobOptLog(db.Model):
    log_id : Mapped[int] = mapped_column(primary_key=True)
    job_func : Mapped[str] = mapped_column()
    job_status : Mapped[str] = mapped_column()
    job_time : Mapped[str] = mapped_column()
    job_message : Mapped[str] = mapped_column()