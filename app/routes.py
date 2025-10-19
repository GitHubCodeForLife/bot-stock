from flask import Blueprint, render_template
from config import Config
from app.model.models import User
main = Blueprint('main', __name__)

@main.route('/')
def home():
    users = User.query.all()
    print("Registered Users:")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    return render_template('index.html')

@main.route("/jobs")
def jobPage():
    job_list : list = Config.scheduler.get_jobs()
    Config.scheduler.export_jobs("./app/static/files/jobs.json")

    for job in job_list:
        print(job)

    return render_template('jobs.html', job_list=job_list)
