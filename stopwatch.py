import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv


def reply(chat_id, text):
    message_id = bot.send_message(
        chat_id, 'Осталось {} секунд(ы):'.format(parse(text)))
    bot.create_countdown(parse(text), notify_progress,
                         message_id=message_id, chat_id=chat_id,
                         secs_total=parse(text))
    bot.create_timer(parse(text), notify, chat_id=chat_id)


def notify(chat_id):
    bot.send_message(chat_id, 'Время вышло!')


def notify_progress(secs_left, message_id, chat_id, secs_total):
    updated_message = 'Осталось {} секунд(ы) \n'.format(
        secs_left) + render_progressbar(secs_total, secs_left)
    bot.update_message(chat_id, message_id, updated_message)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    load_dotenv('token.env')
    token = os.getenv('TG_TOKEN')
    global bot
    bot = ptbot.Bot(token)
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == "__main__":
    main()
