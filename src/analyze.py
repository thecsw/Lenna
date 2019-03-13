import praw
import json
import time
import re

from utils import log_to_file

replace_chars = ['"', '.', ';', ':', '?', '!', '*', '+', '-', '(', ')', '[', ']', '{', '}', '>', '<', ',', '^', '@',
                 '$', '%', '&', '_', '=', '\n', '|', '\\', "#", '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def parse_comment(c):
    try:
        file = open("./data-analyzation/words.json", 'r')
        words_json = json.loads(file.read())
        file.close()

        print("Reading comment " + c.id + " at " + time.strftime("%b %d, %Y - %I:%M:%S") + " by " + str(c.author))

        body = str(c.body.encode('utf-8'))

        for w in body.split(' '):
            word = str(w.encode('utf-8'))

            if "http" in word or "/u/" in word or "/r/" in word or "\\" in word:
                continue

            for ch in replace_chars:
                word = word.replace(ch, '')

            if word is not "" and word is not " " and word is not "'" and word is not "," and word is not '\n' and word[0] is not "'":

                if word in words_json.keys():
                    words_json[word] = int(words_json.get(word)) + 1
                else:
                    words_json[word] = 1

                file = open("./data-analyzation/words.json", 'w')
                file.write(json.dumps(words_json))

                file.close()

    except:
        log_to_file("Failed to read words.json at " + time.strftime("%b %d, %Y - %I:%M:%S"))
        return
