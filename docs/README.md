<!-- TOC -->
* [Slackybot usage](#slackybot-usage)
    * [Slack App token scopes](#slack-app-token-scopes)
    * [Importing module](#importing-module)
    * [Initialize the Slack object](#initialize-the-slack-object)
    * [Send message](#send-message)
    * [Send reply in the thread](#send-reply-in-the-thread)
    * [List all sent messages](#list-all-sent-messages)
    * [List all sent replies](#list-all-sent-replies)
* [List of all methods](#list-of-all-methods)
<!-- TOC -->

# Slackybot usage
### Slack App token scopes
The Slack App should have following token scopes:  
`channels:join` `channels:read` `chat:write` `chat:write.customize` `chat:write.public`


### Importing module
```python
from slackybot import Slack
```


### Initialize the Slack object
```python
slack = Slack(token=None, default_channel='')
```
Initialize the Slack object.

**token** - (string) OAuth token of the Slack App  
**default_channel** - (string) You can specify the default channel - it may be overwritten later.


### Send message
```python
message = slack.send_message(channel='', text='')
```
Sends message to the channel. It returns the Message object.

**channel** - (string) The channel name. It overwrites the default one if passed in the initialization.  
**text** - (string) A message to be sent.


### Send reply in the thread
```python
reply = message.send_reply(text='')
```
Sends the reply to the message. It is a method of the message object.

**text** - (string) A message to be sent.


### List all sent messages
```python
slack.get_messages()
```
Lists all sent messages. Returns list of the Message objects.


### List all sent replies
```python
message.get_replies()
```
Lists all sent replies. Returns list of the Reply objects. It is a method of the Message object.


### Update message or reply
```python
message.update(text='')
reply.update(text='')
```
Updates the message or reply.

**text** - (string) A message to be sent.


### Delete message or reply
```python
message.delete()
reply.delete()
```
Deletes the message or reply.


---


# List of methods of all objects

| Object  | Method                              | Returns        |
|---------|-------------------------------------|----------------|
| Slack   | `send_message(channel='', text='')` | Message object |
|         | `get_messages()`                    | List           |
| Message | `update(text='')`                   | -              |
|         | `send_reply(text='')`               | Reply object   |
|         | `get_replies()`                     | List           |
|         | `delete()`                          | -              |
| Reply   | `update(text='')`                   | -              |
|         | `delete()`                          | -              |