import random
import logging
import os


def generate_random(event, context):
    default_log_args = {
        "level": logging.DEBUG if os.environ.get("DEBUG", False) else logging.INFO,
        "format": "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        "datefmt": "%d-%b-%y %H:%M",
        "force": True,
    }

    logging.basicConfig(**default_log_args)
    log = logging.getLogger("Run-Lambda")

    log.info("I m here too")

    data = random.random()
    log.info(data)

    return {
        'data' : data

    }