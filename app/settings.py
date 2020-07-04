"""
Declare all environment variables defined in .env.<stage-name> and serverless.yml as python variables.

If you would like to use environment variables in your code, you import this module then reference as constants of python variable.
By use this technique, you are able to use IDE auto-completion effectively when you writing python code.
It is useful to reduce miss-typing of environment variables.
"""
import os
import pathlib
import json
import dotenv

project_root_dir = pathlib.Path(__file__).parent / '../'

dotenv.load_dotenv()
MYAPP_STAGE_NAME = os.environ.get('MYAPP_STAGE_NAME')

stage_env_path = project_root_dir / f'.env.{MYAPP_STAGE_NAME}'
dotenv.load_dotenv(stage_env_path.resolve())

# Slack
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')

# AWS
AWS_ACCOUNT_ID = os.environ.get('AWS_ACCOUNT_ID')
# Notice: You don't need to define AWS_REGION in .env and serverless.yml
# because of lambda runtime automatically set AWS_REGION env var when execute.
AWS_REGION = os.environ.get('AWS_REGION') 

# SQS
MY_QUEUE_NAME = os.environ.get('MY_QUEUE_NAME', '')