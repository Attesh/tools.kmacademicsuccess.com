from flask import Flask
from app.routes import web
from config import Config





app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)
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


# Load config.py into Flask
app.config.from_object(Config)

app.register_blueprint(web)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config["DEBUG"])