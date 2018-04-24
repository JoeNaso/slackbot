from flask import Flask, request, Response

from slackclient import SlackClient
from config import BaseConfig

from utils.slack import channel_info, get_all_user_names, send_message
from utils.parsers import parse_text

app = Flask(__name__)
app.config.from_object(BaseConfig)

slack_client = SlackClient(app.config['SLACK_WEBHOOK_SECRET'])

users = {}

@app.route('/slack', methods=['POST'])
def incoming():
    print(request)
    if request.form.get('token') == app.config['SLACK_WEBHOOK_SECRET']:
        channel = request.form.get('channel_name')
        username = request.form.get('username')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says " + text
        print(inbound_message)
        return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works, yo!')


if __name__ == '__main__':
    app.run(debug=True)
