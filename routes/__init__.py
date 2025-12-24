from .submissions import bp as submissions_bp
from .evaluations import bp as evaluations_bp

def register_routes(app):
    app.register_blueprint(submissions_bp)
    app.register_blueprint(evaluations_bp)
