from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory,session
import uuid
import time
import os
from datetime import datetime

web = Blueprint("web", __name__)

@web.route("/")
def index():
    return render_template("index.html")

@web.route('/content-creator/create')
def content_creator_create():
    # Get API configuration from app config - NO STATIC FALLBACKS
    api_base_url = current_app.config.get('API_BASE_URL')
    api_preview_url = current_app.config.get('API_PREVIEW_URL')
    api_token = current_app.config.get('API_TOKEN', '')
    
    # Check if URLs are configured - if not, pass empty or None
    api_config = {
        'API_BASE_URL': api_base_url or '',
        'API_PREVIEW_URL': api_preview_url or '',
        'API_TOKEN': api_token,
        'HAS_CONFIG': bool(api_base_url and api_preview_url)  # Flag to check if configured
    }
    
    return render_template(
        'content-creator/create.html',
        api_config=api_config
    )


# ============================================
# GREAT ADVISOR ROUTES
# ============================================

@web.route('/great-advisor')
def great_advisor():
    """Great Advisor - Input page"""
    # Get API configuration
    api_config = {
        'API_BASE_URL': current_app.config.get('API_BASE_URL', ''),
        'API_TOKEN': current_app.config.get('API_TOKEN', ''),
        'HAS_CONFIG': bool(current_app.config.get('API_BASE_URL'))
    }
    
    return render_template(
        'great-advisor/index.html',
        api_config=api_config
    )

@web.route('/great-advisor/store-result', methods=['POST'])
def store_result():
    session['great_advisor_result'] = request.get_json()
    return jsonify(success=True)

@web.route('/great-advisor/result')
def great_advisor_result():
    result_data = session.get('great_advisor_result')
    return render_template(
        'great-advisor/results-screen.html',
        result_data=result_data
    )


@web.route('/reference-collector')
def reference_collector():
    api_config = {
        'API_BASE_URL': current_app.config.get('API_BASE_URL', ''),
        'API_TOKEN': current_app.config.get('API_TOKEN', ''),
        'HAS_CONFIG': bool(current_app.config.get('API_BASE_URL'))
    }
    
    return render_template(
        'reference-collector/index.html',
        api_config=api_config
    )


@web.route('/structure-builder')
def structure_builder():
    api_config = {
        'API_BASE_URL': current_app.config.get('API_BASE_URL', ''),
        'API_TOKEN': current_app.config.get('API_TOKEN', ''),
        'HAS_CONFIG': bool(current_app.config.get('API_BASE_URL'))
    }
    
    return render_template(
        'structure-builder/index.html',
        api_config=api_config
    )

@web.route('/qa-checker/cgp')
def qa_checker_openai():
    api_config = {
        'API_BASE_URL': current_app.config.get('API_BASE_URL', ''),
        'API_TOKEN': current_app.config.get('API_TOKEN', ''),
        'HAS_CONFIG': bool(current_app.config.get('API_BASE_URL'))
    }
    
    return render_template(
        'qa_checker/openAI/index.html',
        api_config=api_config
    )

@web.route('/qa-checker/cld')
def qa_checker_cluade():
    api_config = {
        'API_BASE_URL': current_app.config.get('API_BASE_URL', ''),
        'API_TOKEN': current_app.config.get('API_TOKEN', ''),
        'HAS_CONFIG': bool(current_app.config.get('API_BASE_URL'))
    }
    
    return render_template(
        'qa_checker/cluade/index.html',
        api_config=api_config
    )

@web.route("/about")
def about():
    return "<h1>About Page</h1>"

@web.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"

@web.route("/hello")
def hello():
    return "Hello, Flask!"

@web.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")