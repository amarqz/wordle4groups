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
        update.message.reply_text('A hablarte, no.')
    else:
        update.message.reply_text('Ahora mismo me dedico a guardar vuestros resultados de Wordle para cositas que se vendrán... 😏')

def wordlerank(update: Update, context: CallbackContext):
    if update.message.chat_id != chat_id:
        update.message.reply_text('¿Qué quieres?')
    else:
        with open("saves/overall.csv") as f:
            rank = f.read().split('\n')
        
        users = []
        points = []
        for p in rank:
            users.append(p.split(',')[0])
            points.append(p.split(',')[1])
        users = [x for _,x in sorted(zip(points,users),reverse=True)]
        points = sorted(points,reverse=True)

        output = '⬜🟨🟩CLASIFICACIÓN🟩🟨⬜\n'
        k = 0
        while k < len(users):
            output += '\n{}. {} - {} puntos'.format(str(k+1), users[k], points[k])
            k += 1
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

            i = 0
            while(i<tries):
                content.append(msg[i+2])
                i = i + 1

            save(content)

            update.message.reply_text('Registrado ✅')
        except:
            return

def main():
    updater = Updater("TOKEN")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("quehaces",wdid))
    dispatcher.add_handler(CommandHandler("encendido", am_on))
    dispatcher.add_handler(CommandHandler("wordlerank", wordlerank))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_wordle))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()