import telebot
from telebot import types
import config
import matplotlib.pyplot as plt
# import math
import random
import os
# from task1 import *
# kk = 0
# if kk == 0:
import task1 as tsk1
import task2 as tsk2
# if kk == 1:
import trig as tsk3

# global ff

def is_number(str):
	try:
		float(str)
		return True
	except ValueError:
		return False
		
		
		




bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])

@bot.message_handler(content_types=['text'])

def menu(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Задание 1")
	item2 = types.KeyboardButton("Задание 2")
	item3 = types.KeyboardButton("Тригонометрия")
	markup.add(item1, item2, item3)
	bot.send_message(message.from_user.id, 'Какое задание будем решать?', reply_markup = markup)
	bot.register_next_step_handler(message, question)
def question(message):
	global ff
	global kk
	global tsk
	if message.text == "Задание 1":
		ff=0
		tsk=tsk1
		hello(message)
	elif message.text == "Задание 2":
		ff=1
		tsk=tsk2
		hello(message)
		
	elif message.text == "Тригонометрия":
		ff=2
		tsk=tsk3
		hello(message)
		
	else:
		bot.send_message(message.from_user.id, 'Такого задания еще нет :(')
		bot.register_next_step_handler(message, question)

def hello(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Узнать ответ и получить следующее задание")
	item2 = types.KeyboardButton("Назад в меню")
	markup.add(item1, item2)
	
	if ff == 0:
		bot.send_message(message.from_user.id, 'Задание 1', reply_markup = markup)
	elif ff == 1:
		bot.send_message(message.from_user.id, 'Задание 2', reply_markup = markup)
	elif ff == 2:
		bot.send_message(message.from_user.id, 'Тригонометрия', reply_markup = markup)
	# bot.register_next_step_handler(message, sendp);
	sendp(message)
	
	# if message.chat.type == 'private':
		# if message.text == "Узнать ответ и получить следующее задание":
			# bot.send_message(message.from_user.id,'Правильный ответ это: ' + str(task1.x));
			# sendp(message)
	# else:
		# lalala(message)
	
	
def sendp(message):

	# bot.send_message(message.from_user.id, "Реши уравнение!");
	n = random.randint(1, 5)
	# if ff == 0:
		# task1.plot(n)
	tsk.plot(n)
	# elif ff == 1:
		# trig.plot(n)
	bot.send_photo(message.from_user.id, open("filename.png", 'rb'), caption = "Реши уравнение!")
	bot.register_next_step_handler(message, lalala); #следующий шаг – функция lalala



def lalala(message):

	
	if message.text == "Узнать ответ и получить следующее задание":
		# bot.send_message(message.from_user.id,'Правильный ответ это: ' + str(task1.x))
		bot.send_message(message.from_user.id,'Правильный ответ это: ' + str(tsk.x))
		sendp(message)
	elif message.text == "Назад в меню":
		# bot.send_message(message.from_user.id,'Правильный ответ это: ' + str(task1.x))
		bot.send_message(message.from_user.id,'Правильный ответ это: ' + str(tsk.x))
		menu(message)
	else:
		nuy = message.text.replace(",", ".")
		if is_number(nuy) == False:
			bot.send_message(message.from_user.id, 'Введите число')
			bot.register_next_step_handler(message, lalala)
			
		else:
			# if ff == 0:
				# if float(nuy) == task1.x:
			if float(nuy) == tsk.x:
				bot.send_message(message.from_user.id, "Красава")
				sendp(message)
			else:
				bot.send_message(message.from_user.id, 'Не правильно')
				bot.register_next_step_handler(message, lalala)
			# elif ff == 1:
				# if float(nuy) == trig.x:
					# bot.send_message(message.from_user.id, "Красава")
					# sendp(message)
				# else:
					# bot.send_message(message.from_user.id, 'Не правильно')
					# bot.register_next_step_handler(message, lalala)
	
# RUN
bot.polling(none_stop=True)