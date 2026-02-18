from flask import Flask, jsonify
from src.conduit_logger import ConduitLogger
from src.database import test_connection
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Root endpoint - System status"""
    logger = ConduitLogger()
    logger.log_request("GET", "/", 200, 0)
    
    return jsonify({
        "system": "OpenClaw",
        "status": "Conduit established",
        "phase": "Phase 1 - Conduit Layer Active",
        "timestamp": "T+2026-02-17"
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    logger = ConduitLogger()
    
    # Test database connection
    db_status = test_connection()
    
    if db_status:
        logger.log_conduit_opened("health_check_entity")
        return jsonify({
            "status": "Operational",
            "database": "Connected",
            "conduit": "Open"
        }), 200
    else:
        logger.log_anomaly_detected("health_check_entity", "Database unreachable")
        return jsonify({
            "status": "Degraded",
            "database": "Disconnected",
            "conduit": "Compromised"
        }), 503

@app.route('/api/capital-flux')
def capital_flux():
    """Capital flux endpoint - Placeholder for Phase 2"""
    logger = ConduitLogger()
    logger.log_request("GET", "/api/capital-flux", 200, 0)
    
    return jsonify({
        "message": "Capital Flux Engine - Phase 2 pending deployment",
        "status": "Standby",
        "units": "Abstract capital units"
    })

if __name__ == "__main__":
    app.run(debug=True)
