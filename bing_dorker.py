#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Script Created By:
	Cr4sHCoD3
Created on:
	May 4, 2018
Copyrights:
	Cr4sHCoD3 2018
Special Mentions:
	PureHackers PH
	Blood Security Hackers
"""



import time
import datetime
import os
import sys
import platform
import re
import requests
from bs4 import BeautifulSoup



def clear():
	if platform.system() == 'Linux':
		os.system('clear')
	elif platform.system() == 'Windows':
		os.system('cls')
	elif platform.system() == 'Darwin':
		os.system('clear')



def banner():
	if platform.system() == 'Windows':
		return  (""" /$$$$$$$  /$$                           /$$$$$$$                      /$$                          
| $$__  $$|__/                          | $$__  $$                    | $$                          
| $$  \ $$ /$$ /$$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$ | $$| $$__  $$ /$$__  $$      | $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$  \ $$| $$  \ $$      | $$  | $$| $$  \ $$| $$  \__/| $$$$$$/ | $$$$$$$$| $$  \__/
| $$  \ $$| $$| $$  | $$| $$  | $$      | $$  | $$| $$  | $$| $$      | $$_  $$ | $$_____/| $$      
| $$$$$$$/| $$| $$  | $$|  $$$$$$$      | $$$$$$$/|  $$$$$$/| $$      | $$ \  $$|  $$$$$$$| $$      
|_______/ |__/|__/  |__/ \____  $$      |_______/  \______/ |__/      |__/  \__/ \_______/|__/      
                         /$$  \ $$                                                                  
                        |  $$$$$$/      Created By: Cr4sH CoD3
                         \______/       PureHackers | Blood Security Hackers
        """)
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		return ("""██████╗ ██╗███╗   ██╗ ██████╗     ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║██╔██╗ ██║██║  ███╗    ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██████╔╝
██╔══██╗██║██║╚██╗██║██║   ██║    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║██║ ╚████║╚██████╔╝    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗██║  ██║
╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
      Created By: Cr4sH CoD3   ~~~|~~~   PureHackers | Blood Security Hackers
		""").replace('█', '\033[32m█\033[0m').replace('╗', '\033[31m╗\033[0m').replace('║', '\033[31m║\033[0m').replace('╝', '\033[31m╝\033[0m').replace('╔', '\033[31m╔\033[0m').replace('═', '\033[31m═\033[0m').replace('╚', '\033[31m╚\033[0m').replace('Created By: Cr4sH CoD3   ~~~|~~~   PureHackers | Blood Security Hackers', '\033[97mCreated By: Cr4sH CoD3   \033[32m~~~\033[31m|\033[32m~~~   \033[97mPureHackers | Blood Security Hackers\033[0m')



def get_width(ii):
	global sizex
	global sizey
	if platform.system() == 'Windows':
		from ctypes import windll, create_string_buffer
		h = windll.kernel32.GetStdHandle(-12)
		csbi = create_string_buffer(22)
		res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
		if res:
			import struct
			(bufx, bufy, curx, cury, wattr,
			left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
			sizex = right - left + 1
			sizey = bottom - top + 1
		else:
			sizex, sizey = 80, 25
	elif platform.system() == 'Linux':
		sizey, sizex = os.popen('stty size', 'r').read().split()
	search(ii)



def search(ii):
	iteration = 1
	links = []
	if platform.system() == 'Windows':
		print ('~' * int(sizex))
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		print ('\033[31m~\033[0m' * int(sizex))
	for i in range(len(ii)):
		search_dork_param = search_engine.replace('<param1>', param1).replace('<param2>', str(iteration))
		if platform.system() == 'Windows':
			print ('[+] - ' + search_dork_param)
		elif platform.system() == 'Linux' or platform.system() == 'Darwin':
			print ('\033[34m[+] \033[31m- \033[97m' + search_dork_param + '\033[0m')
		search_dork = requests.get(search_dork_param)
		search_dork_soup = BeautifulSoup(search_dork.text, 'html.parser')
		for link in search_dork_soup.find_all('h2'):
			link = link.find('a', href=True)
			try:
				l1nk = link['href']
				links.append(l1nk)
			except TypeError:
				continue
		iteration = iteration + 10
	if platform.system() == 'Windows':
		print ('~' * int(sizex))
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		print ('\033[31m~\033[0m' * int(sizex))
	for link in links:
		if platform.system() == 'Windows':
			print ('[+] - ' + link)
		elif platform.system() == 'Linux' or platform.system() == 'Darwin':
			print ('\033[34m[+] \033[31m- \033[97m' + link + '\033[0m')
	if platform.system() == 'Windows':
		print ('~' * int(sizex))
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		print ('\033[31m~\033[0m' * int(sizex))
	if platform.system() == 'Windows':
		user = raw_input('Do you want to save the results? > ')
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		user = raw_input('\033[32mDo you want to save the results? \033[31m> \033[97m')
	if user == 'y' or user == 'Y' or user == 'yes' or user == 'Yes' or user == 'YES':
		if platform.system() == 'Windows':
			filename = raw_input('Filename > ')
		elif platform.system() == 'Linux' or platform.system() == 'Darwin':
			filename = raw_input('\033[32mFilename \033[31m> \033[97m')
		if '.txt' in filename:
			filename = filename
		elif '.txt' not in filename:
			filename = filename + '.txt'
		if os.path.isfile(filename) == True:
			if platform.system() == 'Windows':
				print ('[+] File 200')
				print ('[~] Appending...')
			elif platform.system() == 'Linux' or platform.system() == 'Darwin':
				print ('\033[34m[+] \033[33mFile 200\033[0m')
				print ('\033[34m[~] \033[97mAppending...')
			output = open(filename, 'a+')
			output.write('{0}: {1} {2}, {3} = {4}\n'.format(day, month, mday, year, current_time))
			output.write('~' * int(sizex))
			output.write('\n')
			for link in links:
				output.write(link + '\n')
			output.write('~' * int(sizex))
			output.write('\n\n')
		elif os.path.isfile(filename) != True:
			if platform.system() == 'Windows':
				print ('[+] File 404')
				print ('[~] Creating...')
			elif platform.system() == 'Linux' or platform.system() == 'Darwin':
				print ('\033[34m[+] \033[33mFile 404\033[0m')
				print ('\033[34m[~] \033[97mCreating...')
			output = open(filename, 'w+')
			output.write('{0}: {1} {2}, {3} = {4}\n'.format(day, month, mday, year, current_time))
			output.write('~' * int(sizex))
			output.write('\n')
			for link in links:
				output.write(link + '\n')
			output.write('~' * int(sizex))
			output.write('\n\n')
		if platform.system() == 'Windows':
			print ('~' * int(sizex))
		elif platform.system() == 'Linux' or platform.system() == 'Darwin':
			print ('\033[31m~\033[0m' * int(sizex))




def main():
	search_engine_len = search_engine.replace('<param1>', param1).replace('<param2>', '1')
	se_len = requests.get(search_engine_len)
	se_len_soup = BeautifulSoup(se_len.text, 'html.parser')
	se_search_count = se_len_soup.find('span', attrs={'class': 'sb_count'})
	try:
		se_search_count_result = se_search_count.text.strip().replace(' results', '')
	except AttributeError:
		print ('No result found!')
		sys.exit()

	search_engine_len = search_engine
	search_engine_len = search_engine_len.replace('<param1>', param1).replace('<param2>', se_search_count_result).replace(',', '')
	se_len = requests.get(search_engine_len)
	se_len_soup = BeautifulSoup(se_len.text, 'html.parser')
	se_search_count = se_len_soup.find('span', attrs={'class': 'sb_count'})
	se_search_count_result1 = se_search_count.text.strip().replace(' results', '') #.replace(se_search_count_result, '').replace(' of', '')
	se_search_count_result1_index = se_search_count_result1.index(' of ')
	se_search_count_result2 = se_search_count_result1.replace(se_search_count_result1[:se_search_count_result1_index], '').replace(' of ', '')
	if se_search_count_result2 != se_search_count_result:
		se_search_count = se_search_count_result2
	elif se_search_count_result2 == se_search_count_result:
		se_search_count_result1 = se_search_count_result1[:se_search_count_result1_index]
		se_search_count = se_search_count_result1.split('-', 1)[1]

	i = 1
	ii = []
	while i < int(se_search_count):
		ii.append(i)
		i = i + 10
	get_width(ii)



if __name__ == '__main__':
	clear()
	print (banner())
	month = datetime.date.today().strftime("%B")
	if datetime.date.today().strftime("%w") == 1 or datetime.date.today().strftime("%w") == '1':
		day = 'Monday'
	elif datetime.date.today().strftime("%w") == 2 or datetime.date.today().strftime("%w") == '2':
		day = 'Tuesay'
	elif datetime.date.today().strftime("%w") == 3 or datetime.date.today().strftime("%w") == '3':
		day = 'Wednesday'
	elif datetime.date.today().strftime("%w") == 4 or datetime.date.today().strftime("%w") == '4':
		day = 'Thursday'
	elif datetime.date.today().strftime("%w") == 5 or datetime.date.today().strftime("%w") == '5':
		day = 'Friday'
	elif datetime.date.today().strftime("%w") == 6 or datetime.date.today().strftime("%w") == '6':
		day = 'Saturday'
	elif datetime.date.today().strftime("%w") == 7 or datetime.date.today().strftime("%w") == '7':
		day = 'Sunday'
	mday = datetime.date.today().strftime("%d")
	year = datetime.date.today().strftime("%Y")
	current_datetime = datetime.datetime.now()
	current_time = current_datetime.strftime('%I:%M:%S')
	search_engine = 'https://www.bing.com/search?q=<param1>&first=<param2>'
	if platform.system() == 'Windows':
		param1 = raw_input('Dork > ')
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		param1 = raw_input('\033[32mDork \033[97m> ')
	main()
