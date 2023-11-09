import time

from telethon import functions, types
from telethon.sessions import StringSession
import random as rand
from telethon.sync import TelegramClient

api_id = 26670426
api_hash = "2d3a55403d95725d6fc864750eeb3620"

nums = []
not_found = []
message = "Hello! This is an automated message, --> from sheff"
with open('numbers.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        nums.append(line.strip())


with TelegramClient(api_id=api_id, api_hash=api_hash, session=StringSession()) as client:
    for num in nums:
        result = client(functions.contacts.ImportContactsRequest(
            contacts=[types.InputPhoneContact(
                client_id= rand.randint(1, 10),
                phone=f'+{num}',
                first_name='x',
                last_name=num
            )]
        ))

        if result.imported:
            user_id = result.imported[0].user_id  # Extracting the user_id from the first imported contact
            print(user_id, " --> ", num)
            time.sleep(1)

            client.send_message(user_id, message)

            client(functions.contacts.DeleteContactsRequest(id=[user_id]))
        else:
            not_found.append(num)

with open('not_found.txt', 'w', encoding='UTF-8') as f:
    for num in not_found:
        f.write(f"{num}, not found!\n")

