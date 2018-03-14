# This files contains possible replies and how to reply

import cleverbot
import random

def clever_reply():
    cleverkey = config.cleverbotToken
    cb = cleverbot.Cleverbot(cleverkey, timeout=60)
    cb.reset()
    memepolice = reddit.redditor(bot_name)
    while True:
        for reply in memepolice.stream.replies():
            random = random.randint(0, 20)
            if random < 7:
                response = cb.say(command).encode('utf-8')
                reply.reply(response)
            else:
                pass
