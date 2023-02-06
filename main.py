import requests
import argparse
import json
import colorama
import sys
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def banner():
	print(f"{Style.BRIGHT}{Back.GREEN}{Fore.WHITE}.  .                              .   ")
	print(f"{Style.BRIGHT}{Back.GREEN}{Fore.WHITE}|  | __ _ ._ _  ___  __ _  _.._. _.|_ ")
	print(f"{Style.BRIGHT}{Back.GREEN}{Fore.WHITE}|__|_) (_)[ | )     _) (/,(_][  (_.[ )")
	print()
	print(f"           {Style.BRIGHT}{Fore.BLACK}{Back.RED}Github: thealper2")
	print()
	print()

def scan(types, query):
	banner()
	api = "https://www.usom.gov.tr/api/address/index"
	parameters = {"q": query, "type": types}
	res = requests.get(api, params=parameters)
	res_json = json.loads(res.content)

	code = res_json['count']

	if code == 1:
		model   = res_json['models']
		kID     = model[0].get('id')
		kURL    = model[0].get('url')
		kTYPE   = model[0].get('type')
		kDESC   = model[0].get('desc')
		kSOURCE = model[0].get('source')
		kDATE   = model[0].get('date')
		kCRT    = model[0].get('criticality_level')
		kCON    = model[0].get('connectiontype')
		kLINK   = "https://www.usom.gov.tr/adres/" + str(kID)

		print(f"\t{Style.BRIGHT}{Fore.GREEN}[ID]:     ", kID)
		print(f"\t{Style.BRIGHT}{Fore.GREEN}[URL]:    ", kURL)
		print(f"\t{Style.BRIGHT}{Fore.RED}[TYPE]:   ", kTYPE)
		print(f"\t{Style.BRIGHT}{Fore.YELLOW}[DESC]:   ", kDESC)
		print(f"\t{Style.BRIGHT}{Fore.YELLOW}[SOURCE]: ", kSOURCE)
		print(f"\t{Style.BRIGHT}{Fore.CYAN}[DATE]:   ", kDATE)
		print(f"\t{Style.BRIGHT}{Fore.RED}[WARNING]:", kCRT)
		print(f"\t{Style.BRIGHT}{Fore.GREEN}[CONNECT]:", kCON)
		print(f"\t{Style.BRIGHT}{Fore.GREEN}[LINK]:   ", kLINK)
	else:
		print(f"{Style.BRIGHT}{Fore.YELLOW}Sorguladiginiz {types} USOM veritabaninda bulunamadi.")

argument_parser = argparse.ArgumentParser(description="USOM veritabanininda domain, url ve ip sorgulamasi yapabilirsiniz.")
argument_parser.add_argument('--domain', type=str, required=False, help="Domain sorgulamasi")
argument_parser.add_argument('--url', type=str, required=False, help="URL sorgulamasi")
argument_parser.add_argument('--ip', type=str, required=False, help="IP sorgulamasi")
arguments = argument_parser.parse_args()

if (arguments.ip != None and arguments.url == None and arguments.domain == None):
	scan("ip", arguments.ip)
	print()
	sys.exit()
elif (arguments.url != None and arguments.ip == None and arguments.domain == None):
	scan("url", arguments.url)
	print()
	sys.exit()
elif (arguments.domain != None and arguments.ip == None and arguments.url == None):
	scan("domain", arguments.domain)
	print()
	sys.exit()
else:
	argument_parser.print_help()
