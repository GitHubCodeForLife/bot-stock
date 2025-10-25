from flask import Flask
from app.model.models import db
from app.model.jobSchedulerRepo import JobScheduler
from app.model.jobOptLogRepo import JobOptLog
from app.model.notifcationLogRepo import NotificationLog
from app.scheduler.botScheduler import BotScheduler
from app.shareData import ShareData
from app.scheduler.botListener import job_listener
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # init blueprints
    from .routes import main
    app.register_blueprint(main)

    # init database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)

    # init scheduler
    ShareData.botScheduler = BotScheduler()
    ShareData.app = app
    with app.app_context():
        db.create_all()
        ShareData.botScheduler.reload_jobs_from_db()
        
    ShareData.botScheduler.add_listener(job_listener)
    ShareData.botScheduler.start()

    return app

