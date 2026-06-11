from flask import Flask, jsonify

from .config import Config
from .db import init_app as init_db
from .modules.results.routes import results_bp


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    init_db(app)
    app.register_blueprint(results_bp, url_prefix="/api/results")

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok"})

    return app
