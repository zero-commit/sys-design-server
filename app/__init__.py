from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from app.routes.problems import problems_bp
    from app.routes.submissions import submissions_bp
    from app.routes.evaluations import evaluations_bp

    app.register_blueprint(problems_bp)
    app.register_blueprint(submissions_bp)
    app.register_blueprint(evaluations_bp)

    return app
