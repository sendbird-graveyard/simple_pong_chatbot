import requests
import json
from config import *

def request_to_sb(method, endpoint, data={}, token=None):
  """
  Request to SendBird.
  :param method: method of the request
  :param endpoint: endpoint of the request
  :param data: data to put in the request
  :param token: token to add in the request
  """

  headers = {}
  headers['Content-Type'] = 'application/json'
  headers['Api-Token'] = token

  if method == 'POST':
    requests.post(
      url=endpoint,
      data=json.dumps(data),
      headers=headers
    )
  else:
    raise ValueError('Request method must be POST, GET , DELETE or PUT')

ENDPOINT_BOT = host + '/bots/{}'.format(bot_id)
ENDPOINT_SEND_MESSAGE = ENDPOINT_BOT + '/send'

def send_message_to_channel(message, channel_url):
  """
  Send message to a certain channel.
  :param message: message content
  :param channel_url: url of channel to send
  """
  request_to_sb(method='POST', endpoint=ENDPOINT_SEND_MESSAGE,
                data={'channel_url': channel_url, 'message': message}, token=token)