import socks
import telethon.sync
from telethon import TelegramClient
from tqdm import tqdm

# Go to my.telegram.org, register desktop app and copy id and hash
api_id = 123456
api_hash = 'qwertyqwerty12345123456'

# If you need proxy
proxy_type = socks.SOCKS5
proxy_host = 'IP'
proxy_port = 1111
proxy = (proxy_type, proxy_host, proxy_port)

# Go to chat settings and generate invite link
# NOTE: your group chat must be a supergroup, otherwise script can't get messages
chat_link = 'https://t.me/joinchat/qwertyqwerty'

# 'download' it's just a session name, you can write anything here
client = TelegramClient('download', api_id, api_hash, proxy=proxy)
client.start()
messages = client.get_messages(chat_link, limit=1000)

print(len(messages))
for message in tqdm(messages):
    client.download_media(message)
