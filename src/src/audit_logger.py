import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO
)

def log_request(query):

    logging.info(query)
