from userbot import bot, logger
from telethon import TelegramClient, events
from config import groupinfo


@bot.on(events.NewMessage(**groupinfo))
async def fn(event):
    logger.info("group info plugin called")
    try:
        id = event.message.to_id.channel_id
        logger.info(f"sending group id - {id}")
        await event.respond(f"groupid - {id}")
    except AttributeError:
        id = event.message.to_id.user_id
        logger.info(f"sending user id - {id}")
        await event.respond(f"userid - {id}")
    except Exception as e:
        logger.exception(f"Error while fetching records {e}")
        return

