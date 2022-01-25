import logging
from random import randint
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from saver import save

# Setting the chat ID the bot is desired to work in
chat_id = 'CHATID'
dumb_words = {
    0 : 'mamerto',
    1 : 'bobo',
    2 : 'melón',
    3 : 'fiera',
    4 : 'mastodonte',
    5 : 'tanque'
}

# Enable logger
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def am_on(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('Que no me hables, {}.'.format(dumb_words[randint(0,5)]))
    else:
        update.message.reply_text('Sí, {}.'.format(dumb_words[randint(0,5)]))

def wdid(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('Hablar contigo, no.')
    else:
        update.message.reply_text('Ahora mismo me dedico a guardar vuestros resultados de Wordle para cositas que se vendrán... 😏')

def wordlerank(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('¿Qué quieres?')
    else:
        with open("saves/overall.csv") as f:
            rank = f.read().split('\n')

        scoreboard = {}
        for p in rank:
            scoreboard[p.split(',')[0]] = int(p.split(',')[1])
        scoreboard = sorted(scoreboard.items(), key=lambda x:x[1], reverse=True)

        output = '⬜🟨🟩CLASIFICACIÓN🟩🟨⬜\n'
        for k,i in enumerate(scoreboard,start=1):
            output += '\n{}. {} - {} puntos'.format(str(k), i[0], i[1])
        update.message.reply_text(output)

def avg_pts(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('Shhhh')
    else:
        with open("saves/average.csv") as f:
            rank = f.read().split('\n')

        scoreboard = {}
        for p in rank:
            scoreboard[p.split(',')[0]] = round(float(p.split(',')[1]),2)
        scoreboard = sorted(scoreboard.items(), key=lambda x:x[1])

        output = '⬜🟨🟩PUNTUACIÓN MEDIA🟩🟨⬜\n'
        for k,i in enumerate(scoreboard,start=1):
            output += '\n{}. {} - {} puntos'.format(str(k), i[0], i[1])
        update.message.reply_text(output)

def check_wordle(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('Ups! Creo que no deberíamos estar hablando...')
    
    else:
        try:
            msg = update.message.text.split('\n')
            username = update.effective_user.first_name
            day = int(msg[0].split(' ')[2].replace('#',''))
            tries = int(msg[0].split(' ')[3][0])

            content = [username, day, tries]

            for i in range(tries):
                content.append(msg[i+2])

            save(content)

            update.message.reply_text('Registrado ✅')
        except:
            return

    updater = Updater("TOKEN")
def run_bot():

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("quehaces", wdid))
    dispatcher.add_handler(CommandHandler("encendido", am_on))
    dispatcher.add_handler(CommandHandler("wordlerank", wordlerank))
    dispatcher.add_handler(CommandHandler("media", avg_pts))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_wordle))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    run_bot()