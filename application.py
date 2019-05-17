from flask import Flask
from routes import bot_api
application = Flask(__name__)
application.debug = True

application.register_blueprint(bot_api)
if __name__ == '__main__':
  try:
    application.run()
  except IndexError:
    print('Wrong run command.\n')
    print('python app.py <API_HOST> <APP_TOKEN> <BOT_ID>')
