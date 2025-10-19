from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime
from app.scheduler.schedulerTask import task_send_notif_stock_price
from config import Config
from apscheduler.schedulers.background import BackgroundScheduler
from app.model.models import db

# Initialize scheduler
scheduler = BackgroundScheduler()

# Define a scheduled job
# @scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=10, max_instances=1)
def job():
    print(f"[{datetime.now()}] Running scheduled task...")
    task_send_notif_stock_price()
    print(f"[{datetime.now()}] Task completed.")

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # init blueprints
    from .routes import main
    app.register_blueprint(main)

    # init scheduler
    scheduler.start()
    scheduler.add_job(func=job, trigger="interval", seconds=20, id='job_1', replace_existing=True)
    Config.scheduler = scheduler

    # init database
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

    return app


