import logging
import telegram as telegram_base
from telegram import ext as telegram_ext
from dynaconf import settings


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=settings['log_level']
)

logger = logging.getLogger(__name__)


def start(update: telegram_base.Update, context: telegram_ext.CallbackContext) -> None:
    update.message.reply_text('Hi!')


def help_command(update: telegram_base.Update, context: telegram_ext.CallbackContext) -> None:
    update.message.reply_text('Help!')


def main() -> None:
    updater = telegram_ext.Updater(
        settings['telegram']['token_bot'],
        use_context=True
    )

    dispatcher = updater.dispatcher

    dispatcher.add_handler(telegram_ext.CommandHandler("start", start))
    dispatcher.add_handler(telegram_ext.CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
