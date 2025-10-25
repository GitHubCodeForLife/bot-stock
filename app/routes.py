from flask import Blueprint, render_template, redirect, url_for, request
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

@main.route("/fb/webhook", methods=['POST', 'GET'])
def webhok_received_fb():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return data
    hub_mode = request.args.get('hub.mode')
    hub_verify_token = request.args.get('hub.verify_token')
    hub_challenge = request.args.get('hub.challenge')
    
    if hub_verify_token == "1234":
        return hub_challenge, 200
    else:
        return "Verification failed", 400
    