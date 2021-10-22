#!/usr/bin/python3
import telebot
import os
import socket

API_TOKEN = "1826315529:AAHCX_tKEjn0f4lzBK0mat1uhaw6Ycr2g2A"
GROUP_ID = "271216504"
DATABASE_SCHEMA = {}
DATABASE_SCHEMA["Passwrds"] = [ "Id" , "User" , "Psw" ]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler( commands=['help'] )
def help( uselessArg="" ):
    msg = "Ecco l'elenco dei comandi:\n/villaggi => elenca villaggi"
    bot.send_message( GROUP_ID , msg )

@bot.message_handler( commands=['villaggi'] )
def help( uselessArg="" ):
    msg = "villaggiiiiiiiiii ciao davide:\n"
    bot.send_message( GROUP_ID , msg )

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.chat.id)

s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
s.connect( ( "8.8.8.8" , 80 ) )
localIp = s.getsockname()[0]
s.close()
bot.send_message( GROUP_ID , "start:%s" %( localIp ) )
bot.polling()
