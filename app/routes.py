from flask import Blueprint, render_template, redirect, url_for
from app.shareData import ShareData
main = Blueprint('main', __name__)

@main.route('/')
def home():
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
    return redirect(url_for('main.jobPage'))