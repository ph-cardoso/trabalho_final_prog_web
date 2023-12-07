import logging


# Filter definition
class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.args and len(record.args) >= 3 and record.args[2] != "/healthz"


def filter_log():
    logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
