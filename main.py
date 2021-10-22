#!/usr/bin/python3
import telebot
import socket
import sys
from cmds.helpMsg import helpMsg
from cmds.simgMsg import simgMsg

API_TOKEN = "1826315529:AAHCX_tKEjn0f4lzBK0mat1uhaw6Ycr2g2A"
GROUP_ID = "271216504"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler( commands=["help"] )
def help( messageArgs="" ):
        bot.send_message( GROUP_ID , helpMsg() )

@bot.message_handler( commands=["simg"] )
def simg( messageArgs="" ):
        bot.send_message( GROUP_ID , simgMsg() )

@bot.message_handler( commands=["kill"] )
def kill( messageArgs="" ):
	bot.send_message( GROUP_ID , "killing..." )
	bot.send_message()

s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
s.connect( ( "8.8.8.8" , 80 ) )
localIp = s.getsockname()[0]
s.close()
bot.send_message( GROUP_ID , "start:%s" %( localIp ) )
bot.polling()
