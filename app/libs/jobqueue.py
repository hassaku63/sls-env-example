import json
from app.libs.aws import sqs
from app import settings

from logging import (
    INFO,
    getLogger
)
log = getLogger(__name__)
log.setLevel(INFO)


def enqueue_message(message: object):
    queue_url = sqs.get_queue_url(
        account=settings.AWS_ACCOUNT_ID,
        region=settings.AWS_REGION,
        queue_name=settings.MY_QUEUE_NAME
    )
    log.info({
        'event': 'enqueue_message',
        'message': {
            'queue_url': queue_url,
            'message': message
        }
    })
    return sqs.send_message(
        queue_url=queue_url,
        message=json.dumps(message)
    )