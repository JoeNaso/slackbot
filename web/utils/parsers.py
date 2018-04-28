import csv
import datetime
import os
import spacy

from config import BaseConfig

from .slack import get_all_user_names


def _get_nlp():
    return spacy.load('en')


def parse_text(message, channel, username):
    """
    Find names entities in message
    Check for username or name
    """
    nlp = _get_nlp()
    ents = nlp(message)
    winners = []
    for name, real_name in get_all_user_names():
        for ent in ents:
            if ent == name or ent == real_name:
                winners.append(ent)
    if len(winners) > 1:
        raise ValueError("There is apparently more than one winner. Huh?")
    else:
        return winners[0]


def build_log_entry(app, username, full_name):
    """
    Takes app as an arg to avoid circular imports
    """
    with open(os.path.join(BaseConfig.APP_ROOT, 'data/test_data.csv'), 'a') as log:
        writer = csv.writer(log, delimiter=',')
        writer.write([username, full_name, True, datetime.datetime.today(), False])
    return


def build_message(winner):
    return "Congrats to {winner} :metal:"
