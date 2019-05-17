# SendBird Bot Interface Sample Application
This is a SendBird Bot Interface web server sample. This app receives and handles Webhooks from Sendbird.
## What do this application do?
This application is a simple ping pong bot
_And this bot can also play Rock Paper Scissors by `/rps <r|p|s>` command._
## What functions did this application use from the Bot Interface API?
 - [Receiving messages from the channel](https://docs.sendbird.com/platform/bot_interface#2_bot_interface)
 - [Sending messages to the channel](https://docs.sendbird.com/platform/bot_interface#3_send_message_from_bot)
## Create a new bot!
Refer to the [SendBird Document](https://docs.sendbird.com/platform/bot_interface#3_create_a_bot). Run this application and put this application's URL at `bot_callback_url` when you create a new bot.
## Run this sample!
First, you should install requirements.
```bash
pip install -r requirements.txt
```
After you install requirements, run this application!
```bash
python app.py <API_HOST> <APP_TOKEN> <BOT_ID>
```
