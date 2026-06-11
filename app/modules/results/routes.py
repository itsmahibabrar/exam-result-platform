from flask import Blueprint, jsonify

results_bp = Blueprint("results", __name__)


@results_bp.get("/")
def list_results():
    return jsonify(
        {
            "message": "Results module boilerplate is ready.",
            "endpoints": ["GET /health", "GET /api/results/"],
        }
    )
