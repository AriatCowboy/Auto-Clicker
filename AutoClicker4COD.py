import time
import threading
import datetime
import os
import ctypes


def menu():
	print('Option 1: Autoclicker')
	print('Option 2: Macro')
	Choice = input("Which option would you like?")
	if Choice == '1':
		Autoclicker()
	elif Choice == '2':
		macro()
	else:
		os.system('cls')
		print('dont be a dumbass type 1 or 2!')

def Autoclicker():
	from pynput.mouse import Button, Controller

	delay = 0.01
	button = Button.left
	number_of_clicks = 500

	number_of_click = input('How many clicks?')
	number_of_clicks = int(number_of_click)
	mouse = Controller()
	begin = 1
	number_clicked = 0
	time.sleep(10)
	if begin == 1:
		while number_clicked < number_of_clicks:
			mouse.press(button)
			time.sleep(.01)
			mouse.release(button)
			time.sleep(20)
			number_clicked += 1
			if number_clicked == number_of_clicks:
				begin = 0
				exit()
def macro():
	from pynput.keyboard import Listener, KeyCode, Key, Controller
	begin = 1
	keyboard = Controller()
	while begin == 1:
		keyboard = Controller()
		start_time = time.time()
		elapsed_time = time.time() - start_time
		keyboard.press('e')
		time.sleep(.01)
		keyboard.release('e')
		time.sleep(.01)
		if elapsed_time == 86400:
			begin = 0
			exit()

def exit():
	print('You are clear to exit!')
menu()
