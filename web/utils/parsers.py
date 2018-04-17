import os
import pandas as pd

from main import slack_client


def get_all_user_names(channel_id):
    data = slack_client.api_call('users.list')
    return [(d['name'], d['profile']['real_name_normalized'])
            for d in data['members']]


def parse_text(message, channel, username):
    """
    Read local csv and determine all statuses
    """
    pass


def build_log_entry():
    target = os.path.join(app.config.APP_ROOT,
                          'data/test_data.csv')
    df = pd.read_csv(target)
    return df
