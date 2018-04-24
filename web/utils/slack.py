def list_channels(slack_client):
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


def channel_info(slack_client, channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def get_all_user_names(slack_client):
    """
    Gets tuples of username, full name
    """
    data = slack_client.api_call('users.list')
    return [(d['name'],
            d['profile']['real_name_normalized'])
            for d in data['members']]


def send_message(channel_id, message):
    res = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='john-pingry',
        as_user='false',
        icon_emoji=':moneybag:')
    return res


def all_channel_info():
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(channel['name'] + " --  ID: " + channel['id'])
            detailed_info = channel_info(channel['id'])
            print(detailed_info)
        print("----------")
    else:
        print("Unable to authenticate")
