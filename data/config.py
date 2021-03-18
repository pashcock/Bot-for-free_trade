import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [349368261, 459359171, 173372397]
new_admins = [349368261, 459359171, 173372397]
channel = os.getenv("channel")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
ip = "localhost"

botname = 'trader_lib_bot'
botname_m = 'trader\\_lib\\_bot'
channelname = 'trader_lib'


additional_channel = ''
channel_link = ''
caption = ''


video_blurb = ''
photo_blurb = ''
caption_blurb = ''
text_blurb = ''
parse_blurb = 'Markdown'
url_text_blurb = ''
url_link_blurb = ''
preview_blurb = 0
save_blurb = 0

video_mail = ''
photo_mail = ''
caption_mail = ''
text_mail = ''
parse_mail = 'Markdown'
url_text_mail = ''
url_link_mail = ''
notification_mail = 0
preview_mail = 0
save_mail = 0


redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
