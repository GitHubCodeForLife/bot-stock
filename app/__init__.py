from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime
from bot.app.scheduler.schedulerTask import task_send_notif_stock_price

# Initialize scheduler
scheduler = APScheduler()

# Define a scheduled job
@scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=10, max_instances=1)
def job():
    print(f"[{datetime.now()}] Running scheduled task...")
    task_send_notif_stock_price()
    print(f"[{datetime.now()}] Task completed.")

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes import main
    app.register_blueprint(main)

    scheduler.init_app(app)
    scheduler.start()

    return app


