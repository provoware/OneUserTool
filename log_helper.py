import logging
import os

LOGFILE = os.path.join(os.path.dirname(__file__), 'oneusertool.log')
os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
logging.basicConfig(
    filename=LOGFILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def log(message: str) -> None:
    """Write a message to the global log file."""
    logging.info(message)
