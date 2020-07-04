import boto3
from app import settings

from logging import (
    INFO,
    getLogger
)
log = getLogger(__name__)
log.setLevel(INFO)


sqs_client = None


def _get_sqs_client():
    global sqs_client
    if sqs_client is None:
        sqs_client = boto3.client('sqs')
    return sqs_client


def get_queue_url(account, region, queue_name):
    log.info({
        'event': '_get_queue_url',
        'message': f'https://sqs.{region}.amazonaws.com/{account}/{queue_name}'
    })
    return f'https://sqs.{region}.amazonaws.com/{account}/{queue_name}'


def send_message(queue_url: str, message: str):
    sqs = _get_sqs_client()
    return sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )