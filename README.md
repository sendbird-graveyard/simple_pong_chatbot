# SendBird Pong Bot Example
This is a a basic chat bot written to integration with SendBird's Bot Interface (https://docs.sendbird.com/platform/bot_interface)


## What do this bot do?
This bot simply responds with "pong" any time a user in a channel sends "ping"

## What functions did this application use from the Bot Interface API?
 - [Receiving messages from the channel](https://docs.sendbird.com/platform/bot_interface#2_bot_interface)
 - [Sending messages to the channel](https://docs.sendbird.com/platform/bot_interface#3_send_message_from_bot)
 
 
## Tutorial / How to Run
Refer to the [Bot Interface Tutorial: Pong Bot](https://docs.google.com/document/d/1Tuo2XLtoY8uMwF8trpuGxnKnxXfE7VPYKbYHyFfq4AA/edit?usp=sharing). This tutorial covers deploying this bot to AWS Elastic Beanstalk so that it can integrate with SendBird's Bot Interface and respond to real requests.


## What needs to be changed.
In config.py the following changes are needed:
 - Change **host** to match the SendBird endpoint for your application (Found in the SendBird Dashboard).
 - Change **api_token** to match your SendBird Application's API Token.
 - Change **bot_id** to match your SendBird Application's Bot ID that you will create in the tutorial.
 
## Code Overview

### application.py
This file contains the flask and server code

### config.py 
Configuration options including the api_token, SendBird app endpoint to target and bot_id.

### routes.py 
Routing the bot event/webhook received from SendBird to the correct action from the bot. In this case there is only one action which is to respond to a ping message.

### message_functions.py
Contains the logic to actually send a message back to SendBird.
