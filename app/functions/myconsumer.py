import json
from datetime import datetime
from app.libs.slack import post_message

from logging import (
    INFO,
    getLogger
)
log = getLogger(__name__)
log.setLevel(INFO)


def handler(event, context):
    """SQS Consumer function

    :param event: SQS Event
    :param context: Lambda Context
    """
    for record in event['Records']:
        body = json.loads(record['body'])
        log.info(body)
        message = body.get('message', None)
        if message:
            post_message(f'Your message: {message}')