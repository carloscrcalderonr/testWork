import logging

class AppLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)


        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.DEBUG)


        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)


        self.logger.addHandler(file_handler)

    def log_request(self, method: str, path: str, payload=None):
        self.logger.info(f"Request: {method} {path} - Payload: {payload}")

    def log_response(self, response):
        self.logger.info(f"Response: {response}")
