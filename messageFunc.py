import logging
import time
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def sendMessage(toReplyMessage: Message, replyText: str, replyButtons:InlineKeyboardMarkup = None):
    try:
        return toReplyMessage.reply_text(replyText,
            disable_web_page_preview=True,
            quote=True,
            reply_markup = replyButtons)
    except FloodWait as e:
        time.sleep(e.x * 1.5)
        return toReplyMessage.reply_text(replyText,
            disable_web_page_preview=True,
            quote=True,
            reply_markup = replyButtons)
    except Exception as e:
        LOGGER.info(str(e))

def editMessage(toEditMessage: Message, editText: str, replyButtons:InlineKeyboardMarkup = None):
    try:
        return toEditMessage.edit(text=editText,
            disable_web_page_preview=True,
            reply_markup = replyButtons)
    except FloodWait as e:
        time.sleep(e.x * 1.5)
        return toEditMessage.edit(text=editText,
            disable_web_page_preview=True,
            reply_markup = replyButtons)
    except MessageNotModified as e:
        LOGGER.info(str(e))
    except Exception as e:
        LOGGER.info(str(e))

def sendDocument(toReplyDocument: Message, filePath: str, capt=None):
    try:
        return toReplyDocument.reply_document(filePath,caption=capt)
    except FloodWait as e:
        time.sleep(e.x * 1.5)
        return toReplyDocument.reply_document(filePath,caption=capt)
    except Exception as e:
        LOGGER.info(str(e))

def sendAudio(toReply, filePath, caption, progresArgs, duzenlenecek, c_time, indirilenBoyut, toplamGonderilen):
    duration, artist, title = getMediaInfo(filePath)
    try:
        return toReply.reply_audio(audio=filePath, disable_notification=True,
				caption=caption,duration=duration, performer=artist,title=title, thumb="src/file.jpg",
				quote=True, progress = progressMulti,
				progress_args=(progresArgs, duzenlenecek, c_time, indirilenBoyut, toplamGonderilen))
    except FloodWait as e:
        time.sleep(e.x * 1.5)
        return toReply.reply_audio(audio=filePath, disable_notification=True,
				caption=caption,duration=duration, performer=artist,title=title, thumb="src/file.jpg",
				quote=True, progress = progressMulti,
				progress_args=(progresArgs, duzenlenecek, c_time, indirilenBoyut, toplamGonderilen))
    except Exception as e:
        LOGGER.info(str(e))
