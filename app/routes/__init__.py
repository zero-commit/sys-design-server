from .submissions import submissions_bp
from .evaluations import evaluations_bp
from .problems import problems_bp

def register_routes(app):
    app.register_blueprint(submissions_bp)
    app.register_blueprint(evaluations_bp)
    app.register_blueprint(problems_bp)
