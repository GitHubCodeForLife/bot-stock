from flask import Blueprint, render_template, jsonify
from .company_service import CompanyService
# Create a blueprint named 'company'
company_bp = Blueprint('company', __name__, url_prefix='/company')

@company_bp.route('/')
def company_home():
    return "Welcome to the Company section!"

@company_bp.route('/<company_name>')
def company_profile(company_name):
    news = CompanyService.get_company_news(company_name)
    columns = news.columns
    return render_template('company_overview/index.html', news=news.to_dict(orient='records'), columns=columns)

