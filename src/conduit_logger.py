import logging
import sys
from datetime import datetime
from functools import wraps

# Configure logging with otherworldly format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class ConduitLogger:
    """Logging system for OpenClaw - Conduit Layer"""
    
    @staticmethod
    def log_conduit_opened(entity_id):
        """Log successful authentication"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[T+{timestamp}] Conduit opened: entity '{entity_id}' verified")
        logging.info(f"Conduit opened: entity '{entity_id}' verified at T+{timestamp}")
    
    @staticmethod
    def log_anomaly_detected(entity_id, reason):
        """Log failed authentication"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[T+{timestamp}] ANOMALY DETECTED: entity '{entity_id}' - {reason}")
        logging.warning(f"Anomaly detected: entity '{entity_id}' - {reason} at T+{timestamp}")
    
    @staticmethod
    def log_request(method, endpoint, status, duration_ms):
        """Log API requests"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_symbol = "✓" if status < 400 else "✗"
        print(f"[T+{timestamp}] Request: {method} {endpoint} | Status: {status} {status_symbol} | Duration: {duration_ms}ms")
        logging.info(f"Request processed: {method} {endpoint} | Status: {status} | Duration: {duration_ms}ms")
    
    @staticmethod
    def log_error(error_type, details):
        """Log system errors"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[T+{timestamp}] CRITICAL ERROR: {error_type} | Details: {details}")
        logging.error(f"System error: {error_type} | Details: {details} at T+{timestamp}")

def conduit_entry_required(func):
    """Decorator to track function entry/exit"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = func.__name__
        print(f"[T+{timestamp}] Conduit entry: {func_name} initiated")
        try:
            result = func(*args, **kwargs)
            print(f"[T+{timestamp}] Conduit exit: {func_name} completed")
            return result
        except Exception as e:
            print(f"[T+{timestamp}] Conduit breach: {func_name} failed - {str(e)}")
            raise
    return wrapper

if __name__ == "__main__":
    # Test the logging system
    logger = ConduitLogger()
    
    print("=" * 60)
    print("OPENCLAW CONDUIT LAYER - SYSTEM TEST")
    print("=" * 60)
    
    # Test successful authentication
    logger.log_conduit_opened("entity_alpha_001")
    
    # Test request logging
    logger.log_request("GET", "/api/capital-flux", 200, 45)
    logger.log_request("POST", "/api/transfer", 403, 12)
    
    # Test anomaly detection
    logger.log_anomaly_detected("entity_unknown_999", "Invalid credentials")
    
    # Test error logging
    logger.log_error("DatabaseTimeout", "Connection lost to primary node")
    
    # Test decorator
    @conduit_entry_required
    def sample_capital_calculation():
        return "Capital flux calculated"
    
    result = sample_capital_calculation()
    
    print("=" * 60)
    print("CONDUIT LAYER TEST COMPLETE")
    print("=" * 60)
