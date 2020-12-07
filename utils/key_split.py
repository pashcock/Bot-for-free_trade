from data import config


async def key_split(arg):
    try:
        s = arg.split(' - ', 1)
        config.url_text_blurb = s[0]
        config.url_link_blurb = s[1]
        if config.url_link_blurb[0:4] == 'http':
            return True
        else:
            return False
    except:
        return False


async def key_split_mail(arg):
    try:
        s = arg.split(' - ', 1)
        config.url_text_mail = s[0]
        config.url_link_mail = s[1]
        if config.url_link_mail[0:4] == 'http':
            return True
        else:
            return False
    except:
        return False