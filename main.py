from flask import Flask
from config import Config

# Create Flask app - using absolute paths for templates and static
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'app', 'templates'),
    static_folder=os.path.join(BASE_DIR, 'app', 'static')
)

# Load config
app.config.from_object(Config)

# Register custom filters
@app.template_filter('level_class')
def level_class_filter(level):
    """Convert level to CSS class"""
    if not level:
        return 'p-poor'
    l = str(level).lower()
    if 'excell' in l:
        return 'p-exc'
    if 'good' in l:
        return 'p-good'
    if 'satisf' in l:
        return 'p-sat'
    if 'weak' in l:
        return 'p-weak'
    return 'p-poor'

@app.template_filter('priority_class')
def priority_class_filter(pri):
    """Convert priority to CSS class"""
    if not pri:
        return 'pb-m'
    p = str(pri).lower()
    if 'high' in p:
        return 'pb-h'
    if 'medium' in p:
        return 'pb-m'
    return 'pb-l'

# Import and register blueprint
try:
    from app.routes import web
    app.register_blueprint(web)
    print("✅ Blueprint 'web' registered successfully")
    print(f"📁 Template folder: {app.template_folder}")
    print(f"📁 Static folder: {app.static_folder}")
except ImportError as e:
    print(f"⚠️ Error importing blueprint: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config.get("DEBUG", False))
