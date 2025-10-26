from flask import Blueprint, render_template, redirect, url_for, request
from app.blueprints import company_bp, job_bp, fb_bp

main = Blueprint('main', __name__)
main.register_blueprint(company_bp)
main.register_blueprint(job_bp)
main.register_blueprint(fb_bp)

@main.route('/')
def home():
    return render_template('index.html')
