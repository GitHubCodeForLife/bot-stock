from flask import Blueprint, render_template
from app.shareData import ShareData
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
    job_list : list = ShareData.botScheduler.scheduler.get_jobs()
    ShareData.botScheduler.scheduler.export_jobs("./app/static/files/jobs.json")
    return render_template('jobs.html', job_list=job_list)

@main.route("/reload_jobs", methods=['POST'])
def reload_jobs():
    ShareData.botScheduler.reload_jobs_from_db()
    ShareData.botScheduler.start()
    # Redirect back to jobs page
    return jobPage()