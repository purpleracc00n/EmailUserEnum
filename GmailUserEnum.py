import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

import colorama
from colorama import Fore, Style
import argparse
import sys
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("-p","--profile", help="Directory location of the browser profile in use. Default: /home/kali/.config/google-chrome/Default", type=str)
parser.add_argument("-e","--email", help="Email of the ", type=str)
parser.add_argument("-f","--file", help="File containing a list of Gmail addresses to check", type=str)
args = parser.parse_args()

if args.file is not None:
	try:
		with open(args.file,"r") as emails:
			pass
	except:
		print(f"{Fore.RED}[!] Could not read from the given location. Exiting... {Style.RESET_ALL}")
		sys.exit(1)
else:
	print(f"{Fore.RED}[!] No target email list provided. Exiting... {Style.RESET_ALL}")
	sys.exit(1)

class GmailEnumerator():
	def __init__(self, p, e):
		self.profile_location = p
		self.email = e 

	def do_login(self):
		try:
			options = uc.ChromeOptions()
			options.add_argument(f"user-data-dir={self.profile_location}")
			self.driver = uc.Chrome(options=options,use_subprocess=True)
			self.driver.get("https://myaccount.google.com/")
			html = self.driver.page_source
			if f"({self.email})" in html:
				return True
			else:
				return False
		except Exception as ex:
			return False
			
	def lookup_gmail(self, email):
			self.driver.get(f'https://calendar.google.com/calendar/u/0/embed?src={email}&pli=1')
			check_value = str(self.driver.find_element(By.ID,"calendarTitle").get_attribute('innerText'))
			
			if email in check_value and "Google Calendar" not in check_value:
				return True
			else:
				return False

ge = GmailEnumerator(args.profile, args.email)
if not ge.do_login():
	print(f"{Fore.RED}[-] Login Failed. Exiting... {Style.RESET_ALL}")
	sys.exit(1)
else:
	print(f"{Fore.GREEN}[+] Login Successful...!!{Style.RESET_ALL}")

with open(args.file,"r") as emails:
	for email in emails:
		e = email.rstrip("\n")
		exists = ge.lookup_gmail(e)
		if exists:
			print(f"{Fore.GREEN}[+] Valid gmail address: {e} {Style.RESET_ALL}")
