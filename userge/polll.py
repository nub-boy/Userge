""" create poll, vote poll, stop poll, retract vote """

# By @Krishna_Singhal

import random
from userge import userge, Message


@userge.on_cmd("poll", about={
    'header': "Create Poll of Suggestion to get opinion",
    'usage': "{tr}poll [reply to ques text]"},
    allow_private=False)
async def create_poll(msg: Message):
    """" Create poll """

    options = ["Yes, Sure 😎", "No interest 🙄", "What..? 😳😳🤔🤔"]

    replied = msg.reply_to_message
    if replied:
        query = "Do you agree with that replied Suggestion..?"
        msg_id = replied.message_id
        await userge.send_poll(msg.chat.id, query, options,
                           reply_to_message_id=msg_id)
    else:
        query = "Do you agree with that Suggestion..?"
        await userge.send_poll(msg.chat.id, query, options)
    await msg.delete()


@userge.on_cmd("vote", about={
    'header': "Vote poll",
    'description': "Options are in numeric "
                   "(Count start in Python from 0) "
                   "see example to vote option no. 1", 
    'usage': "{tr}vote [option | reply to poll]",
    'examples': "{tr}vote 0 (with reply to poll)"},
    allow_private=False)
async def vote_poll(msg: Message):
    """ vote poll """

    replied = msg.reply_to_message
    if replied and replied.poll:
        if msg.input_str and msg.input_str.isnumeric():
            option = int(msg.input_str)
        else:
            option = random.randint(0, len(replied.poll.options) - 1)

        try:
            await userge.vote_poll(msg.chat.id, replied.message_id, option)
        except Exception as l:
            await msg.err(l)
        else:
        	await msg.edit("`Votted poll...`")
    else:
        await msg.err("How can I vote without reply to poll")


@userge.on_cmd("stop", about={
    'header': "Stop a poll which was sent by you.",
    'usage': "{tr}stop [reply to poll]"},
    allow_private=False)
async def stop_poll(msg: Message):
    """ Stop poll """

    replied = msg.reply_to_message

    if replied and replied.poll:
        try:
            await userge.stop_poll(msg.chat.id, replied.message_id)
        except Exception as l:
            await msg.err(l)
        else:
            await msg.edit("`Poll Stopped...`")
    else:
        await msg.err("How can I stop poll without reply a poll")


@userge.on_cmd("retract", about={
    'header': "Retract your vote in a Poll",
    'usage': "{tr}retract [reply to poll]"},
    allow_private=False)
async def retract_vote(msg: Message):
    """ Retract vote """

    replied = msg.reply_to_message

    if replied and replied.poll:
        try:
            await userge.retract_vote(msg.chat.id, replied.message_id)
        except Exception as l:
            await msg.err(l)
        else:
            await msg.edit("`Vote retracted...`")
    else:
        await msg.err("How can I retract your vote without reply a poll")
