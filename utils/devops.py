import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

def log_event(msg):
    logging.info(msg)