import json
from slack import WebClient
from app import settings

from logging import (
    INFO,
    getLogger
)
log = getLogger(__name__)
log.setLevel(INFO)


slk = None

def _get_client():
    global slk
    if slk is None:
        slk = WebClient(token=settings.SLACK_BOT_TOKEN)
    return slk


def post_message(text: str):
    client = _get_client()
    params = {
        'channel': settings.SLACK_CHANNEL,
        'blocks': [{
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': text
            }
        }]
    }
    log.info({
        'event': 'slack.post_message',
        'message': json.dumps(params)
    })
    # client.chat_postMessage(**params)