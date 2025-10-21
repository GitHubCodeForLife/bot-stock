from flask import Flask
from datetime import datetime
from app.scheduler.schedulerTask import task_send_notif_stock_price
from config import Config
from app.model.models import db
from app.scheduler.botScheduler import BotScheduler
from app.shareData import ShareData
from app.scheduler.botListener import job_listener

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

    # init database
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

    # init scheduler
    ShareData.botScheduler = BotScheduler()
    ShareData.app = app
    with app.app_context():
        ShareData.botScheduler.reload_jobs_from_db()
        
    ShareData.botScheduler.add_listener(job_listener)
    ShareData.botScheduler.start()

    return app

