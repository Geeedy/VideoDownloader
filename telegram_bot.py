import telebot
import time
import parser
import downloader
import os

token='7881010489:AAGzls-74FC0EMlYvvyHNJ9PB24lsVEJEj8'
bot=telebot.TeleBot(token)


@bot . message_handler ( content_types = [ 'text'])
def  handle_text ( message ):
  if  message.chat.id == 1242255971:
    link = parser.get_link_motherless(message.text)
    downloader.download(link)
    video = open('file.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    os.remove('file.mp4')
  else:
    bot.send_message(message.chat.id, 'ERROR')




while True:
  try:
    bot.polling()
  except:
    time.sleep(5)