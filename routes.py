from flask import request, Blueprint
from message_functions import send_message_to_channel
import json

bot_api = Blueprint('bot_api', __name__)

REQUEST_CATEGORY = 'category'
CAT_MESSAGE_NOTIFICATION = 'bot_message_notification'
CAT_GROUP_CHANNEL_JOIN = 'bot_event/group_channel:join'
CAT_GROUP_CHANNEL_LEAVE = 'bot_event/group_channel:leave'

PARAM_CHANNEL = 'channel'
PARAM_CHANNEL_URL = 'channel_url'
PARAM_MESSAGE = 'message'
PARAM_MESSAGE_TEXT = 'text'

HTTP_VALID_RESPONSE = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@bot_api.route('/', methods=['GET'])
def get_request():
  return HTTP_VALID_RESPONSE

@bot_api.route('/bot', methods=['POST'])
def bot_request():
  requested_params = request.get_json()
  category = requested_params[REQUEST_CATEGORY]

  if category == CAT_MESSAGE_NOTIFICATION:
    return on_message_arrived(requested_params)

  return HTTP_VALID_RESPONSE


def on_message_arrived(requested_params):
  """
  On message arrive.
  :param requested_params: requested param
  """
  message = requested_params[PARAM_MESSAGE][PARAM_MESSAGE_TEXT]
  channel_url = requested_params[PARAM_CHANNEL][PARAM_CHANNEL_URL]
  if message == "ping":
    send_message_to_channel("pong", channel_url)

  return HTTP_VALID_RESPONSE