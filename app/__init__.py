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
from flask_caching import Cache


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

    # init cached
    app.config['CACHE_TYPE'] = os.getenv('CACHE_TYPE')
    app.config['CACHE_DEFAULT_TIMEOUT'] = os.getenv('CACHE_DEFAULT_TIMEOUT')
    cache = Cache()
    cache.init_app(app)

    # init scheduler
    ShareData.botScheduler = BotScheduler()
    ShareData.app = app
    ShareData.cache = cache
    is_worker = os.getenv('IS_WORKER')
    print("IS_WORKER: " + is_worker)
    if is_worker == 'False':
        with app.app_context():
            # print("init scheduler")
            db.create_all()
            ShareData.botScheduler.reload_jobs_from_db()
            ShareData.botScheduler.add_listener(job_listener)
            ShareData.botScheduler.start()
        
    ShareData.botScheduler.init_woker()

    return app

