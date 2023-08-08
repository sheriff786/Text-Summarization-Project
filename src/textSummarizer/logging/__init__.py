#custom logges
import os
import sys
import logging

logging_str ="[%(asctime)s: %(levelname)s :%(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_los.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath), #it will create log file and insert loges details 
        logging.StreamHandler(sys.stdout) #it will show los in terminals
    ]
)
logger = logging.getLogger("textSummarizerLogger")
