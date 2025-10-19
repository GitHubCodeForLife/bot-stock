from flask import Blueprint, render_template
from config import Config

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route("/jobs")
def jobPage():
    job_list : list = Config.scheduler.get_jobs()
    Config.scheduler.export_jobs("./app/static/files/jobs.json")

    for job in job_list:
        print(f"Job ID: {job.id}, Next Run Time: {job.next_run_time}")

    return render_template('jobs.html', job_list=job_list)
