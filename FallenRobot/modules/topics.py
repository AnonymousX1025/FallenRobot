import mysql.connector
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up SQL database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)


def add_topic(update: Update, context: CallbackContext):
    # Get topic from user message
    topic = ' '.join(context.args)

    # Insert topic into database
    mycursor = mydb.cursor()
    sql = "INSERT INTO topics (name) VALUES (%s)"
    val = (topic,)
    mycursor.execute(sql, val)
    mydb.commit()

    # Send confirmation message to user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Topic '{topic}' added!")

def list_topics(update: Update, context: CallbackContext):
    # Get list of topics from database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name FROM topics")
    topics = [row[0] for row in mycursor.fetchall()]

    # Send list of topics to user
    if topics:
        message = "Current topics:\n\n"
        for topic in topics:
            message += f"- {topic}\n"
    else:
        message = "No topics found."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN)

def remove_topic(update: Update, context: CallbackContext):
    # Get topic from user message
    topic = ' '.join(context.args)

    # Remove topic from database
    mycursor = mydb.cursor()
    sql = "DELETE FROM topics WHERE name = %s"
    val = (topic,)
    mycursor.execute(sql, val)
    mydb.commit()

    # Send confirmation message to user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Topic '{topic}' removed!")


# Set up updater and dispatcher
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('addtopic', add_topic))
dispatcher.add_handler(CommandHandler('listtopics', list_topics))
dispatcher.add_handler(CommandHandler('removetopic', remove_topic))
