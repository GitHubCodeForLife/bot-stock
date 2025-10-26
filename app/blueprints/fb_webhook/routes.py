from flask import Blueprint
from flask import Blueprint, render_template, redirect, url_for, request

fb_bp = Blueprint('fb', __name__, url_prefix='/fb')

@fb_bp.route("/webhook", methods=['POST', 'GET'])
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