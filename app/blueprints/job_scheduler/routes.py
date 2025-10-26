from flask import Blueprint, render_template, jsonify, redirect, url_for
from app.shareData import ShareData

job_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@job_bp.route("")
def jobPage():
    job_list : list = ShareData.botScheduler.scheduler.get_jobs()
    ShareData.botScheduler.scheduler.export_jobs("./app/static/files/jobs.json")
    return render_template('job_scheduler/jobs.html', job_list=job_list)


@job_bp.route("/reload_jobs", methods=['POST'])
def reload_jobs():
    ShareData.botScheduler.reload_jobs_from_db()
    ShareData.botScheduler.start()
    # Redirect back to jobs page
    return redirect(url_for('main.jobs.jobPage'))
