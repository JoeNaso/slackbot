import os

from slackclient import SlackClient


class BaseConfig(object):
    """
    Some basic subclassing for different configuration defaults
    """
    DEBUG = os.environ.get('DEBUG', True)
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_OAUTH_TOKEN')
