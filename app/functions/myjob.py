import json
from datetime import datetime
from app.libs import jobqueue

from logging import (
    INFO,
    getLogger
)
log = getLogger(__name__)
log.setLevel(INFO)


def handler(event, context):
    now = datetime.now()
    message = {
        'timestamp': now.timestamp(),
        'message': f'hello, now is {str(now)}'
    }
    log.info({
        'event': 'handler',
        'message': message
    })
    response = jobqueue.enqueue_message(message)
    log.info({
        'event': 'handler.enqueue_message',
        'message': response
    })
    return response
