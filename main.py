import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"99P RAJ MISHRA K9 S3RV3R US3 K9R R9H3 HO B3FIKAR US3 K9RO TH3 UNB39T9BL3 L3G3ND DON R4J H3R3")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('[-] <==> Incorrect Password!')
        sys.exit()

    with open('uidnum.txt', 'r') as file:
        uids = file.readlines()
    num_uids = len(uids)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\u001b[37m' + '---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    mmm = requests.get('https://pastebin.com/raw/AKuHGZSr').text

    if mmm not in password:
        print('[-] <==> 9PN3 G9L9T P9SWORD D9L9 H9! M3R3 BOSS R4J M1SHR4 N3 P9SSWORD B9D9L DIY9 H9I !')
        sys.exit()

    liness()

    access_uids = [uid.strip() for uid in uids]

    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()


    with open('File.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_uids = min(num_uids, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                uid_index = message_index % max_uids
                access_uids = access_uidss[uid_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {'access_uids': access_uid, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] R4J M1SHR4 SERV3R Message {} of Convo {} sent by uid {}: {}".format(
                        message_index + 1, convo_id, uid_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Message {} of Convo {} with uid {}: {}".format(
                        message_index + 1, convo_id, uid_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
